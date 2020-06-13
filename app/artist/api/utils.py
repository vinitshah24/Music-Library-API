
import datetime
from django.conf import settings
from django.utils import timezone

from rest_framework_jwt.settings import api_settings
EXPIRATION_DELTA = api_settings.JWT_REFRESH_EXPIRATION_DELTA

#  Responsible for controlling the response data returned after login or refresh
# Override to return a custom response including the serialized representation of the User
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + EXPIRATION_DELTA - datetime.timedelta(seconds=200)
    }
