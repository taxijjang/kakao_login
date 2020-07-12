from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    #path('',accounts.views.index, name="index"),
]
