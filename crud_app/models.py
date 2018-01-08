from django.db import models
from django.core.urlresolvers import reverse


class Student(models.Model):
    Surname = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Level = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField()
    Phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.Surname + ' ' + self.Firstname

    def get_absolute_url(self):
        return reverse("all_list", kwargs={"id": self.id})
