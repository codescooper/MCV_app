from django.shortcuts import render
from .models import Evenement, Predications

def accueil(request):
    return render(request, 'core/accueil.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def predications(request):
    predications = Predications.objects.all().order_by('-date')  # Tous les predications, triés par date la plus récente
    return render(request, 'core/predications.html', {'predications': predications})

def agenda(request):
    evenements = Evenement.objects.all().order_by('date')  # Tous les événements, triés par date
    return render(request, 'core/agenda.html', {'evenements': evenements})
