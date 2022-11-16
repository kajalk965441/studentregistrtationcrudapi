from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null= False)
    email = models.CharField(max_length=100, null= False)
    phone = models.CharField(max_length=100, null=False)
    subject = models.CharField(max_length=100, blank = True, null = True)
    Class =  models.CharField(max_length=100, blank = True, null = True )
    address = models.CharField(max_length=100,blank = True, null = True )
    city = models.CharField(max_length=100,blank = True, null = True )
     
    def __str__(self):
        return self.name