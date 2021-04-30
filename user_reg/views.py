from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST' :
        uname= request.POST["username"]
        pssw= request.POST["pass"]

        user = User.objects.create_user(username= uname, password = pssw)
        user.save()
        print('customer registered')
        return redirect("/user_login")

    else:
        return render(request,"register.html")
