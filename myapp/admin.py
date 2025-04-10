from django.contrib import admin
from .models import (
     IndexSlider, AboutUs, ExploreTopSubjects,
     Courses, Teachers, TestimonialSlider,
     GetInTouch,Contact,EmailSubscription,Blog,CourseRegistration)


class contact_filter(admin.ModelAdmin):
    list_display = ('name','email', 'created_at', 'updated_at')
    search_fields = ('name','email')

class index_slider(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at', 'updated_at')
    search_fields = ('title','subtitle')

class about_us(admin.ModelAdmin):
    list_display = ('h1', 'description', 'created_at', 'updated_at')
    search_fields = ('h1', 'description')

class explore_top_subjects(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

class courses(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

class teacher(admin.ModelAdmin):
    list_display = ('name', 'profession', 'created_at', 'updated_at')
    search_fields = ('name', 'profession')

class testimonial_slider(admin.ModelAdmin):
    list_display = ('name', 'professions', 'created_at', 'updated_at')
    search_fields = ('name', 'professions')

class get_in_touch(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    search_fields = ('email',)

class subscription_filter(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    search_fields = ('email',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at', 'is_active']
    search_fields = ['title', 'author']
    readonly_fields = ['slug']

class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'phone')
    search_fields = ('user__username', 'user__email', 'experience')
    list_filter = ('experience',)

admin.site.register(CourseRegistration, CourseRegistrationAdmin)
admin.site.register(Contact, contact_filter)
admin.site.register(IndexSlider, index_slider)
admin.site.register(AboutUs, about_us)
admin.site.register(ExploreTopSubjects, explore_top_subjects)
admin.site.register(Courses, courses)
admin.site.register(Teachers, teacher)
admin.site.register(TestimonialSlider, testimonial_slider)
admin.site.register(GetInTouch, get_in_touch)
admin.site.register(EmailSubscription, subscription_filter)
admin.site.register(Blog, BlogAdmin)

