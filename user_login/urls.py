from django.urls import path

from . import views

urlpatterns = [
   path('user_login/',views.userlogin,name="userlogin")
]