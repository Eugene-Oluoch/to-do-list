from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created','-updated']
        
        
    def __str__(self):
        return self.name