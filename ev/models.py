from django.db import models


class EV(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    battery_size = models.IntegerField()
    wltp_range = models.IntegerField()
    cost = models.IntegerField()
    power = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

    