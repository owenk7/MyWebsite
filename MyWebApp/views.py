from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePageView(request) :
    return render(request, 'homepage.html')

def resumePageView(request) :

    data = {
        'Experience' : ['BYU', 'City of Bentonville', 'Costco Wholesale'],
        'Education' : ['BYU', 'Bentonville High School'], 
        'Skills' : ['Programming with JavaScript', 'Programming with Python', 'SQL Database'],
    }
    return render(request, 'resume.html', data)

def aboutMePageView(request) :
    return render(request, 'aboutMe.html')