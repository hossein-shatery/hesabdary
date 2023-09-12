from django.db import models
from django.contrib.auth.models import User

class kharj(models.Model):
   text = models.CharField(max_length=255)
   date = models.DateTimeField()
   adad = models.BigIntegerField()
   user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)
   def __str__(self):
     return f"{self.text} {self.adad}"
     
class token(models.Model):
   user = models.OneToOneField(User , on_delete=models.CASCADE, primary_key=True,)
   token = models.CharField(max_length=25)
   def __str__(self):
     return f"{self.user}"
    
class dakhl(models.Model):
   text = models.CharField(max_length=255)
   date = models.DateTimeField()
   adad = models.BigIntegerField()
   user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)   
   def __str__(self):
      return f"{self.text} {self.adad}"
