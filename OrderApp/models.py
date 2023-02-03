from django.db import models

# Create your models here.
class Table(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null = False,blank=False)
    email = models.CharField(max_length=100,null = False,unique=True,blank=False)
    phone = models.CharField(max_length=20,null = False,blank=False)
    contact = models.CharField(max_length=255,null = False,blank=False)
    # order =
    def __str__(self):
        return self.name