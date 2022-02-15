<<<<<<< HEAD
"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

import tickets.views
import blog.views
import client.views
import criticize.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', client.views.login_page, name='login'),
    path('logout', client.views.logout_user, name='logout'),
    path('registration/', client.views.registration_page, name='registration'),
    path('blog/', blog.views.display, name='blog'),
    path('ticket/', tickets.views.blog_and_photo_upload, name='ticket'),
    path('criticize/', criticize.views.criticize, name='criticize')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.urls import path

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', blog.views.home, name='home'),
    path('blog/ticket/', blog.views.create_ticket, name='ask_review'),
    path('photo-feed/', blog.views.photo_feed, name='photo_feed'),
    path('blog/review', blog.views.create_review, name='create_review'),
    path('blog/<int:blog_id>', blog.views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit', blog.views.edit_blog, name='edit_review'),
    path('follow-users/', blog.views.follow_users, name='follow_users')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 988f8af (MAJ programme)
