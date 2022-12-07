from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField( max_length=50)
    date =models.DateTimeField()
    content = models.CharField( max_length=5000)
    


