from django.contrib import admin

from.models import Song as SongModel
from.forms import SongForm


# This will change the view in the admin view
class SongAdmin(admin.ModelAdmin):
    form = SongForm
    # Horizontal table view in admin console
    list_display = ('id', 'name', 'year_released', 'genre', 'artist')
    search_fields = ('id', 'name', 'year_released', 'genre', 'artist')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(SongModel, SongAdmin)
