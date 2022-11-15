from django.db import models
from django.utils.translation import gettext_lazy as _

from base_model.models import AbstractModel

TYPE_DOCUMENT_CHOICES = (
    ('CC', _('ID Card')),
    ('TI', _('Card Identification')),
    ('NIT', _('NIT'))
)


class Clients(AbstractModel):
    """
    Model which contains information about clients
    """
    document = models.PositiveIntegerField(verbose_name=_('Document'))
    type_document = models.CharField(
        verbose_name=_('Type document'), max_length=3, choices=TYPE_DOCUMENT_CHOICES
    )
    first_name = models.CharField(verbose_name=_('First name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email'), max_length=150)
