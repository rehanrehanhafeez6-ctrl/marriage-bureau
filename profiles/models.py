from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    pref_min_age = models.PositiveIntegerField(default=18)
    pref_max_age = models.PositiveIntegerField(default=40)
    pref_city = models.CharField(max_length=50, blank=True)
    pref_education = models.CharField(max_length=100, blank=True)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def age(self):
        today = date.today()
        born = self.date_of_birth
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return self.full_name