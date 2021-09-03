from django.shortcuts           import render
from django.http                import HttpResponse  
# from django.db.models.functions import Concat 
# from django.db.models           import F, Value
from Site.models                import Candidates, Workers, Workers_Role 
from datetime                   import date, datetime
from Site.api.workers           import add_worker
from Site.api.candidates        import edit_candidate
from django.views               import View
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth        import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from Site.api.candidates        import list_candidates, add_candidate
# Create your views here.

def test_workers_page(request):
    if_create=False
    if request.method=="POST":
        y=int(request.POST['worker_year_of_birth'])
        m=int(request.POST['worker_month_of_birth'])
        d=int(request.POST['worker_month_of_birth'])
        worker_role=request.POST['worker_role']
        add_worker(name=request.POST['worker_name'], surname=request.POST['worker_surname'], birthday=date(y,m,d), worker_role=worker_role)
    workers = Workers.objects.all()# tabele się łączą automatycznie jeśli mają powiązanie,
    
    return render(request,'testworkers.html', {'workers':workers})

# def home_page(request):
#     return render(request,'home.html')

def test_candidates_page(request):

    if request.method=="POST":
        y=int(request.POST['candidate_year_of_birth'])
        m=int(request.POST['candidate_month_of_birth'])
        d=int(request.POST['candidate_month_of_birth'])
        add_candidate(name=request.POST['candidate_name'],surname=request.POST['candidate_surname'], 
                        birthday=date(y,m,d), phone_number=request.POST['candidate_phone_number'],
                        sex=request.POST['candidate_sex'], email='test@m.com',cv='pass',motivation_letter='pas',
                        hired='P')

    candidates = list_candidates()
    
    return render(request,'testcandidates.html', {'candidates':candidates})





class Home(View):
    template = 'home.html'
    login_url = 'login/'

    def get(self,request,id_test):
        return render(request, self.template,{'test':{'id_test':id_test}})


class Index(LoginRequiredMixin,View):
    template = 'index.html'
    login_url = 'login/'

    def get(self, request):
        return render(request, self.template) 




def edit_candidate_page(request,id_candidate):

    if(request.method=='POST'):
        edit_candidate(id=id_candidate,name=request.POST['candidate_name'],surname=request.POST['candidate_surname'], 
                        birthday=request.POST['candidate_birthdate'], phone_number=request.POST['candidate_phone_number'],
                        sex=request.POST['candidate_sex'], email=request.POST['candidate_email'],
                        cv=request.POST['candidate_cv'],motivation_letter=request.POST['candidate_motivation_letter'],)
        candidate=Candidates.objects.get(ID=id_candidate)
        print(candidate.Birthdate)
        print(type(candidate.Birthdate))
        candidate.Birthdate =candidate.Birthdate.strftime("%Y-%m-%d") 
        print(type(candidate.Birthdate))
        print(f"_{candidate.Birthdate}_ {type(candidate.Birthdate)}") 
        return render(request,'editcandidate.html',{'candidate':candidate})

    # if(request.method=='PUT'):
    candidate=Candidates.objects.get(ID=id_candidate)
    candidate.Birthdate =candidate.Birthdate.strftime("%Y-%m-%d")
    return render(request,'editcandidate.html',{'candidate':candidate})