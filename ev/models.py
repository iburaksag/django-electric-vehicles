from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MaxValueValidator

class EV(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    battery_size = models.IntegerField()
    wltp_range = models.IntegerField()
    cost = models.IntegerField()
    power = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        return self.evreview_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.name


class EVReview(models.Model):
    ev = models.ForeignKey(EV, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=100, blank=True, null=True)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.ev}"

    