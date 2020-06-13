from django.contrib import admin

from .models import Playlist as PlaylistModel
from .forms import PlaylistForm


# This will change the view in the admin view
class PlaylistAdmin(admin.ModelAdmin):
    form = PlaylistForm
    # Horizontal table view in admin console
    list_display = ('id', 'name', 'get_songs')
    search_fields = ('id', 'name', 'get_songs')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_songs(self, obj):
        return "\n".join([s.name for s in obj.song.all()])


admin.site.register(PlaylistModel, PlaylistAdmin)
