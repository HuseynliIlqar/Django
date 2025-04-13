from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
from .forms import ContactForm, EmailSubscriptionForm,CommentForm
from .models import (
    IndexSlider, AboutUs, ExploreTopSubjects, Courses, Teachers,
    TestimonialSlider, GetInTouch, Blog, CourseRegistration,
    Category,
)

def index(request):
    about_us = AboutUs.objects.all()
    categories = Category.objects.all()
    sliders = IndexSlider.objects.all()
    explore_top_subjects = ExploreTopSubjects.objects.all()
    courses = Courses.objects.all()
    teachers = Teachers.objects.all()
    testimonials = TestimonialSlider.objects.all()
    get_in_touch = GetInTouch.objects.all()
    blogs = Blog.objects.order_by('-created_at')[:3]

    EXPERIENCES = ["Təcrübəsiz", "Tələbə", "Peşəkar"]

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        experience = request.POST.get('experience')

        if not username or not email or not phone_number or not password1 or not password2 or not experience:
            messages.error(request, "Bütün sahələri doldurun.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES
            })

        if password1 != password2:
            messages.error(request, "Şifrələr uyğun gəlmir.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES
            })

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu istifadəçi adı artıq mövcuddur.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES
            })

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu e-poçt artıq istifadə olunub.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES
            })

        if experience not in EXPERIENCES:
            messages.error(request, "Düzgün təcrübə səviyyəsi seçin.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES
            })

        myUser = User.objects.create_user(username=username, email=email, password=password1)
        myCourseRegistration = CourseRegistration(user=myUser, phone=phone_number, experience=experience)
        myCourseRegistration.save()

        messages.success(request, "Qeydiyyat uğurla tamamlandı! İndi giriş edə bilərsiniz.")
        return redirect('myapp:login_page')

    return render(request, 'index.html', {
        "sliders": sliders,
        "about_us": about_us,
        "explore_top_subjects": explore_top_subjects,
        "courses": courses,
        "teacher": teachers,
        "testimonial": testimonials,
        "get_in_touch": get_in_touch,
        "last_posts": blogs,
        'categories': categories,
        "experiences": EXPERIENCES,
    })


def about(request):
    categories = Category.objects.all()
    testimonials = TestimonialSlider.objects.all()
    about_us = AboutUs.objects.all()
    get_in_touch = GetInTouch.objects.all()
    courses = Courses.objects.all()

    return render(request, 'about.html', {
        "get_in_touch": get_in_touch,
        "about_us": about_us,
        "testimonial": testimonials,
        "courses": courses,
        'categories': categories,
    })


def contact(request):
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    courses = Courses.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız uğurla göndərildi. Tezliklə sizinlə əlaqə saxlanılacaq.")
            return redirect('myapp:contact')
        else:
            messages.error(request, "Zəhmət olmasa, formdakı səhvləri düzəldin.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        "get_in_touch": get_in_touch,
        "form": form,
        "courses": courses,
        'categories': categories,

    })


def course(request):
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    explore_top_subjects = ExploreTopSubjects.objects.all()
    courses = Courses.objects.all()

    return render(request, 'course.html', {
        "get_in_touch": get_in_touch,
        "explore_top_subjects": explore_top_subjects,
        "courses": courses,
        'categories': categories,

    })


def teacher(request):
    courses = Courses.objects.all()
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    teachers = Teachers.objects.all()

    return render(request, 'teacher.html', {
        "get_in_touch": get_in_touch,
        "teacher": teachers,
        "courses": courses,
        'categories': categories,
    })


def testpage(request):
    return render(request, 'testpage.html')


def logout_page(request):
    logout(request)
    return redirect('myapp:login_page')


def login_page(request):
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    courses = Courses.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Uğurla daxil oldunuz!")
            return redirect('myapp:profile')
        else:
            messages.error(request, "İstifadəçi adı və ya şifrə yanlışdır.")
            return render(request, 'login_page.html', {
                "get_in_touch": get_in_touch,
                "courses": courses,
            })

    return render(request, 'login_page.html', {
        "get_in_touch": get_in_touch,
        "courses": courses,
        'categories': categories,

    })


EXPERIENCES = ["Təcrübəsiz", "Tələbə", "Peşəkar"]

def register_page(request):
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    courses = Courses.objects.all()

    EXPERIENCES = ["Təcrübəsiz", "Tələbə", "Peşəkar"]

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        experience = request.POST.get('experience')

        if not username or not email or not phone_number or not password1 or not password2 or not experience:
            messages.error(request, "Bütün sahələri doldurun.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES,
                "get_in_touch": get_in_touch,
                "courses": courses,
            })

        if password1 != password2:
            messages.error(request, "Şifrələr uyğun gəlmir.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES,
                "get_in_touch": get_in_touch,
                "courses": courses,
            })

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu istifadəçi adı artıq mövcuddur.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES,
                "get_in_touch": get_in_touch,
                "courses": courses,
            })

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu e-poçt artıq istifadə olunub.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES,
                "get_in_touch": get_in_touch,
                "courses": courses,
            })

        if experience not in EXPERIENCES:
            messages.error(request, "Düzgün təcrübə səviyyəsi seçin.")
            return render(request, 'register.html', {
                "experiences": EXPERIENCES,
                "get_in_touch": get_in_touch,
                "courses": courses,
            })

        myUser = User.objects.create_user(username=username, email=email, password=password1)
        myCourseRegistration = CourseRegistration(user=myUser, phone=phone_number, experience=experience)
        myCourseRegistration.save()

        messages.success(request, "Qeydiyyat uğurla tamamlandı! İndi giriş edə bilərsiniz.")
        return redirect('myapp:login_page')

    return render(request, 'register.html', {
        'experiences': EXPERIENCES,
        "get_in_touch": get_in_touch,
        "courses": courses,
        'categories': categories,
    })

@login_required(login_url='myapp:login_page')
def profile_page(request):
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    courses = Courses.objects.all()

    user = request.user
    registration_instance = get_object_or_404(CourseRegistration, user=request.user)

    return render(request, 'profile_page.html', {
        'user': user,
        'course_registration': registration_instance,
        "get_in_touch": get_in_touch,
        "courses": courses,
        'categories': categories,
    })


def course_blog(request, slug):
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    course = get_object_or_404(Courses, slug=slug)
    courses = Courses.objects.all()

    return render(request, 'course_blog.html', {
        'get_in_touch': get_in_touch,
        'course': course,
        'courses': courses,
        'categories': categories,
    })


def course_apply(request):
    if not request.user.is_authenticated:
        return redirect('myapp:login_page')

    if request.method == "POST":
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Courses, id=course_id)

        registration = get_object_or_404(CourseRegistration, user=request.user)

        if not registration.can_apply_again():
            messages.error(request, "Siz artıq müraciət etmisiniz. 30 gün sonra yenidən cəhd edin.")
            return redirect('myapp:profile')

        user_info = (
            f"İstifadəçi adı: {request.user.username}\n"
            f"Email: {request.user.email}\n"
            f"Telefon: {registration.phone}\n"
            f"Təcrübə: {registration.get_experience_display()}\n"
            f"Kurs: {course.title}\n"
        )

        subject = "Yeni Müraciət - Login olan istifadəçi"
        message = f"Müraciət alan istifadəçinin məlumatları:\n\n{user_info}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ilqarhuseynli51@gmail.com']

        send_mail(subject, message, from_email, recipient_list)

        registration.last_applied = timezone.now()
        registration.save()

        messages.success(request, "Müraciətiniz qəbul edildi və email göndərildi!")
        return redirect('myapp:profile')

    return render(request, 'course_blog.html')


def category_posts(request, slug):
    selected_category = get_object_or_404(Category, slug=slug)
    courses = Courses.objects.all()
    posts_list = selected_category.posts.all()
    categories = Category.objects.all()
    get_in_touch = GetInTouch.objects.all()
    blogs = Blog.objects.order_by('-created_at')[:3]

    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'blog.html', {
        'selected_category': selected_category,
        'posts': posts_list,
        'page_object': page_object,
        'categories': categories,
        "last_posts": blogs,
        "get_in_touch": get_in_touch,
        "courses": courses,
    })


def blog(request, slug=None):
    get_in_touch = GetInTouch.objects.all()
    courses = Courses.objects.all()
    categories = Category.objects.all()
    last_posts = Blog.objects.order_by('-created_at')[:3]

    course = None
    if slug:
        course = get_object_or_404(Courses, slug=slug)

    keyword = request.GET.get('keyword', '')
    if keyword:
        blog_list = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(title2__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(main_content__icontains=keyword)
        ).order_by('-created_at')
    else:
        blog_list = Blog.objects.filter(is_active=True).order_by('-created_at')

    paginator = Paginator(blog_list, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Qeydiyyatınız uğurla qəbul edildi')
            return redirect('myapp:blog')
    else:
        form = EmailSubscriptionForm()

    context = {
        "get_in_touch": get_in_touch,
        "blog": blog_list,
        "page_object": page_object,
        "last_posts": last_posts,
        "courses": courses,
        "categories": categories,
        "form": form,
        "keyword": keyword,
        "course": course,
    }

    return render(request, 'blog.html', context)


def single(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    courses = Courses.objects.all()
    get_in_touch = GetInTouch.objects.all()
    categories = Category.objects.all()
    blogs = Blog.objects.order_by('-created_at')[:3]

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = post
            new_comment.author = request.user.courseregistration
            new_comment.save()
            return redirect('myapp:single', slug=post.slug)
    else:
        comment_form = CommentForm()

    context = {
        "get_in_touch": get_in_touch,
        "courses": courses,
        "post": post,
        'categories': categories,
        "last_posts": blogs,
        "comments": comments,
        "comment_form": comment_form,
        "new_comment": new_comment,
    }
    return render(request, 'single.html', context)

