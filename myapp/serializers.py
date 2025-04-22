from rest_framework import serializers
from .models import Blog, Category
from myapp.models import (CourseRegistration, IndexSlider, AboutUs,
                          ExploreTopSubjects,Courses,Teachers,TestimonialSlider,
                          GetInTouch,Category)

class BlogSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    author = serializers.PrimaryKeyRelatedField(queryset=CourseRegistration.objects.all())

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'title2',
            'image', 'image2',
            'author', 'description', 'main_content',
            'slug', 'is_active', 'category',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

class IndexSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexSlider
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'h1',
                  'description', 'url',
                  'image', 'created_at', 'updated_at'
                  ]
        read_only_fields = ['created_at', 'updated_at']

class ExploreTopSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploreTopSubjects
        fields = ['id', 'title',
                  'description', 'url',
                  'image', 'created_at','updated_at'
                  ]

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'title', 'h1', 'course_description', 'courese_requirements', 'image',
                  'course_hour', 'student_count', 'course_star', 'course_comment_count', 'slug',
                  'course_price', 'created_at', 'updated_at']

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'name', 'image', 'profession', 'created_at', 'updated_at',
                  'READ_ME', 'social_media_url_1', 'social_media_icon_1',
                  'social_media_url_2', 'social_media_icon_2',
                  'social_media_url_3', 'social_media_icon_3']

class TestimonialSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialSlider
        fields = ['id', 'name', 'professions', 'image', 'comment', 'created_at', 'updated_at']

class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = ['id', 'location', 'location_url', 'phone_number', 'email', 'created_at', 'updated_at',
                  'social_media_url_1', 'social_media_icon_1', 'social_media_url_2', 'social_media_icon_2',
                  'social_media_url_3', 'social_media_icon_3', 'social_media_url_4', 'social_media_icon_4']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']