from django.urls import path

from . import views

urlpatterns = [
   path('user_tasks/',views.usertask,name="usertask"),
   path('adminhome/',views.adminview,name="adminhome")
]