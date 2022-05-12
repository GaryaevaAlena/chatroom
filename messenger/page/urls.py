from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    re_path(r'^profile/edit/$', profile_edit, name='edit'),
    re_path(r'^profile/$', UserProfile.as_view(), name='myprofile'),
    path('profile/<int:pk>/', Profile.as_view(), name='profiles'),
    path('', NewChat.as_view(), name='newchat'),
    path('<int:pk>/edit/', EditChat.as_view(), name='chat_edit'),
    path('<int:pk>/', Chatter.as_view(), name='chatter'),

]