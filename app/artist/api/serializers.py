from rest_framework import serializers

from artist.models import Artist as ArtistModel


class ArtistSerializer(serializers.ModelSerializer):

    # Extra kwargs - Password is Extra field
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = ArtistModel
        fields = [
            'email', 'password', 'username', 'born_date',
            'origin', 'genre'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        artist = ArtistModel(
            email=validated_data['email'],
            username=validated_data['username'],
            born_date=validated_data['born_date'],
            origin=validated_data['origin'],
            genre=validated_data['genre']
        )
        artist.set_password(validated_data['password'])
        artist.save()
        return artist

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.born_date = validated_data.get(
            'born_date', instance.born_date)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.set_password(validated_data.get('password', instance.genre))
        instance.save()
        return instance

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request is not None and not request.parser_context.get('kwargs'):
            fields.pop('email', None)
            fields.pop('is_admin', None)
            fields.pop('is_staff', None)
            fields.pop('is_superuser', None),
            fields.pop('password', None)
        return fields


class ArtistAdminSerializer(serializers.ModelSerializer):

    # Extra kwargs - Password is Extra field
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = ArtistModel
        fields = [
            'email', 'password', 'username', 'born_date',
            'origin', 'genre', 'is_admin',
            'is_staff', 'is_superuser'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        artist = ArtistModel(
            email=validated_data['email'],
            username=validated_data['username'],
            born_date=validated_data['born_date'],
            origin=validated_data['origin'],
            genre=validated_data['genre'],
            is_admin=validated_data['is_admin'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],
        )
        artist.set_password(validated_data['password'])
        artist.save()
        return artist

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.born_date = validated_data.get(
            'born_date', instance.born_date)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.set_password(validated_data.get('password', instance.genre))
        instance.save()
        return instance
