# Generated by Django 4.0.1 on 2022-02-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_device_license_expiry_device_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial_no',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
