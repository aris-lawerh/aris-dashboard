# Generated by Django 4.0.1 on 2022-02-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_device_date_assigned_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_location',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]