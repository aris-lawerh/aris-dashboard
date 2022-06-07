# Generated by Django 4.0.1 on 2022-02-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_device_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='assignment_reason',
            field=models.CharField(choices=[(1, 'Loaner'), (2, 'Regular'), (3, 'Short Term'), (4, 'Long Term'), (5, 'Other')], default='Loaner', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date_assigned',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date_returned',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='known_issues',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='last_maintained',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='license_expiry',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='machine_condition',
            field=models.CharField(choices=[(1, 'Excellent'), (2, 'Good'), (3, 'Broken'), (4, 'Dented'), (5, 'Ugly'), (6, 'Missing Accessory'), (7, 'Other')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='purchase_date',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='antivirus_license',
            field=models.CharField(choices=[(1, 'Expired'), (2, 'Active')], default='N/A', max_length=1000),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='cover_inspection',
            field=models.CharField(choices=[(1, 'Done'), (2, 'Not Done')], default='Not Done', max_length=1000),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='device_condition',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Network Device', 'Network Device'), ('Router', 'Router'), ('TV', 'TV'), ('Misc', 'Misc'), ('Printer', 'Printer'), ('Desktop', 'Desktop'), ('Tablet', 'Tablet'), ('Intercom', 'Intercom'), ('Accessories', 'Accessories'), ('Hard Cover', 'Hard Cover'), ('Bags', 'Bags'), ('Camera', 'Camera')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='dust_inspection',
            field=models.CharField(choices=[(1, 'Done'), (2, 'Not Done')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='system_license',
            field=models.CharField(choices=[(1, 'Expired'), (2, 'Active')], default='N/A', max_length=1000),
        ),
    ]
