from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import annonce.views

app_name = 'annonce'
urlpatterns = [
    # les liens pour l'application utilisateur
    path('Ajouter/', annonce.views.Ajouter, name="Ajouter"),
path('Offres/', annonce.views.offres, name="Offres"),
path('Demandes/', annonce.views.demandes, name="Demandes"),
path('mes_annonces/', annonce.views.mes_annonces, name="mes_annonces"),


]
