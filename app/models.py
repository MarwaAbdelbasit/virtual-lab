from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
    )
from django.conf import settings

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, full_name, email, university, type, faculty, date_of_birth=None, password=None, is_active=True, is_staff=False, is_admin=False):
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
        if not type:
            raise ValueError("user must provide whether he is a student or an institute")

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            university = university,
            faculty = faculty,
            type = type,
        )
        user_obj.set_password(password) # change user password
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, full_name, email, university, faculty, type, date_of_birth=None, password=None):
        user = self.create_user(
            email,
            full_name,
            university,
            faculty,
            type,
            date_of_birth = date_of_birth,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, full_name, email, university, faculty, type, date_of_birth=None, password=None):
        user = self.create_user(
            email,
            full_name,
            university,
            faculty,
            type,
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
    date_of_birth = models.DateField(verbose_name="date of birth", auto_now=False, auto_now_add=False, null=True)
    STUDENT = 'S'
    INSTITUTE = 'I'
    ADMIN = 'A'
    user_types = [
        (STUDENT, 'Student'),
        (INSTITUTE, 'Institute'),
        (ADMIN, 'Admin'),
    ]
    type = models.CharField(max_length=1, choices=user_types, default=STUDENT, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) # can login
    staff = models.BooleanField(default=False) # staff user non superuser
    admin = models.BooleanField(default=False) # superuser

    USERNAME_FIELD = 'email' # username
    REQUIRED_FIELDS = ['full_name', 'university', 'faculty', 'type'] # python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_university(self):
        return self.university

    def get_faculty(self):
        return self.faculty

    def get_type(self):
        return self.type

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

    def is_student(self):
        if self.type == 'S':
            return True
        else:
            return False

    def is_institute(self):
        if self.type == 'I':
            return True
        else:
            return False


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



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
    device_name = models.ForeignKey(Devices, on_delete=models.CASCADE)
    user_exp = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)
    duration = models.DurationField()

    def __str__(self):
        return self.title


# Reservation model
class Reservation(models.Model):
     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=True)
     Device=models.OneToOneField(Devices,on_delete=models.CASCADE,default=True)
     Start_time = models.DateTimeField()
     Finish_time = models.DateTimeField()

     def __str__(self):
        return f'{self.user} has booked {self.Device}from {self.Start_time} to {self.Finish_time}'

# FAQ model
class FAQ(models.Model):
    question_id = models.IntegerField(primary_key=True)
    Question = models.CharField(max_length=100)
    Answer = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.Answer} for {self.Question}'



# plans model
class Plan(models.Model):
    STANDARD = 'S'
    PLUS = 'P'
    PREMIUM = 'M'
    names = [
        (STANDARD, 'Standard'),
        (PLUS, 'Plus'),
        (PREMIUM, 'Premium'),
    ]
    plan_name = models.CharField(max_length=1, choices=names, default=STANDARD)
    price = models.CharField(max_length=100)
    feauters_of_plan = models.TextField()
    number_of_coupons = models.IntegerField()

    def __str__(self):
        return self.plan_name

    def get_number_of_coupons(self):
        return self.number_of_coupons


# coupons model
class Coupon(models.Model):
    code = models.CharField(primary_key=True, max_length=50, unique=True)
    active = models.BooleanField()

    def __str__(self):
        return self.code


# order model
class Purchase(models.Model):
    plan_name = models.ForeignKey(Plan, on_delete=models.CASCADE)
    payment_option = models.CharField(max_length=50)
    institute=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=True)

    def __str__(self):
        return f'{self.institute} purchased {self.plan_name}'

    def get_plan_name(self):
        return self.plan_name
