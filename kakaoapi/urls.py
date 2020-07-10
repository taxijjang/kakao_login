from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',accounts.views.index, name="index"),
    path('accounts/',include('accounts.urls')),
    path('oauth/',accounts.views.oauth,name ='oauth'),

]
