from django.contrib import admin

from .models import Album as AlbumModel
from .forms import AlbumForm


# This will change the view in the admin view
class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    # Horizontal table view in admin console
    list_display = ('id', 'name', 'song')
    search_fields = ('id', 'name', 'song')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(AlbumModel, AlbumAdmin)
