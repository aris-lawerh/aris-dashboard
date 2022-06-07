from django import forms
from .models import Device, Assignment


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['category', 'device_name', 'serial_no', 'assigned_to', 'purchase_date']

class DeviceUpdateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['category', 'device_name', 'serial_no', 'assigned_to', 'purchase_date']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['devices', 'staff']

