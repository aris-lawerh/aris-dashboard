# Generated by Django 4.0.1 on 2022-02-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_device_serial_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='assigned_to',
            field=models.CharField(default='Not Assigned', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='assignment_reason',
            field=models.CharField(choices=[(1, 'Loaner'), (2, 'Regular'), (3, 'Short Term'), (4, 'Long Term'), (5, 'Other')], default='Loaner', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date_assigned',
            field=models.CharField(default='N/A', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date_returned',
            field=models.CharField(default='N/A', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_location',
            field=models.CharField(default='N/A', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_name',
            field=models.CharField(default='N/A', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='known_issues',
            field=models.CharField(default='N/A', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='last_maintained',
            field=models.CharField(default='N/A', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='license_expiry',
            field=models.CharField(default='N/A', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='maintained_by',
            field=models.CharField(default='N/A', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='order_number',
            field=models.CharField(default='N/A', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='purchase_date',
            field=models.CharField(default='N/A', max_length=20, null=True),
        ),
    ]