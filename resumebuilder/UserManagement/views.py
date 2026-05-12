from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='GET':
        return render(request,'UserManagement/registration.html')
    else:
        first_name=request.POST['first-name']
        last_name=request.POST['last-name']
        email=request.POST['email']
        password=request.POST['password']

        confirm_password=request.POST['confirm-password']
        if password!=confirm_password:
            messages.error(request,"both passwords are not matching")
        username=f"{first_name.lower()}_{uuid.uuid4().hex[:6]}"
        print(username,first_name,last_name,email,password,confirm_password)
        user=User.objects.create( username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        if user:
            return redirect('user/login')
        else:
            messages.error(request,user)

