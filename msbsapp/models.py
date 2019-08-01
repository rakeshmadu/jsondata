from django.db import models
class Data(models.Model):
    owner_id = models.CharField(max_length = 50)
    camapaign = models.CharField(max_length = 50)
    campaign_id =models.CharField(max_length = 6000)
