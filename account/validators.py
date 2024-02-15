from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_file_extension(value):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    extension = value.name.split('.')[-1]

    if extension.lower() not in allowed_extensions:
        raise ValidationError(
            _('Invalid file extension. Only JPG, JPEG, PNG, and GIF files are allowed.'),
            code='invalid_image_file_extension',
        )