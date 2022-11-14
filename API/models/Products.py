from django.db import models
from django.utils.translation import gettext_lazy as _

from base_model.models import AbstractModel


class Products(AbstractModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
