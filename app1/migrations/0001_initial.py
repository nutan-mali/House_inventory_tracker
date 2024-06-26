# Generated by Django 4.2 on 2024-04-18 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_rooms', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('equipment_name', models.CharField(max_length=100)),
                ('purchase_date', models.DateField(default=django.utils.timezone.now)),
                ('maintenance_schedule', models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly'), ('weekly', 'Weekly')], max_length=10)),
                ('maintenance_date', models.DateField()),
                ('discard_date', models.DateField()),
                ('insurance_policy_number', models.CharField(max_length=100)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='app1.house')),
            ],
        ),
    ]
