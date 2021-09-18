from django.db import models

# Create your models here.

class Domain(models.Model):
	name = models.CharField(max_length=200, null=True,verbose_name="نام دامنه")
	price=models.IntegerField(max_length=50,verbose_name="قیمت",null=True)
