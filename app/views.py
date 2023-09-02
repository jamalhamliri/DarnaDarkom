from django.shortcuts import render

from annonce.models import Annonce, Images


# Create your views here.

# la page home
def home(request):
    offres = Annonce.objects.filter(type='Offre')
    demandes = Annonce.objects.filter(type='Demande')
    photos = Images.objects.all()
    ctx={'offres':offres,'demandes':demandes,'photos':photos }
    return render(request, 'app/home.html',ctx)


def about_us(request):
    return render(request, 'app/about_us.html')


def contact(request):
    return render(request, 'app/contact.html')


def security(request):
    return render(request, 'app/security.html')
