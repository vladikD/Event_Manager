import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from .validators import validate_image_file_extension

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=128, validators=[validate_password])
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, validators=[validate_image_file_extension])
    email_confirmed = models.BooleanField(default=False)
