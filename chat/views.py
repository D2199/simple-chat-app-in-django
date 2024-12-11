from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout,aauthenticate,alogin
from django.contrib.auth.models import User

def login(request):
    if request.method=="POST": 
        # print(request.POST['username'],request.POST['password'])
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        # print(dir(user))
        if user is not None:
            # print('user Exest',user)
            login(request)
            # print(help(login))

            return 
        # redirect('dashboard')
        
    return render(request,'login.html')

def dashboard(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated :
        users=User.objects.all()
        users=[user.username for user in User.objects.all()]
        print(users)
        return render(request,'dashboard.html',{'users':users})
    return redirect('login')

def chat(request,to):
     if request.user.is_authenticated :
        recivers=User.objects.filter(username=to)
        
        # messages=Message.objects.filter(user=request.user,to=reciver)
        for reciver in recivers:
            # print(reciver.id)
            messages=Message.objects.filter(to=reciver)
            # print(messages)
        return render(request,'chat.html',{'massages':[message for message in messages],'to':to})

def addMsg(request):
    if request.user.is_authenticated:
        to=request.POST["to"]
        recivers=User.objects.filter(username=to)
        for reciver in recivers:
            massage=request.POST["massage"]
            msg=Message(value=massage,froms=request.user,to=to)
            msg.save()
            print(massage)
    
   

    return HttpResponse({"success"})

def register(request):
    if request.method=="POST": 
        # print(request.POST['username'],request.POST['password'])
        try :
            user=User.objects.create_user(request.POST['username'],request.POST['password'])
            user.save()
            print(user)
        except Exception as e:
            return HttpResponse(e)
        return redirect('login')
    return render(request,'register.html')
        
def logout(req):
    logout(req)
    return redirect('login')