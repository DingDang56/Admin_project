from django.db import models

class Admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Subject(models.Model):
    name =models.CharField(max_length=32)
    date = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    grade = models.CharField(max_length=32)
    delete_flag=models.CharField(max_length=32,default="false")
    photo = models.ImageField(upload_to="img",default="img/web-3219281_640.jpg")
    subject = models.ManyToManyField(Subject)


class Score(models.Model):
    subject = models.CharField(max_length=32)
    subject_id = models.IntegerField()
    score = models.FloatField()
    student = models.CharField(max_length=32)
    student_id = models.IntegerField()

# Create your models here.
