from django.db import models
from accounts.models import CustomUser

# Create your models here.
class house(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    images= models.ImageField(upload_to='img')
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return self.name