from django.contrib import admin
from oshpaz import models  
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Achievement)
admin.site.register(models.Profession)
admin.site.register(models.Certificate)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Scientist)
admin.site.register(models.HealthyLife)
admin.site.register(models.PersonalPrescription)
admin.site.register(models.Myerrors)
admin.site.register(models.Announcement)