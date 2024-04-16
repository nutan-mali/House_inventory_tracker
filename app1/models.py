from django.db import models
from django.utils import timezone

class House(models.Model):
    name = models.CharField(max_length=100)

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    equipment_name = models.CharField(max_length=100)
    purchase_date = models.DateField(default=timezone.now)
    maintenance_schedule = models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly'), ('weekly', 'Weekly')], max_length=10)
    maintenance_date = models.DateField()
    discard_date = models.DateField()
    insurance_policy_number = models.CharField(max_length=100)