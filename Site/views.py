from django.shortcuts import render
from django.http      import HttpResponse  
from django.db.models.functions import Concat 
from django.db.models import F, Value
from Site.models import Candidates 
import datetime
# Create your views here.


def home_page(request):
    
    if request.method=="POST":
        Candidates.objects.create(Name=request.POST['candidate_name'], Surname =request.POST['candidate_surname'],Birthdate=datetime.date(1999,12,11))

    candidates = Candidates.objects.all()
    
    return render(request,'home.html', {'candidates':candidates})

