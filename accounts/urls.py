from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [
    path('',accounts.views.index, name="index"),
    path('oauth/',accounts.views.oauth, name='oauth'),
    path('kakao_login/',accounts.views.kakao_login, name='kakao_login'),
    path('kakao_logout/',accounts.views.kakao_logout, name='kakao_logout'),
]
