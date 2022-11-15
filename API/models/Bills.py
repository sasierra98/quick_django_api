from django.db import models
from django.utils.translation import gettext_lazy as _

from API.models import Clients, Products
from base_model.models import AbstractModel


class Bills(AbstractModel):
    client = models.ForeignKey(verbose_name=_('Client'), to=Clients, on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name=_('Company name'), max_length=50)
    nit = models.PositiveBigIntegerField(verbose_name=_('NIT'))
    code = models.PositiveSmallIntegerField(verbose_name=_('Verification code'), null=True)
    products = models.ManyToManyField(verbose_name=_('Products'), to=Products)
