from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    ism=models.CharField(max_length=200)
    familiya=models.CharField(max_length=200)
    jami_yozilgan_kitoblar_soni=models.CharField(max_length=200)
    millati=models.CharField(max_length=200)
    yoshi=models.IntegerField(default=0,blank=True,null=True)
    yatilgan_vaqt=models.DateTimeField(auto_now_add=True)
    ozgargan_vaqt=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ism
    
    
    

    
class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    varoqlar_soni=models.IntegerField()
    class MuqovaTuri(models.TextChoices):
        qattiq='qattiq','Qattiq muqova'
        yumshoq='yumshoq','Yumshoq muqova'
        
    jild=models.CharField(max_length=200,choices=MuqovaTuri.choices)
    rasm=models.ImageField(upload_to='media/',blank=True,null=True)
    omborda_mavjud=models.BooleanField(default=0)
    yaratilgan_vaqt=models.DateTimeField(auto_now_add=True)
    ozgartirilgan_vaqt=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Store(models.Model):
    name=models.CharField(max_length=200)
    manzil=models.CharField(max_length=200)
    sotiladigan_kitoblar=models.ManyToManyField(Book)
    sotuvchi=models.ForeignKey(User,on_delete=models.CASCADE)
    jami_sotilgan_kitoblar_soni=models.IntegerField(default=0)
    yaratilgan_vaqt=models.DateTimeField(default=timezone.now,blank=True,null=True)
    ozgartirilgan_vaqt=models.DateTimeField(timezone.now,blank=True,null=True)
    
    def __str__(self):
        return self.name
        
