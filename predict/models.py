from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    name = models.CharField(max_length=50)
    age = models. IntegerField()
    gender = models.CharField(max_length=30)
    height = models. IntegerField()
    weight = models. IntegerField()
    symptom1 = models.CharField(max_length=30)
    symptom2 = models.CharField(max_length=30, blank=True)
    symptom3 = models.CharField(max_length=30, blank=True)
    symptom4 = models.CharField(max_length=30, blank=True)
    symptom5 = models.CharField(max_length=30, blank=True)
    disease = models.CharField(max_length=30)
    consultDoctor = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class database(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    precaution = models.TextField(max_length=5000)
    symptom = models.TextField(max_length=5000)

    def __str__(self):
        return self.disease

class doc_DB(models.Model):
    id = models.AutoField(primary_key=True)
    Doctor = models.CharField(max_length=250)
    Type = models.CharField(max_length=250)
    Pincode = models.CharField(max_length=250)
    Location =models.TextField(max_length=5000)

    def __str__(self):
        return self.Doctor