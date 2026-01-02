from django.shortcuts import render
from django.urls import conf
from .utils import paginateProfiles, searchProfiles
from .models import Profile

# Create your views here.

def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'projects/profiles.html', context)