from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('single/<slug:slug>/', views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('teacher/', views.teacher, name='teacher'),
    path('test/', views.testpage, name='test'),
    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('profile_page/', views.profile_page, name='profile'),
    path('course_apply/', views.course_apply, name='course_apply'),
    path('course_blog/<slug:slug>/', views.course_blog, name='course_blog'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('blog/<slug:slug>/', views.blog, name='blog_by_course'),
]
