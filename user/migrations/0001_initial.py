# Generated by Django 4.0.1 on 2022-02-15 09:00

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, default=5.0, max_digits=2)),
                ('devices_assigned', models.CharField(max_length=1000, null=True)),
                ('device_image', models.ImageField(default='no_device.png', upload_to='device_images')),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('staff', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
