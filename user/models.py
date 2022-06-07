from django.db import models
from django.contrib.auth.models import User
import PIL
# Create your models here.

POSITIONS = [
    ('Primary Staff', 'Primary Staff'),
    ('Secondary Staff', 'Secondary Staff'),
    ('Auxiliary Staff', 'Auxiliary Staff'),
    ]

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    rating = models.DecimalField(default=5.0, decimal_places=1, max_digits=2)
    position = models.CharField(max_length=100, choices=POSITIONS, null=True)
    devices_assigned = models.CharField(max_length=1000, null=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.staff.username} - Profile'