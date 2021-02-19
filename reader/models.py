from django.db import models

# Create your models here.
class Reader(models.Model):
    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('Other','Other'),
    ]
    name = models.CharField(max_length = 25)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10,choices = GENDER,default='M')
    book_name = models.CharField(max_length = 25)
    author = models.CharField(max_length = 25)
    phone_number = models.CharField(max_length = 10)
    ask_book = models.CharField(max_length = 25)
    image = models.ImageField()

