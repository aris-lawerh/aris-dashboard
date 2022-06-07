from contextlib import contextmanager
import re
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from django.db.models import Q 

from .models import Device
from .forms import DeviceForm
from .filters import DeviceFilter
# Create your views here.


@login_required
def index(request):
    items = Device.objects.all()
    staff = User.objects.all()
    user = User.objects.all()

    if request.method == 'POST':
        send_mail(
            subject='Request for a Device.',
            message='Dear IT Support,\n\nPlease, ' + str(request.user.first_name) + ' ' + str(request.user.last_name) + ' would like to request a device. Kindly send the device request form link to their mail at, ' + str(request.user.email) + '\n\nRegards,\nLawerh Caesar.',
            from_email= request.user.email,
            recipient_list= ['l.caesar@aris.edu.gh', 'support@aris.edu.gh', 'gmuhammad@aris.edu.gh'],
            fail_silently=True
        )
        messages.success(request, 'Your mail has been sent successfully. Expect a mail from IT Support soon.', fail_silently=True)
        return redirect('index')
    
    context = {
        'items' : items,
        'user'  : request.user,
        'staff' : staff,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def dashboard(request):
   return render(request, 'dashboard/base1.html')

def help(request):
    
    return render(request, 'dashboard/help.html')

@login_required
def devices(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
    #items = Device.objects.filter(assigned_to__icontains=q)
        multiple_q = Q(Q(device_name__icontains=q) | Q(assigned_to__icontains=q) | Q(category__icontains=q))
        items = Device.objects.filter(multiple_q)
        page = Paginator(items, 10)
        page_list = request.GET.get('page')
        page = page.get_page(page_list) 
    else:            
        #ORM - Object Relational Model
        items = Device.objects.all()
        #or in SQL
        #items = Device.objects.raw('SELECT * FROM dashboard_device')
        page = Paginator(items, 10)
        page_list = request.GET.get('page')
        page = page.get_page(page_list) 

    context = {
        'page': page,
    }
    return render(request, 'dashboard/devices.html', context)


def device_delete(request, pk):
    item = Device.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('devices')
    return render(request, 'dashboard/device_delete.html')

def device_update(request, pk):
    item = Device.objects.get(id=pk)
    if request.method =='POST':
        form = DeviceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('devices')
    else:
        form = DeviceForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/device_update.html', context)

@login_required
def device_add(request):
    if request.method =='POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devices')
    else:
        form = DeviceForm()
        
    context = {
        'form': form,
    }
    return render(request, 'dashboard/device_add.html', context)

@login_required
def device_filter(request):
    items = Device.objects.all()
    if request.method =='POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devices')
    else:
        form = DeviceForm()
    
    myFilter = DeviceFilter(request.GET, queryset=items)
    items = myFilter.qs

    page = Paginator(items, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list) 


    context = {
        'form' : form,
        'page': page,
        'myFilter': myFilter,
    }
    return render(request, 'dashboard/device_filter.html', context)

@login_required
def assignment(request):
    return render(request, 'dashboard/assignment.html')

@login_required
def staff(request):
    teachers = User.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    teachers = User.objects.get(id=pk)
    context = {
        'teachers': teachers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def maintenance(request):
    return render(request, 'dashboard/maintenance.html')