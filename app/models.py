from django.db import models

# Create your models here.

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
