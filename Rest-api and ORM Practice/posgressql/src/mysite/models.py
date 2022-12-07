from django.db import models

# Create your models here.
class saiyan(models.Model):
    fname = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    
    def __str__(self):
        return self.fname