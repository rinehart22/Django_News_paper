from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# but if we just want a custom user model
#that can be updated with additional fields, the better choice is AbstractUser which
#subclasses AbstractBaseUser

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null=True, blank=True)