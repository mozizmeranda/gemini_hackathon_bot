from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, related_name="doctor", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    start_time_of_work = models.TimeField()
    end_time_of_work = models.TimeField()
    experience_years = models.IntegerField()
    grafik = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


# class Auth(AbstractUser):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name


