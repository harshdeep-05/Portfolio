from django.shortcuts import render
from .models import Skills
# Create your views here.

def home(request):

    skill1=Skills()
    skill1.type = 'Languages'
    skill1.name = 'C++'
    skill1.level = 4

    skill2=Skills()
    skill2.type = 'Frontend'
    skill2.name = 'Html'
    skill2.level = 3

    skill3=Skills()
    skill3.type = 'Backend'
    skill3.name = 'Django'
    skill3.level = 3

    skill4=Skills()
    skill4.type = 'Creative'
    skill4.name = 'Guitar'
    skill4.level = 5

    skills= [skill1,skill2,skill3,skill4]
    return render(request, 'blog/home.html', {'skills': skills}) 

def Blog(request):
        return render(request, 'blog/Blog.html')