from django.contrib import admin
from oshpaz.models import  User,Certificate,Achievement,Profession
# Register your models here.

admin.site.register(User)
admin.site.register(Achievement)
admin.site.register(Profession)
admin.site.register(Certificate)