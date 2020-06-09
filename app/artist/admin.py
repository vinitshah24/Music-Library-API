from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Artist as ArtistModel
from .forms import ArtistForm


# This will change the view in the admin view
class ArtistAdmin(UserAdmin):
    form = ArtistForm
    # Horizontal table view in admin console
    list_display = ('id','email', 'username', 'origin', 'genre',
                    'date_joined', 'last_logged', 'is_admin',
                    'is_active', 'is_staff', 'is_superuser')
    search_fields = ['username', 'origin', 'genre']
    readonly_fields = ['id', 'password', 'date_joined', 'last_logged']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ArtistModel, ArtistAdmin)

