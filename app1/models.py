from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class House(models.Model):
    name = models.CharField(max_length=100)
    num_rooms = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='rooms')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    equipment_name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    maintenance_schedule = models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly'), ('weekly', 'Weekly')], max_length=10)
    maintenance_date = models.DateField()
    discard_date = models.DateField()
    insurance_policy_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name
