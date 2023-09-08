from django.db import models
from django.contrib.auth.models import User

class kharj(models.Model):
   text = models.CharField(max_length=255)
   date = models.DateTimeField()
   adad = models.BigIntegerField()
   user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)
   def __str__(self):
     return f"{self.text} {self.adad}"
class dakhl(models.Model):
   text = models.CharField(max_length=255)
   date = models.DateTimeField()
   adad = models.BigIntegerField()
   user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)   
   def __str__(self):
      return f"{self.text} {self.adad}"
