from django.shortcuts           import render
from django.http                import HttpResponse  
from django.db.models.functions import Concat 
from django.db.models           import F, Value
from Site.models                import Candidates, Workers 
from datetime                   import date
# Create your views here.


def home_page(request):
    
    if request.method=="POST":
        Candidates.objects.create(Name=request.POST['candidate_name'], Surname =request.POST['candidate_surname'],Birthdate=date(1999,12,11))

    candidates = Workers.objects.all()# tabele się łączą automatycznie jeśli mają powiązanie,
    
    return render(request,'home.html', {'candidates':candidates})

