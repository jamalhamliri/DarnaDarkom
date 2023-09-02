from django.db import models

from annonce.validators import file_size
from users.models import CustomUser
from PIL import Image


# Create your models here.
class Pays(models.Model):
    name = models.CharField(verbose_name="nom de pays", max_length=255,
                            unique=True)

    def __str__(self):
        return self.name


class Ville(models.Model):
    pays = models.ForeignKey(Pays,
                             related_name='Pays',
                             on_delete=models.CASCADE)
    ville_name = models.CharField(verbose_name="ville name", max_length=255,
                                  unique=True)

    def __str__(self):
        return "Pays "+ self.pays.name + " : Ville " + self.ville_name


# la table pour les annonces
class Annonce(models.Model):
    AnnonceType = (
        ("Offre", "OFFRE"),
        ("Demande", "DEMANDE")
    )
    Type_hebergement= (
        ("Hotel", "HOTEL"),
        ("Maison", "MAISON"),


    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pays = models.ForeignKey(Pays, related_name='pays_annonce', on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(verbose_name="Location", max_length=100, blank=True)
    type = models.CharField(max_length=50, choices=AnnonceType)
    type_hebergement = models.CharField(max_length=50, choices=Type_hebergement, blank=True)
    description = models.TextField(verbose_name="Description", max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, default=None, related_name='images')
    image = models.ImageField(upload_to='media/annonce', validators=[file_size])
    IMAGE_MAX_SIZE = (400, 400)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.image.path)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Reservations(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reservations_as_guest')
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation {self.id} by {self.user.email} for {self.annonce.title}"


class Reviews(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews_as_reviewer')
    reviewed_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews_as_reviewed_user')
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} by {self.reviewer.email} for {self.reviewed_user.email} on {self.annonce.title}"
