from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PersonalDetails)
admin.site.register(EductaionDetails)
admin.site.register(SkillsDetails)
admin.site.register([ProfessionDetails,ProjectDetails])
