from django.db import models


class AbstractModel(models.Model):
    """
    Abstract model used to provide essential fields to models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
