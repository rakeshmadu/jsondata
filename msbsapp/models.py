from django.db import models

# Create your models here.
class Data(models.Model):
    owner_id = models.CharField(max_length = 50)
    camapaign = models.CharField(max_length = 50)
    campaign_id =models.CharField(max_length = 6000)
