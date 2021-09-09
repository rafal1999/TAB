from django.shortcuts           import render, redirect
from django.http                import HttpResponse  
# from django.db.models.functions import Concat 
# from django.db.models           import F, Value
from Site.models                import Candidates, Workers, Workers_Role, Recruitment_Meetings,Recruitment_Process, Candidates_Role
from datetime                   import date, datetime
from Site.api.workers           import add_worker
from Site.api.candidates        import edit_candidate
from django.views               import View
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth        import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from Site.api.candidates        import list_candidates, add_candidate, list_candidates_roles, add_process
from Site.api.interview         import add_interview_data, check_if_interview_took_place
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
        candidate.Birthdate =candidate.Birthdate.strftime("%Y-%m-%d") 
        return render(request,'editcandidate.html',{'candidate':candidate})
   
    candidate=Candidates.objects.get(ID=id_candidate)
    candidate.Birthdate =candidate.Birthdate.strftime("%Y-%m-%d")
    return render(request,'editcandidate.html',{'candidate':candidate})

def add_interview_data_page(request,id_process):

    if (check_if_interview_took_place(id_process=id_process)):
        return redirect('interview_summary_page',id_process=id_process)
   
    if(request.method=='POST'):
        add_interview_data(id_process=id_process, id_worker=1, hard_skils=request.POST['hard_skils'], 
                            soft_skils=request.POST["soft_skils"], grade=request.POST["grade"], notes=request.POST['notes']) 
        return redirect(interview_summary_page,id_process=id_process)

    process = Recruitment_Process.objects.get(ID=id_process)
    candidate=Candidates.objects.get(ID=process.ID_Candidates.ID)
    role = Candidates_Role.objects.get(ID=process.ID_Candidates_Role.ID)

    return render(request, 'interview.html',{'candidate':candidate,'role':role})


def interview_summary_page(request, id_process):

    process = Recruitment_Process.objects.get(ID=id_process)
    candidate=Candidates.objects.get(ID=process.ID_Candidates.ID)
    role = Candidates_Role.objects.get(ID=process.ID_Candidates_Role.ID)   
    interview_data = Recruitment_Meetings.objects.get(ID_Recruitment_Process=process)
    
    return render(request,"interview_summary.html",{'candidate':candidate,'role':role,
                'interview_data': interview_data})

def assistant_page(request):
# 
    if(request.method=='POST'):
        if(request.POST['form_type']=='addform'):
           return  redirect('add_candidate_page') 
        if(request.POST['form_type']=='editform'):
           return  redirect('edit_candidate_page',id_candidate=int(request.POST["candidate"]))
        if(request.POST['form_type']=='processform'):
           return redirect('add_process_page')

    candidates = Candidates.objects.all() 
    return render(request,"assistant.html",{'candidates':candidates})

def add_candidate_page(request):
    if request.method=="POST":
        add_candidate(name=request.POST['candidate_name'],surname=request.POST['candidate_surname'], 
                        birthday=request.POST['candidate_birthdate'], phone_number=request.POST['candidate_phone_number'],
                        sex=request.POST['candidate_sex'], email='test@m.com',cv='pass',motivation_letter='pas',
                        hired='P')
        return  redirect('assistant_page')

    return render(request,"addcandidate.html") 	

def add_process_page(request):

    candidates=list_candidates()
    roles=list_candidates_roles()
    if(request.method=='POST'):
        add_process(id_candidate=request.POST['candidate'], id_role=request.POST['role'])

    return render(request,'addprocess.html',{'candidates':candidates, 'roles':roles})

def process_sumary_page(request): #dsad
    pass