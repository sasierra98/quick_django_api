from django.db import models
from django.utils.translation import gettext_lazy as _

from API.models import Clients, Products
from base_model.models import AbstractModel


class Bills(AbstractModel):
    client = models.ForeignKey(verbose_name=_('Client'), to=Clients, on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name=_('Company name'), max_length=50)
    nit = models.PositiveIntegerField(verbose_name=_('NIT'))
    code = models.CharField(verbose_name=_('Code'), max_length=150)
    products = models.ManyToManyField(verbose_name=_('Products'), to=Products)
