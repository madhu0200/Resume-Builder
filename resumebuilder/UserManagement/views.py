from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import uuid
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login
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
            return redirect('register',messages)
        
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            messages.error(request, "Invalid email format")
            return redirect('register')

        # Password Length Validation
        if len(password) < 8:
            messages.error(request, "Password must contain minimum 8 characters")
            return redirect('register')

        # Password Complexity Validation
        if not re.search(r'[A-Z]', password):
            messages.error(request, "Password must contain one uppercase letter")
            return redirect('register')

        if not re.search(r'[a-z]', password):
            messages.error(request, "Password must contain one lowercase letter")
            return redirect('register')

        if not re.search(r'[0-9]', password):
            messages.error(request, "Password must contain one number")
            return redirect('register')

        username=f"{first_name.lower()}_{uuid.uuid4().hex[:6]}"
        email_existed= User.objects.filter(email=email)
        if email_existed:
            messages.error(request,"email already existed")
            return redirect('register',messages)
        user=User.objects.create( username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        if user:
            return redirect('login')
        else:
            messages.error(request,"some error occured please try after some time")
            return redirect('register',messages)


def login_user(request):
    if request.method=='GET':
        return render(request,'UserManagement/Login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']

         # Find user using email
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid Email")
            return redirect('login')

        # Authenticate using username
        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')

        else:
            messages.error(request, "Invalid Password")
            return redirect('login')


