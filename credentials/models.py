from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    mobile = models.CharField(max_length=120,blank=True,null=True)
    
    def __str__(self):
        return self.user.username



class idClone(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return '{} - {}'.format(self.email)

 





