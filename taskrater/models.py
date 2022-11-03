from django.db import models

# Create your models here.
class RateData(models.Model):
    task = models.CharField(max_length = 60, blank=True, null=True)
    query= models.CharField(max_length = 100)
    rate=models.SmallIntegerField()
    job_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
