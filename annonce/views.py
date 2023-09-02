from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from annonce.forms import *

# Create your views here.

from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import AddAd, PhotoForm  # Assurez-vous que les importations sont correctes


@login_required(login_url='/login')
def Ajouter(request):
    add_ad_form = AddAd()
    photo_form = PhotoForm()
    PhotoFormSet = formset_factory(PhotoForm, extra=4)
    formset = PhotoFormSet()

    if request.method == 'POST':
        add_ad_form = AddAd(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        formset = PhotoFormSet(request.POST, request.FILES)
        print(request.POST)
        print(add_ad_form)

        if add_ad_form.is_valid() and photo_form.is_valid() and formset.is_valid():
            annonce = add_ad_form.save(commit=False)
            annonce.user = request.user
            annonce.save()

            photo = photo_form.save(commit=False)
            photo.annonce_id = annonce.id
            photo.save()

            for formp in formset:
                if formp.cleaned_data:
                    images = formp.save(commit=False)
                    images.annonce_id = annonce.id
                    images.save()

            return redirect('home')  # Remplacez par la page appropriée

    ctx = {
        "form": add_ad_form,
        "photo_form": formset,
        "photo": photo_form,  # Utilisez un nom distinctif pour éviter la confusion
    }
    return render(request, 'annonces/ajouter.html', ctx)


def offres(request):
    annonces = Annonce.objects.filter(type='Offre')
    photos = Images.objects.all()

    ctx = {'annonces': annonces, 'photos': photos}
    return render(request, 'annonces/offres.html', ctx)


def demandes(request):
    annonces = Annonce.objects.filter(type='Demande')
    photos = Images.objects.all()
    print(Annonce.title)
    ctx = {'annonces': annonces, 'photos': photos}
    return render(request, 'annonces/demandes.html', ctx)


def mes_annonces(request):
    annonces = Annonce.objects.filter(user=request.user)
    photos = Images.objects.all()
    return render(request, 'annonces/mesAnnonces.html', {'annonces': annonces, 'photos': photos})
