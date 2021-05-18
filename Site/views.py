from django.shortcuts           import render
from django.http                import HttpResponse  
from django.db.models.functions import Concat 
from django.db.models           import F, Value
from Site.models                import Candidates, Workers, Workers_Role 
from datetime                   import date
# Create your views here.


def home_page(request):
    if_create=False
    if request.method=="POST":
        y=int(request.POST['worker_year_of_birth'])
        m=int(request.POST['worker_month_of_birth'])
        d=int(request.POST['worker_month_of_birth'])
        worker_role=request.POST['worker_role']
        if worker_role=="": #jeśli puste 
            Workers.objects.create(Name=request.POST['worker_name'], Surname =request.POST['worker_surname'],Birthdate=date(y,m,d),ID_Workers_Role=None)
    
        else:
            obj,if_create= Workers_Role.objects.get_or_create(Name=worker_role) #zwraca truple i jeśli obj istneije w bazie to go nie dodaje  if_create jest wtedy  false 
            Workers.objects.create(Name=request.POST['worker_name'], Surname =request.POST['worker_surname'],Birthdate=date(y,m,d),ID_Workers_Role=obj)#działa nawet jesli podajemy tą samą rolę

    workers = Workers.objects.all()# tabele się łączą automatycznie jeśli mają powiązanie,
    
    return render(request,'home.html', {'workers':workers})

