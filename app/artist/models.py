from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class ArtistManager(BaseUserManager):
    def create_artist(self, email, username, born_date, origin, genre, password=None):
        if not email:
            raise ValueError("Email not provided!")
        if not username:
            raise ValueError("Username not provided!")
        if not born_date:
            raise ValueError("Date of Birth not provided!")
        if email is not None and username is not None and born_date is not None:
            artist = self.model(
                email=self.normalize_email(email),
                username=username,
                born_date=born_date,
                origin=origin,
                genre=genre
            )
            artist.set_password(password)
            artist.save(using=self._db)
            return artist

    def create_superuser(self, email, username, born_date, origin, genre, password=None):
        if not email:
            raise ValueError("Email not provided!")
        if not username:
            raise ValueError("Username not provided!")
        if not born_date:
            raise ValueError("Date of Birth not provided!")
        if email is not None and username is not None and born_date is not None:
            artist = self.create_artist(
                email=self.normalize_email(email),
                username=username,
                born_date=born_date,
                origin=origin,
                genre=genre
            )
            artist.set_password(password)
            artist.is_admin = True
            artist.is_staff = True
            artist.is_superuser = True
            artist.save(using=self._db)
            return artist


class Artist(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",
                              max_length=100, unique=True)
    username = models.CharField(verbose_name="username", max_length=100, unique=True)
    born_date = models.DateField(verbose_name="born date")
    origin = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name="date joined",
                                       auto_now_add=True)
    last_logged = models.DateTimeField(verbose_name="last login",
                                       auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Use email for login credential
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'born_date', 'origin', 'genre']

    objects = ArtistManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        return self.is_admin

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        return True
