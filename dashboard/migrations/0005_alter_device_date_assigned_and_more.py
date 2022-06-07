# Generated by Django 4.0.1 on 2022-02-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='date_assigned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date_returned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='last_maintained',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]