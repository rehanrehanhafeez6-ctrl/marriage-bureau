from django.shortcuts import render
from .models import Profile


def home(request):
    count = Profile.objects.filter(is_approved=True).count()
    return render(request, 'home.html', {'approved_count': count})