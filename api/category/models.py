from django.db import models

# Create your models here.

class Category(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name



