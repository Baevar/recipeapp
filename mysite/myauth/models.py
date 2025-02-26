from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name="Пользователь")
    bio = models.CharField(max_length=50, blank=True, verbose_name="Имя")