from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from .models import Device, Assignment, Maintenance
from user.models import Profile
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

admin.site.site_header = 'ARIS Inventory Admin Page'

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'device_name',
        'serial_no',
        'location',
        'assigned_to',
        'assigned_by',
        'purchase_date',
        'last_maintained',
        'maintained_by',
        'known_issues',
        'date_assigned',
        'date_returned',
        'assignment_reason',
        'machine_condition',
        'license_expiry',
        'order_number'
        )
    list_filter = ['category','serial_no' ,'assigned_to', 'assignment_reason']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                url = reverse('admin:index')
                return HttpResponseRedirect(url)


            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split("\n")
            num=0

            for x in csv_data:
                col = x.split(",")

                created = Device.objects.update_or_create(
                        category            = col[0],
                        device_name         = col[1],
                        serial_no           = col[2],
                        location            = col[3],
                        assigned_to         = col[4],
                        assigned_by         = col[5],
                        purchase_date       = col[6],
                        last_maintained     = col[7],
                        maintained_by       = col[8],
                        known_issues        = col[9],
                        date_assigned       = col[10],
                        date_returned       = col[11],
                        assignment_reason   = col[12],
                        device_location     = col[13],
                        machine_condition   = col[14],
                        license_expiry      = col[15],
                        order_number        = col[16],
                    )
                num+=1

        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/csv_upload.html', data)

admin.site.register(Device, DeviceAdmin)
admin.site.register(Assignment)
admin.site.register(Maintenance)
admin.site.register(Profile)
