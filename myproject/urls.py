from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('single/<slug:slug>/', views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('teacher/', views.teacher, name='teacher'),
    path('test/', views.testpage, name='test'),
    path('logout/', views.logout_page, name='logout'),
    path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('profile_page/', views.profile_page, name='profile'),
    path('course_blog/<int:pk>', views.course_blog, name='course_blog'),
    path('course_apply/', views.course_apply, name='course_apply'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)