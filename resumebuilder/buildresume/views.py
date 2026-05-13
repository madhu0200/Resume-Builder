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
        personal_details=PersonalDetails.objects.filter(user=current_user)
        education_details=EductaionDetails.objects.filter(user=current_user)
        return render(request,'buildresume/home.html',{'personal_details':personal_details,'education_details':education_details})
    


@login_required
def personal_details(request):
    print(request.method)
    if request.method == 'POST':
        current_user = request.user

        fullName = request.POST['full_name']
        location = request.POST['location']
        mobile = request.POST['mobile']
        email = request.POST['email']
        github = request.POST['github']
        professionSummary = request.POST['summary']
        linkedin = request.POST['linkedin']

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            messages.error(request, "Invalid email format")
            return redirect('home')

        personal_details, created = PersonalDetails.objects.update_or_create(
            user=current_user,
            defaults={
                "FullName": fullName,
                "Location": location,
                "mobile": mobile,
                "email": email,
                "gitLink": github,
                "linkedIn": linkedin,
                "professionSummary": professionSummary,
            }
        )

        if personal_details:
            messages.success(request, "Personal details saved successfully")

        return redirect('home')

    

@login_required
def education_details(request):
    if request.method == 'POST':
        current_user = request.user

        courses = request.POST.getlist('course')
        edu_froms = request.POST.getlist('edu_from')
        edu_tos = request.POST.getlist('edu_to')
        colleges = request.POST.getlist('college')
        cgpas = request.POST.getlist('cgpa')

        errors = []
        for i in range(len(courses)):
            course = courses[i].strip()
            edu_from = edu_froms[i].strip()
            edu_to = edu_tos[i].strip()
            college = colleges[i].strip()
            cgpa = cgpas[i].strip()

            # ✅ Validation
            if not course or not college:
                errors.append(f"Record {i+1}: Course and College are required.")
                continue
            if edu_from and edu_to and edu_from > edu_to:
                errors.append(f"Record {i+1}: 'From' date cannot be after 'To' date.")
                continue

            # ✅ Save record
            EductaionDetails.objects.update_or_create(
                user=current_user,
                course=course,
                college=college,
                defaults={
                    'edu_from': edu_from,
                    'edu_to': edu_to,
                    'cgpa': cgpa,
                }
            )

        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            messages.success(request, "Education details updated successfully")

        return redirect('home')

   
        
   
