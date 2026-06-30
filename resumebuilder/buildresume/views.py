from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from .models import *
from django.template.loader import get_template
import pdfkit
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)


# Create your views here.
@login_required
def home(request):
    if request.method=='GET':
        current_user=request.user
        personal_details=PersonalDetails.objects.filter(user=current_user).first()
        education_details=EductaionDetails.objects.filter(user=current_user)
        skills_details=SkillsDetails.objects.filter(user=current_user)
        profession_details=ProfessionDetails.objects.filter(user=current_user)
        project_details=ProjectDetails.objects.filter(user=current_user)

        return render(request,'buildresume/home.html',{'personal_details':personal_details,
                                                       'education_details':education_details,
                                                       'skills_details':skills_details,
                                                       'professional_details':profession_details,
                                                       'project_details':project_details})
    


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
        user = request.user

        # Collect lists of values from the form
        courses = request.POST.getlist('course')
        colleges = request.POST.getlist('college')
        edu_froms = request.POST.getlist('edu_from')
        edu_tos = request.POST.getlist('edu_to')
        cgpas = request.POST.getlist('cgpa')

        # Existing records in DB
        existing_records = list(EductaionDetails.objects.filter(user=user))

        # Case 1 & 2: Update existing records up to the number of UI entries
        for i in range(min(len(existing_records), len(courses))):
            record = existing_records[i]
            record.course = courses[i]
            record.college = colleges[i]
            record.edu_from = edu_froms[i]
            record.edu_to = edu_tos[i]
            record.cgpa = cgpas[i]
            record.save()

        # Case 3: If UI has more, create new records
        if len(courses) > len(existing_records):
            for i in range(len(existing_records), len(courses)):
                EductaionDetails.objects.create(
                    user=user,
                    course=courses[i],
                    college=colleges[i],
                    edu_from=edu_froms[i],
                    edu_to=edu_tos[i],
                    cgpa=cgpas[i]
                )

        # Case 1: If DB has more, delete extras
        elif len(existing_records) > len(courses):
            for i in range(len(courses), len(existing_records)):
                existing_records[i].delete()

        messages.success(request, "Education details updated successfully")
        return redirect('home')
    


@login_required
def skills_details(request):
    if request.method == 'POST':
        user = request.user

        # Collect lists of values from the form
        keys = request.POST.getlist('key')
        values = request.POST.getlist('value')

        # Existing records in DB
        existing_records = list(SkillsDetails.objects.filter(user=user))

        # Case 1 & 2: Update existing records up to the number of UI entries
        for i in range(min(len(existing_records), len(keys))):
            record = existing_records[i]
            record.key = keys[i]
            record.value = values[i]
            record.save()

        # Case 3: If UI has more, create new records
        if len(keys) > len(existing_records):
            for i in range(len(existing_records), len(keys)):
                SkillsDetails.objects.create(
                    user=user,
                    key=keys[i],
                    value=values[i],
                )

        # Case 1: If DB has more, delete extras
        elif len(existing_records) > len(keys):
            for i in range(len(keys), len(existing_records)):
                existing_records[i].delete()

        messages.success(request, "skills details updated successfully")
        return redirect('home')
    

@login_required
def professional_details(request):
    if request.method == 'POST':
        user = request.user

        # Collect lists of values from the form
        companies = request.POST.getlist('company')
        exp_froms = request.POST.getlist('exp_from')
        exp_tos = request.POST.getlist('exp_to')
        locations = request.POST.getlist('company_location')
        descriptions = request.POST.getlist('experience_description')
        print(companies,exp_froms,exp_tos,locations,descriptions)
        # Existing records in DB
        existing_records = list(ProfessionDetails.objects.filter(user=user))

        # Case 1 & 2: Update existing records up to the number of UI entries
        for i in range(min(len(existing_records), len(companies))):
            record = existing_records[i]
            record.company = companies[i]
            record.exp_from = exp_froms[i]
            record.exp_to = exp_tos[i]
            record.location = locations[i]
            record.description = descriptions[i]
            record.save()

        # Case 3: If UI has more, create new records
        if len(companies) > len(existing_records):
            for i in range(len(existing_records), len(companies)):
                ProfessionDetails.objects.create(
                    user=user,
                    company=companies[i],
                    exp_from=exp_froms[i],
                    exp_to=exp_tos[i],
                    location=locations[i],
                    description=descriptions[i]
                )

        # Case 1: If DB has more, delete extras
        elif len(existing_records) > len(companies):
            for i in range(len(companies), len(existing_records)):
                existing_records[i].delete()

        messages.success(request, "Professional details updated successfully")
        return redirect('home')
    
@login_required
def project_details(request):
    if request.method == 'POST':
        user = request.user

        # Collect lists of values from the form
        names = request.POST.getlist('project_name')
        descriptions = request.POST.getlist('project_description')

        # Existing records in DB
        existing_records = list(ProjectDetails.objects.filter(user=user))

        # Case 1 & 2: Update existing records up to the number of UI entries
        for i in range(min(len(existing_records), len(names))):
            record = existing_records[i]
            record.name = names[i]
            record.description = descriptions[i]
            record.save()

        # Case 3: If UI has more, create new records
        if len(names) > len(existing_records):
            for i in range(len(existing_records), len(names)):
                ProjectDetails.objects.create(
                    user=user,
                    name=names[i],
                    description=descriptions[i],
                )

        # Case 1: If DB has more, delete extras
        elif len(existing_records) > len(names):
            for i in range(len(names), len(existing_records)):
                existing_records[i].delete()

        messages.success(request, "projects details updated successfully")
        return redirect('home')
    

@login_required
def resume_showcase(request):
    if request.method=='GET':
        
        image_urls=os.listdir(os.path.join(BASE_DIR,"static","images"))
        return render(request,'buildresume/ResumeShowCase.html',{'image_links':image_urls})
    
@login_required
def buildresume(request,template_id):
    current_user=request.user
    if request.method=='GET':
        personal_details=PersonalDetails.objects.filter(user=current_user).first()
        education_details=EductaionDetails.objects.filter(user=current_user)
        skills_details=SkillsDetails.objects.filter(user=current_user)
        for skills in skills_details:
            skills.value=skills.value.split(',')

        
        profession_details=ProfessionDetails.objects.filter(user=current_user)

        for experience in profession_details:
            experience.description=[desc.strip() for desc in experience.description.split('_') if desc!='']
            
            print(experience.description)
        project_details=ProjectDetails.objects.filter(user=current_user)

        for project in project_details:
            project.description=[desc.strip() for desc in project.description.split('_') if desc!='']
            
            print(project.description)

        return render(request,f'buildresume/ResumeTemplate{template_id}.html',{'personal_details':personal_details,
                                                       'education_details':education_details,
                                                       'skills_details':skills_details,
                                                       'professional_details':profession_details,
                                                       'project_details':project_details})
@login_required
def download_resume(request,template_id):
    current_user=request.user
    if request.method=='GET':
        try:
            personal_details=PersonalDetails.objects.filter(user=current_user).first()
            education_details=EductaionDetails.objects.filter(user=current_user)
            skills_details=SkillsDetails.objects.filter(user=current_user)
            for skills in skills_details:
                skills.value=skills.value.split(',')

            
            profession_details=ProfessionDetails.objects.filter(user=current_user)

            for experience in profession_details:
                experience.description=[desc.strip() for desc in experience.description.split('_') if desc!='']
                
               
            project_details=ProjectDetails.objects.filter(user=current_user)

            for project in project_details:
                project.description=[desc.strip() for desc in project.description.split('_') if desc!='']
                
                

        

            template = get_template(f'buildresume/ResumeTemplate{template_id}.html')
            html = template.render({
                'personal_details': personal_details,
                'education_details': education_details,
                'skills_details': skills_details,
                'professional_details': profession_details,
                'project_details': project_details,
                'hide_download': True,
            })

            path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

            css_path = os.path.join(BASE_DIR,f"static\\buildresume\\ResumeTemplate{template_id}.css")
            
            pdf = pdfkit.from_string(html, False, configuration=config, options={'enable-local-file-access': None}, css=css_path)

    


            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="resume_template_{template_id}.pdf"'
            return response

        except Exception as e:
            return HttpResponse(f"Error generating resume: {e}", content_type="text/plain")
        
    
