from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, sic, email, first_name, password=None):
        if not sic:
            raise ValueError('Users must have an sic')

        user = self.model(
            sic=sic,
            email=self.normalize_email(email),
            first_name=first_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, sic, email, first_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            sic=sic,
            email=email,
            first_name=first_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    sic = models.CharField(max_length=15, unique=True)
    email = models.EmailField(verbose_name='email address')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'sic'
    REQUIRED_FIELDS = ['email', 'first_name']

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.sic

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
