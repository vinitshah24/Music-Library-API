from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/artist/', include('artist.api.admin_urls')),
    path('api/artist/', include('artist.api.local_urls')),
]
