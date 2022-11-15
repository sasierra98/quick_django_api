from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from base_model.models import AbstractModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, AbstractModel):
    email = models.EmailField(verbose_name=_('email'), unique=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
