from django.db import models
from houses.models import house
from accounts.models import CustomUser


# Create your models here.
class order(models.Model):
    house = models.ForeignKey(house,on_delete=models.CASCADE,default=None)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    client = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"{self.house}"


class favorite(models.Model):
    house = models.ForeignKey(house,on_delete=models.CASCADE,default=None)
    client = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"{self.client}"