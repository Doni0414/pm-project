from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import User

admin.site.register(User)
# admin.site.register(Hospital_Information)
# admin.site.register(Patient)

