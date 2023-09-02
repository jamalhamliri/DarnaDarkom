from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager

import datetime


# fonction pour convert email a des lettres minuscules
class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """

    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value


# la table utilisateur
class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('', 'Choose gender'),
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    Normal = 'Normal'
    Type = (
        ("Pro", "PRO"),
        ("Normal", "NORMAL")
    )
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Seuls les caractères alphanumériques sont autorisés.')
    pinnumbers = RegexValidator(r'^[0-9]*$', 'Seuls les chiffres entre 0 et 9 sont autorisés.')
    email = LowercaseEmailField(_('email address'), max_length=255, unique=True)
    first_name = models.CharField(max_length=150, blank=True, validators=[alphanumeric])
    last_name = models.CharField(max_length=150, blank=True, validators=[alphanumeric])
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True)
    type = models.CharField(max_length=50, default=Normal)

    image = models.ImageField(verbose_name='Photo de profil', upload_to='media/user/', blank=True)

    phone_regex = RegexValidator(regex=r'^\d{16}$', message="phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=16, blank=True,
                             null=True)  # you can set it unique = True
    date_of_birth = models.DateField(_("Date de naissance"), default=datetime.date.today)
    date_joined = models.DateTimeField(default=timezone.now)
    # Les utilisateurs de is staff auront accès aux abonnements au panneau d'administration, etc.
    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)  # Détermine que l'utilisateur peut se connecter à l'application Web

    # lorsque l'utilisateur est créé, le système envoie un e-mail après avoir vérifié l'utilisateur, nous vérifions que l'utilisateur est actif

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ProUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=True)
    premium_expiry_date = models.DateTimeField()
    date_joined = models.DateTimeField(default=timezone.now)


class Payments(models.Model):
    user = models.OneToOneField(ProUser, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField(default=timezone.now)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(verbose_name="Location", max_length=100, blank=True)
    about = models.CharField(verbose_name="Bio", max_length=100, blank=True)
    Hebregement = models.BooleanField(default=False)
    rating_average = models.FloatField()
