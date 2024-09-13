from django.shortcuts import render

# Create your views here.

# dummy data
skills = ['Python', 'JavaScript', 'Django']

def skills_list(request):
    return render(request, 'skills/skills_list.html', {'skills': skills})