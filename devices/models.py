from django.db import models

# Create your models here.
class Device(models.Model):
    serial_number=models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=20,unique=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}({self.serial_number})"


    
    

