"""Models for database."""
from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    manager = models.ForeignKey('self', null=True, blank=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name
