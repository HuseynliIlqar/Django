from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'myapp'


router = DefaultRouter()
router.register('blogs', views.BlogViewSet)
router.register('index-sliders', views.IndexSliderViewSet)
router.register('about-us', views.AboutUsViewSet)
router.register('explore-top-subjects', views.ExploreTopSubjectsViewSet)
router.register('courses', views.CoursesViewSet)
router.register('teachers', views.TeachersViewSet)
router.register('testimonial-sliders', views.TestimonialSliderViewSet)
router.register('get-in-touch', views.GetInTouchViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('single/<slug:slug>/', views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('teacher/', views.teacher, name='teacher'),
    path('test/', views.testpage, name='test'),
    path('course-apply/', views.course_apply, name='course_apply'),
    path('course_blog/<slug:slug>/', views.course_blog, name='course_blog'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('blog/<slug:slug>/', views.blog, name='blog_by_course'),
    path('auth/login/', views.login_page, name='login_page'),
    path('auth/logout/', views.logout_page, name='logout'),
    path('auth/register/', views.register_page, name='register_page'),
    path('auth/profile/', views.profile_page, name='profile'),

    path('api/', include(router.urls)),

    path('auth/', obtain_auth_token, name='api_token_auth'),
]
