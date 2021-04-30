from django.shortcuts import render,redirect
from .models import tasks
from django.contrib.auth.models import User
from notifications.signals import notify
from django.utils import timezone

# Create your views here.


def usertask(request):

    if request.method=='POST':
        newdesc = request.POST['newdesc']
        newtask= tasks.objects.create(creator= request.user.username, desc = newdesc)
        sender = User.objects.get(username=request.user.username)
        receiver = User.objects.get(is_superuser= True)
        message= newtask.desc
        now= timezone.now()
        newtask.save()
        notify.send(sender, recipient=receiver, verb='Message', description=message, timestamp = now)
        return redirect("/user_tasks/")
    else:
        task = tasks.objects.filter(creator = request.user.username)

        return render(request, 'cindex.html', {'tasks': task})

def adminview(request):
    if request.method=='POST':
        curid= request.POST["taskid"]
        entry = tasks.objects.get(id = curid  )
        entry.completed=True 
        sender = User.objects.get(username=request.user.username)
        receiver = User.objects.get(username=entry.creator)
        message= entry.desc
        now= timezone.now()
        entry.save()
        notify.send(sender, recipient=receiver, verb='Message', description=message, timestamp = now)
        return redirect("/adminhome/")
    else:
        task = tasks.objects.all()
        return render(request,'adminhome.html',{'tasks':task})