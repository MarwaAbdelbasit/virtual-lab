from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Accounts(models.Model):
    email = models.EmailField(verbose_name="user e-mail", max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.DecimalField(max_digits=11, decimal_places=0)
    university = models.CharField(max_length=30)
    faculty = models.CharField(max_length=100)
    date_of_birth = models.DateField(verbose_name="date of birth", auto_now=False, auto_now_add=False)
    country = models.CharField(max_length=30)
    password = models.CharField(max_length=100, null=False)

    STUDENT = 'student'
    INSTITUTE = 'institute'
    types = [
        (STUDENT, 'Student'),
        (INSTITUTE, 'Institute'),
    ]
    user_type = models.CharField(max_length=10, choices=types, default=STUDENT)

    def is_upperclass(self):
        return self.type in {self.STUDENT, self.INSTITUTE}

    def __str__(self):
        return self.username


# devices model
class Devices(models.Model):
    name = models.CharField(max_length=100)
    device_id = models.CharField(primary_key=True, max_length=10)
    # true = device is free / false = device is in-use
    status = models.BooleanField(default=True)
    description = models.TextField()
    rate = models.IntegerField()
    review = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(default='device_default.png', blank=True, max_length=100)


    def __str__(self):
        return self.name

# Experiments model
class Experiments(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    experiment_id = models.IntegerField(primary_key=True)
    device_name = models.ForeignKey(Devices, on_delete=models.PROTECT)
    # user_id = models.ForeignKey(Users, on_delete=RESTRICT)
    duration = models.DurationField()

    def __str__(self):
        return self.title
