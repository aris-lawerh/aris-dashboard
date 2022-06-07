# from sre_constants import CATEGORY_LOC_WORD
# from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User

CATEGORY = [
    ('Laptop','Laptop'),
    ('Macbook', 'Macbook'),
    ('Phone', 'Phone'),
    ('Network Device', 'Network Device'),
    ('Router','Router'),
    ('TV', 'TV'),
    ('Misc','Misc'),
    ('Printer', 'Printer'),
    ('Desktop', 'Desktop'),
    ('Tablet', 'Tablet'),
    ('Intercom','Intercom'),
    ('Accessories', 'Accessories'),
    ('Hard Cover', 'Hard Cover'),
    ('Bags', 'Bags'),
    ('AIO', 'AIO'),
    ('Camera', 'Camera'),
    ('IMAC','IMAC'),
    ('ID Card Printer', 'ID Card Printer'),
    ]
ADMINS = [
    ('Lawerh Caesar', 'Lawerh Caesar'),
    ('Gabriel Muhammad', 'Gabriel Muhammad'),
    ('Anthony Kwawu', 'Anthony Kwawu'),
    ('Symplice Athodjinou', 'Symplice Athodjinou'),
    ('Christopher Hanson', 'Christopher Hanson'),
    ('Nausheen Siddiqi', 'Nausheen Siddiqi'),
]

REASONS = [
    ("Loaner", "Loaner"),
    ("Regular", "Regular"),
    ("Short Term", "Short Term"),
    ("Long Term", "Long Term"),
    ("Other", "Other"),
]

CONDITION = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Broken', 'Broken'),
    ('Dented', 'Dented'),
    ('Ugly', 'Ugly'),
    ('Missing Accessory', 'Missing Accessory'),
    ('Other', 'Other'),
]

INSPECTION = [
    ('Done', 'Done'),
    ('Not Done', 'Not Done'),
]

LICENSE = [
    ('Expired', 'Expired'),
    ('Active', 'Active'),
]

class Device(models.Model):
    category            = models.CharField(max_length=1000, choices=CATEGORY, null=True, blank=True)
    device_name         = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    serial_no           = models.CharField(max_length=1000, null=True, blank=True)
    location            = models.CharField(max_length=1000, default='Not Assigned', null=True, blank=True)
    purchase_date       = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    last_maintained     = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    device_location     = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    maintained_by       = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    known_issues        = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    assigned_to         = models.CharField(max_length=1000, default='Not Assigned', null=True, blank=True)
    assigned_by         = models.CharField(max_length=1000, default='Not Assigned', choices=ADMINS, null=True, blank=True)
    date_assigned       = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    date_returned       = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    machine_condition   = models.CharField(max_length=1000, choices=CONDITION, null=True, blank=True)
    assignment_reason   = models.CharField(max_length=1000, choices=REASONS, default='Loaner', null=True, blank=True)
    license_expiry      = models.CharField(max_length=1000, default='N/A', null=True, blank=True)
    order_number        = models.CharField(max_length=1000, default='N/A', null=True, blank=True)


    def __str__(self):
        return f'{self.category}'


class Assignment(models.Model):
    devices             = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    staff               = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date                = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.devices.category} ({self.devices.device_name}) requested by {self.staff.username} at {self.date}'


class Maintenance(models.Model):
    choose_item         = models.CharField(max_length=1000, choices=CATEGORY)
    device_condition    = models.CharField(max_length=1000, choices=CONDITION)
    cover_inspection    = models.CharField(max_length=1000, default="Not Done", choices=INSPECTION)
    dust_inspection     = models.CharField(max_length=1000, choices=INSPECTION)
    antivirus_license   = models.CharField(max_length=1000, default='N/A', choices=LICENSE)
    system_license      = models.CharField(max_length=1000, default='N/A', choices=LICENSE)
    staff               = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Device condition: {self.device_condition}. Maintenance done by {self.staff.username}'

