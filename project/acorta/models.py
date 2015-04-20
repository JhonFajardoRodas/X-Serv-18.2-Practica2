from django.db import models

# Create your models here.


class urlDB (models.Model):

	url = models.CharField(max_length=100)
	urlCut = models.IntegerField()

