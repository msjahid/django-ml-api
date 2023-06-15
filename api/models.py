from django.db import models


class Salary(models.Model):
    YearsExperience = models.FloatField()
    salary = models.FloatField()