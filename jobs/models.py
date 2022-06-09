from django.db import models

# Create your models here.
class Jobs(models.Model):
	title = models.CharField(max_length = 120)
	desc = models.TextField()
	timeposted = models.DateTimeField(auto_now_add=True)
