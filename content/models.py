from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile')
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    Git_Hub = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='flash')

    def __str__(self):
        return self.user.username

class Education(models.Model):
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    university = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Skills(models.Model):
    skill = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

class Experience(models.Model):
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='default company')
    project = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job


