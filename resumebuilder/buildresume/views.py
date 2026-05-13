from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from .models import *


# Create your views here.
@login_required
def home(request):
    if request.method=='GET':
        current_user=request.user
        personal_details=PersonalDeatils.objects.get(user=current_user)
        return render(request,'buildresume/home.html',{'personal_details':personal_details})
    
@login_required
def personal_details(request):
    print(request.method)
    if request.method=='POST':
        current_user=request.user

        fullName=request.POST['full_name']
        location=request.POST['location']
        mobile=request.POST['mobile']
        email=request.POST['email']
        github=request.POST['github']
        professionSummary=request.POST['summary']
        linkedin=request.POST['linkedin']
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            messages.error(request, "Invalid email format")
            return redirect('home')

        existed_personal_details=PersonalDeatils.objects.get(user=current_user)
        if existed_personal_details:
            existed_personal_details.FullName=fullName
            existed_personal_details.Location=location
            existed_personal_details.mobile=mobile
            existed_personal_details.email=email
            existed_personal_details.gitLink=github
            existed_personal_details.professionSummary=professionSummary
            existed_personal_details.linkedIn=linkedin
            existed_personal_details.save()
            messages.success(request,"personal details updated successfully")
            
        else:
        
            personal_details=PersonalDeatils.objects.create(user=current_user,FullName=fullName,Location=location,mobile=mobile,email=email,gitLink=github,linkedIn=linkedin,professionSummary=professionSummary)
            personal_details.save()
            if personal_details:
                messages.success(request,"personal details saved successfully")
        return redirect('home')
   
        
   
