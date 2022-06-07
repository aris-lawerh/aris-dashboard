import django_filters
from.models import *

class DeviceFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        fields = ['category', 'device_name', 'location', 'purchase_date']