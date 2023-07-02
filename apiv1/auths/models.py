from django.db import models

# Create your models here.


class Captcha(models.Model):
  
  account = models.CharField(
    max_length=128,
  )
  captcha = models.CharField(
    max_length=6,
  )