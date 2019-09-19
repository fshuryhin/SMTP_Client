from django.db import models

# Create your models here.
class MailSettings(models.Model):
    name = models.CharField(max_length = 250, primary_key = True)
    val = models.CharField(max_length = 250)
