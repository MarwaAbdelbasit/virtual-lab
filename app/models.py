from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
    )

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, full_name, email, university, faculty, date_of_birth=None, password=None, is_active=True, is_staff=False, is_admin=False):
        # takes whats in the REQUIRED_FIELDS arguments
        if not email:
            raise ValueError("user must have an email")
        if not password:
            raise ValueError("user must have a password")
        if not full_name:
            raise ValueError("user must have a full name")
        if not university:
            raise ValueError("user must have a university")
        if not faculty:
            raise ValueError("user must have a faculty")

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            university = university,
            faculty = faculty,
        )
        user_obj.set_password(password) # change user password
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, full_name, email, university, faculty, date_of_birth=None, password=None):
        user = self.create_user(
            email,
            full_name,
            university,
            faculty,
            date_of_birth = date_of_birth,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, full_name, email, university, faculty, date_of_birth=None, password=None):
        user = self.create_user(
            email,
            full_name,
            university,
            faculty,
            date_of_birth = date_of_birth,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=30)
    faculty = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name="date of birth", auto_now=False, auto_now_add=False)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) # can login
    staff = models.BooleanField(default=False) # staff user non superuser
    admin = models.BooleanField(default=False) # superuser

    USERNAME_FIELD = 'email' # username
    REQUIRED_FIELDS = ['full_name', 'university', 'faculty'] # python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_university(self):
        return self.university

    def get_faculty(self):
        return self.faculty

    def get_date_of_birth(self):
        if self.date_of_birth:
            return self.date_of_birth
        return self.email

    def short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


# class Accounts(models.Model):
#     email = models.EmailField(verbose_name="user e-mail", max_length=255, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     phone = models.DecimalField(max_digits=11, decimal_places=0)
#     university = models.CharField(max_length=30)
#     faculty = models.CharField(max_length=100)
#     date_of_birth = models.DateField(verbose_name="date of birth", auto_now=False, auto_now_add=False)
#     country = models.CharField(max_length=30)
#     password = models.CharField(max_length=100, null=False)
#
#     STUDENT = 'student'
#     INSTITUTE = 'institute'
#     types = [
#         (STUDENT, 'Student'),
#         (INSTITUTE, 'Institute'),
#     ]
#     user_type = models.CharField(max_length=10, choices=types, default=STUDENT)
#
#     def is_upperclass(self):
#         return self.type in {self.STUDENT, self.INSTITUTE}
#
#     def __str__(self):
#         return self.username


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
