# Generated by Django 4.0.1 on 2022-02-08 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Network Device', 'Network Device'), ('Router', 'Router'), ('TV', 'TV'), ('Misc', 'Misc'), ('Printer', 'Printer'), ('Desktop', 'Desktop'), ('Tablet', 'Tablet'), ('Intercom', 'Intercom'), ('Accessories', 'Accessories'), ('Hard Cover', 'Hard Cover'), ('Bags', 'Bags'), ('Camera', 'Camera')], max_length=100, null=True)),
                ('device_name', models.CharField(default='N/A', max_length=1000)),
                ('serial_no', models.CharField(max_length=100, null=True, unique=True)),
                ('purchase_date', models.DateField(auto_now=True)),
                ('last_maintained', models.DateField(auto_now=True)),
                ('maintained_by', models.CharField(default='N/A', max_length=50)),
                ('known_issues', models.CharField(default='N/A', max_length=20)),
                ('assigned_to', models.CharField(default='Not Assigned', max_length=50)),
                ('assigned_by', models.CharField(choices=[(1, 'Lawerh Caesar'), (2, 'Gabriel Muhammad'), (3, 'Anthony Kwawu'), (4, 'Symplice Athodjinou'), (5, 'Christopher Hanson'), (6, 'Nausheen Siddiqi')], default='Not Assigned', max_length=50, null=True)),
                ('date_assigned', models.DateField(auto_now=True)),
                ('date_returned', models.DateField(auto_now=True)),
                ('machine_condition', models.CharField(choices=[(1, 'Excellent'), (2, 'Good'), (3, 'Broken'), (4, 'Dented'), (5, 'Ugly'), (6, 'Missing Accessory'), (7, 'Other')], max_length=20, null=True)),
                ('assignment_reason', models.CharField(choices=[(1, 'Loaner'), (2, 'Regular'), (3, 'Short Term'), (4, 'Long Term'), (5, 'Other')], default='Loaner', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.device')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
