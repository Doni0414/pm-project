from django.db import models

import hospital
from hospital.models import User


# Create your models here.

class Admin_Information(models.Model):
    ADMIN_TYPE = (
        ('hospital', 'hospital'),
        ('laboratory', 'laboratory'),
        ('pharmacy', 'pharmacy'),
    )

    admin_id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='hospital_admin')
    username = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(upload_to='admin/', default='admin/user-default.png', null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, choices=ADMIN_TYPE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)