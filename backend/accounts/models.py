from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAccount(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username
    

class SectionOffice(models.Model):
    user=models.OneToOneField(UserAccount,on_delete=models.CASCADE,related_name='office_account')
    office_id=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    address=models.TextField(null=True,blank=True)

class Public(models.Model):
    user=models.OneToOneField(UserAccount,on_delete=models.CASCADE,related_name='public_account')
    profile_pic=models.ImageField(upload_to='profile_pic',null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    consumer_id=models.CharField(max_length=40,null=True,blank=True)
    section_office=models.ForeignKey(SectionOffice,on_delete=models.CASCADE,null=True,blank=True,related_name='public_office')
    created_at=models.DateTimeField(auto_now_add=True)

class LineWorker(models.Model):
    user=models.OneToOneField(UserAccount,on_delete=models.CASCADE,related_name='worker_account')
    worker_id=models.IntegerField(null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    office=models.ForeignKey(SectionOffice,on_delete=models.CASCADE,null=True,blank=True,related_name='my_office')
    address=models.TextField(null=True)