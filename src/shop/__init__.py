from django.db.models import TextChoices


class Roles(TextChoices):
    CLIENT = 'CLIENT', 'CLIENT'
    ADMIN = 'ADMIN', 'ADMIN'
    MANAGER = 'MANAGER', 'MANAGER'
