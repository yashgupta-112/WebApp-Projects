from django.db import models

# Create your models here.
class contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def __str__(self):
        return 'Message from'+''+ self.name+''+self.email

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    image =models.ImageField(upload_to="gym/images",default="")
    sname = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    contents = models.CharField(max_length=500)

class Ninja(models.Model):
    email= models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    ages = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    habit = models.CharField(max_length=100)
    message = models.CharField(max_length=800)