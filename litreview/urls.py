# from ast import pattern
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
                               redirect_authenticated_user=True),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', blog.views.home, name='home'),
    path('post/', blog.views.post, name='post'),
    path('blog/ticket/', blog.views.create_ticket, name='ask_review'),
    path('blog/review', blog.views.create_review, name='create_review'),
    path('blog/ticket/<int:blog_id>/review_response', blog.views.create_review_response_ticket, name='review_response'),
    path('blog/<int:blog_id>', blog.views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit_review', blog.views.edit_review, name='edit_review'),
    path('blog/<int:blog_id>/delete_review', blog.views.delete_review, name='delete_review'),
    path('blog/<int:blog_id>/edit_ticket', blog.views.edit_ticket, name='edit_ticket'),
    path('blog/<int:blog_id>/delete_ticket', blog.views.delete_ticket, name='delete_ticket'),
    path('follow-users/', blog.views.follow_users, name='follow_users'),
    path('follow-users/<int:follows_id>/remove', blog.views.unfollow_follow_users, name="remove_follow_users"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += pattern('', (
#     r'^static/(?P<path>.*)$',
#     'django.views.static.serve',
#     {'document_root': settings.STATIC_ROOT}
# ))