from django.contrib import admin
from django.urls import path, include
from dashboard import views as dash_views
from user import views as user_views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView




urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', dash_views.index, name='dashboard'),
    path('help/', dash_views.help, name='help'),
    path('devices/', dash_views.devices, name='devices'),
    path('assignment/', dash_views.assignment, name='assignment'),
    path('maintenance/', dash_views.maintenance, name = "maintenance"),
    path('register/', user_views.register, name='register' ),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('staff/', dash_views.staff, name='staff'),
    path('staff/detail/<int:pk>/', dash_views.staff_detail, name='staff-detail'),
    path('profile/update/', user_views.profile_update, name='profile-update'),
    path('', dash_views.index, name='index'),
    #path('', dash_views.index, name='dashboard'),
    path('devices/add/', dash_views.device_add, name='device-add'),
    path('devices/filter/', dash_views.device_filter, name='device-filter'),
    path('devices/delete/<int:pk>/', dash_views.device_delete, name='device-delete'),
    path('devices/update/<int:pk>/', dash_views.device_update, name='device-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)