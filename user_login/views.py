from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def userlogin(request):
    if request.method== 'POST':
        uname= request.POST["username"]
        pssw= request.POST["pass"]
        user= auth.authenticate(username= uname, password = pssw)

        if user is not None:
            auth.login(request,user)
            if user.is_superuser== True:
                return redirect("/adminhome")
            else:
                return redirect("/user_tasks")
        else:
            print('invalid credentials')
            return redirect("/user_login")


    else:
        return render(request, "userlogin.html")
