from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


class IndexSlider(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    url = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    h1 = models.CharField(max_length=100)
    description= models.TextField(max_length=2000)
    url = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class ExploreTopSubjects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Courses(models.Model):
    title = models.CharField(max_length=100)
    h1 = models.CharField(max_length=100, blank=True, null=True)
    course_description = models.TextField(blank=False, null=False, max_length=1000, default="Açıqlama")
    courese_requirements = models.TextField(blank=False, null=False, max_length=1000, default="Tələblər")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    course_hour = models.CharField(max_length=10)
    student_count = models.CharField(max_length=10)
    course_star = models.CharField(max_length=10)
    course_comment_count = models.CharField(max_length=10, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    course_price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('course_blog', kwargs={'slug': self.slug})

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    profession = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    social_media_url_1 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_1 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_2 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_2 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_3 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_3 = models.CharField(max_length=20, null=True, blank=True)

class TestimonialSlider(models.Model):
    name = models.CharField(max_length=100)
    professions = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class GetInTouch(models.Model):

    location = models.CharField(max_length=50, null=True, blank=True)
    location_url = models.URLField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    social_media_url_1 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_1 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_2 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_2 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_3 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_3 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_4 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_4 = models.CharField(max_length=20, null=True, blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmailSubscription(models.Model):
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

EXPERIENCE_CHOICES = [
    ("təcrübəsiz", "Təcrübəsiz"),
    ("tələbə", "Tələbə"),
    ("peşəkar", "Peşəkar"),
]
class CourseRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default="təcrübəsiz")
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, default='default.jpg')
    bio = models.CharField(max_length=15, blank=True, null=True)
    last_applied = models.DateTimeField(null=True, blank=True)

    def can_apply_again(self):
        from datetime import timedelta

        if not self.last_applied:
            return True
        return timezone.now() - self.last_applied > timedelta(days=30)

    def __str__(self):
        return f"{self.user}"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            # Əsas slug dəyəri yaradılır
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            # Mövcud slug varsa, avtomatik counter əlavə edilir
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    title2 = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey('CourseRegistration', on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    main_content = models.TextField(max_length=5000, null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, db_index=True, blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('CourseRegistration', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.author} - {self.body[:20]}"
