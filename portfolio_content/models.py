from django.db import models

# Create your models here.

class Project(models.Model):
    """The Project class can be used to create database entries with django's ORM. it will be used to store information for the projects web page where vistors to the site can learn all about the personal and professional project work I have done"""
    title = models.CharField(max_length=100)
    personal_or_professional = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    description = models.TextField()
    technology_used = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")