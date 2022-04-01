from django.urls import re_path
from post.models import Reels
from .views import *


urlpatterns = [
    re_path(r'post/$',Post.as_view(),name='post'),
    re_path(r'share/$',Share.as_view(),name='post'),
    re_path(r'upload_reel/$',Reels.as_view(),name="upload_reel"),
    re_path(r'reels/$',view_reels.as_view(),name="reels"),
    re_path(r'likereel/<int:id>/$',like_reels.as_view(),name="likereel"),
    re_path(r'likepost/<int:id>/$',like_post.as_view(),name="likepost"),
    re_path(r'uploadstory/$',Story.as_view(),name="upload_story"),
    re_path(r'comment/$',Comment.as_view(),name="comment"),
]

