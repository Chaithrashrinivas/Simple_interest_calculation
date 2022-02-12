from django.db import models

# Create your models here.

class User(models.Model):
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    principal = models.CharField(max_length=100)
    interest = models.CharField(max_length=50)

    def __str__(self):
        return self.interest


