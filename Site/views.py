from django.shortcuts import render
from django.http      import HttpResponse  
from django.db.models.functions import Concat 
from django.db.models import F, Value
from Site.models import Candidates 
# Create your views here.


def home_page(request):
    
    if request.method=="POST":
        Candidates.objects.create(Name=request.POST['candidate_name'], Surname =request.POST['candidate_surname'])

    candidates = Candidates.objects.all()
    
    return render(request,'home.html', {'candidates':candidates})

