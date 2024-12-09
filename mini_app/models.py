from django.db import models


# Create your models here.

class conversion(models.Model):
    text=models.CharField(max_length=300)
    number=models.IntegerField()


    def __str__(self):
        return f"{self.text} → {self.number}"
    
# class Conversion(models.Model):
#     text=models.CharField(max_length=300)
#     number=models.IntegerField()
#     def __str__(self):
#         return f"{self.text} → {self.number}"


class Convert(models.Model):
    text_input=models.CharField(max_length=250)
    number_result=models.IntegerField()
    
    def __str__(self):
        return f"{self.text_input} → {self.number_result}"
    

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.username
