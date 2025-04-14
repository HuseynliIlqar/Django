from django.contrib import admin
from .models import (
    IndexSlider, AboutUs, ExploreTopSubjects,
    Courses, Teachers, TestimonialSlider,
    GetInTouch, Contact, EmailSubscription, Blog, CourseRegistration,
    Category,Comment,UpdateFontAwesome)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body','active','published_date']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at', 'is_active']
    search_fields = ['title', 'author']
    readonly_fields = ['slug']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'email')

@admin.register(IndexSlider)
class IndexSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('h1', 'description', 'created_at', 'updated_at')
    search_fields = ('h1', 'description')

@admin.register(ExploreTopSubjects)
class ExploreTopSubjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ['slug']

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'created_at', 'updated_at',)
    search_fields = ('name', 'profession',)
    readonly_fields = ('READ_ME', 'created_at', 'updated_at',)
    fields = ('name', 'profession','image',
              'READ_ME',
              'social_media_url_1','social_media_icon_1',
              'social_media_url_2','social_media_icon_2',
              'social_media_url_3','social_media_icon_3')

@admin.register(TestimonialSlider)
class TestimonialSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'professions', 'created_at', 'updated_at')
    search_fields = ('name', 'professions')

@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    search_fields = ('email',)

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    search_fields = ('email',)

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'phone')
    search_fields = ('user__username', 'user__email', 'experience')
    list_filter = ('experience',)

@admin.register(UpdateFontAwesome)
class UpdateFontAwesomeAdmin(admin.ModelAdmin):
    list_display = ('update_url',)
    readonly_fields = ('READ_ME','updated_at',)
    fields = ('READ_ME','update_url','updated_at',)

