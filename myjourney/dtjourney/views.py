from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    """Display all learning journeys"""
    try:
        journeys = LearningJourney.objects.all()
        context = {'journeys': journeys}
        return render(request, 'dtjourney/index.html', context)
    except Exception as e:
        context = {
            'journeys': [],
            'error_message': 'Sorry, there was an error loading the journeys.',
        }
        return render(request, 'dtjourney/index.html', context)

def aboutMe(request):
    """Display all about me entries"""
    try:
        details = AboutMe.objects.all()
        context = {'details': details}
        return render(request, 'dtjourney/aboutMe.html', context)
    except Exception as e:
        context = {
            'details': [],
            'error_message': 'Sorry, there was an error loading the information.',
        }
        return render(request, 'dtjourney/aboutMe.html', context)
