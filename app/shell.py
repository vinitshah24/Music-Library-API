from playlist.models import Playlist
from album.models import Album
from song.models import Song
import os
import json
from django.core import serializers

from artist.models import Artist


# List all artists
artist_list = Artist.objects.all()
qs_json = serializers.serialize('json', artist_list)
json_data = json.loads(qs_json)
print(json_data)

# Create new artist
newArtist = Artist.objects.create(
    email='wiley@abc.com', username='wiley',
    born_date='2020-02-02', origin='China', genre='Pop'
)
newArtist.set_password('wiley')
newArtist.save()
a = Artist.objects.filter(email='wiley@abc.com')
result = a.update(is_admin=True, is_staff=True, is_superuser=True)
if result == 1:
    print("SUCCESS")

# Create new artist with admin and staff flags
newArtist2 = Artist.objects.create(
    email='testPerm@abc.com', username='testPerm',
    born_date='2020-03-02', origin='Russia', genre='Pop',
    is_admin=True, is_staff=True, is_superuser=True
)
newArtist2.save()

# Delete an Artist by filtering the email
delArtist = Artist.objects.filter(email='testPerm@abc.com').first().delete()
print(newArtist2)

# GET by id -> pk
getArtist = Artist.objects.filter(id=8)
queryset = serializers.serialize('json', getArtist)
artist_details = json.loads(queryset)
print(artist_details)

# -----------------------------------------------------------


# Create song
artist_for_song = Artist.objects.filter(id=2)
newSong = Song.objects.create(
    name='TestSong', year_released='2020',
    genre='Country', artist=artist_for_song.get()
)

# Delete the artist to check if the song is deleted [Relationship check] - SUCCESS
delSongArtist = Artist.objects.filter(id=2).first().delete()
print(delSongArtist)


# Clean Console
os.system('cls')

# -----------------------------------------------------------


# GET all albums
album_list = Album.objects.all()
qs_json = serializers.serialize('json', album_list)
json_data = json.loads(qs_json)
print(json_data)

# Get single album
album = Album.objects.filter(id=1)
qs_json = serializers.serialize('json', album)
json_data = json.loads(qs_json)
print(json_data)

exitingAlbum = Album.objects.first()

# Add song to the album
Album.objects.create(name="TestMe", song=newSong)

# -----------------------------------------------------------


# Get all playlists
playlists = Playlist.objects.all()
qset = serializers.serialize('json', playlists)
ps_data = json.loads(qset)
print(ps_data)


# Create playlist and add a song
addSong = Song.objects.filter(id=2).get()
newPlaylist = Playlist.objects.create(name="UKHits")
newlyCreatedPlaylist = Playlist.objects.filter(id=2).get()
newlyCreatedPlaylist.song.add(addSong)

# -----------------------------------------------------------

# Check if the song is owned by the user
findsong = Song.objects.filter(id=3)
print(findsong)

json_ser = serializers.serialize('json', findsong)
data = json.loads(json_ser)
print(type(data[0]['fields']['artist']))
print("Song Owner ID: " + str(data[0]['fields']['artist']))

