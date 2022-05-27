from random import choices
from turtle import title
from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length = 50)
    description= models.TextField()
    
    PRIORITY = (
    ('1', 'High'),
    ('2', 'Medium'),
    ('3', 'Low'),
    )
    
    priority=models.CharField(max_length = 10,choices=PRIORITY)
    isCompleted=models.BooleanField()
    
    updated_date=models.DateTimeField(auto_now=True,)
    created_date =models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return self.title
        