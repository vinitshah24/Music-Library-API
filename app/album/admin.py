from django.contrib import admin

from .models import Album as AlbumModel
from .forms import AlbumForm


# This will change the view in the admin view
class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    # Horizontal table view in admin console
    list_display = ('id', 'name', 'get_songs')
    search_fields = ('id', 'name', 'get_songs')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_songs(self, obj):
        return "\n".join([s.name for s in obj.song.all()])


admin.site.register(AlbumModel, AlbumAdmin)
