# Generated by Django 4.0.1 on 2022-02-10 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_assignment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_condition', models.CharField(choices=[('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Network Device', 'Network Device'), ('Router', 'Router'), ('TV', 'TV'), ('Misc', 'Misc'), ('Printer', 'Printer'), ('Desktop', 'Desktop'), ('Tablet', 'Tablet'), ('Intercom', 'Intercom'), ('Accessories', 'Accessories'), ('Hard Cover', 'Hard Cover'), ('Bags', 'Bags'), ('Camera', 'Camera')], max_length=20)),
                ('cover_inspection', models.CharField(choices=[(1, 'Done'), (2, 'Not Done')], default='Not Done', max_length=20)),
                ('dust_inspection', models.CharField(choices=[(1, 'Done'), (2, 'Not Done')], max_length=20)),
                ('antivirus_license', models.CharField(choices=[(1, 'Expired'), (2, 'Active')], default='N/A', max_length=20)),
                ('system_license', models.CharField(choices=[(1, 'Expired'), (2, 'Active')], default='N/A', max_length=20)),
                ('choose_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.device')),
            ],
        ),
    ]