"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# agregamos acciones de usuarios (login, logout)
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'),
         name='reset_password'),
]

# agregamos acciones propias
from django.urls import include
from . import views

urlpatterns += [
    # homapage
    path('', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
    path('statistics/', views.statistics, name='stats'),
    path('tables/', views.tables, name='tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('editors/', views.editors, name='editors'),
    path('forms/', views.forms, name='forms'),

    # registro y perfil de usuario
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    # blog
    # path('noticias/', include('apps.blog.urls'), name='blog'),
]


from django.conf import settings
from django.conf.urls.static import static

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
