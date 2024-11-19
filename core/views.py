from django.shortcuts import render
from .models import Evenement, Predications, EgliseInfo
from .forms import ContactForm

def accueil(request):
    return render(request, 'core/accueil.html')

def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire ici
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Vous pourriez envoyer un email ici ou sauvegarder dans la base de données
            return render(request, 'core/contact_success.html', {'nom': nom})
    else:
        form = ContactForm()
    
    # Récupérez les informations de l'église
    eglise_info = EgliseInfo.objects.first()
    
    return render(request, 'core/contacts.html', {
        'form': form,
        'adresse_eglise': eglise_info.adresse,
        'email_eglise': eglise_info.email,
        'telephone_eglise': eglise_info.telephone,
        'programme_hebdomadaire': eglise_info.programme_hebdomadaire
    })
    

def predications(request):
    predications = Predications.objects.all().order_by('-date')  # Tous les predications, triés par date la plus récente
    return render(request, 'core/predications.html', {'predications': predications})

def agenda(request):
    evenements = Evenement.objects.all().order_by('date')  # Tous les événements, triés par date
    return render(request, 'core/agenda.html', {'evenements': evenements})
