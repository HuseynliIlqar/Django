from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('single/<slug:slug>/', views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search_bar, name='search'),
    path('teacher/', views.teacher, name='teacher'),
    path('login_page/', views.joinNow, name='login_page'),
    path('test/', views.testpage, name='test'),
    path('logout', views.logout_page, name='logout'),
    path('register_page/', views.register_page, name='register_page'),
    path('profile_page/', views.profile_page, name='profile'),
    path('course_blog/<int:pk>', views.course_blog, name='course_blog'),
    path('course_apply/<int:course_id>/', views.course_apply, name='course_apply'),
]