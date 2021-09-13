from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from django.db import models
from Site import constants
from django.shortcuts           import redirect, render
from django.http                import HttpResponse  
# from django.db.models.functions import Concat 
# from django.db.models           import F, Value
from Site.models                import Candidates, Workers, Workers_Role, Calendar
from datetime                   import date, datetime
from Site.api.workers           import add_worker
from django.views               import View
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth        import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from Site.api.candidates        import (list_candidates, add_candidate, list_candidates_roles, add_process, 
                                        list_processes_by_role, list_processes_without_tests_by_role, list_processes_by_role_and_stage)
from Site.api.interviews        import check_if_interview_took_place, add_interview_data
import Site.api.workers         as WorkersAPI
import Site.api.calendar        as Calendar
import Site.api.tests           as tests
from Site.models                import Workers, Recruitment_Process, Candidates_Role, Recruitment_Meetings
from django                     import forms      
from Site.forms                 import MeetingTypeForm
from django.contrib.auth.models import User
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

def test_calendar_page(request):
    
    if request.method=="POST":
        myDate = request.POST['date']
        
        Calendar.add_meeting(date=datetime.strptime(myDate, "%d/%m/%Y %H:%M"), desc=request.POST['meeting_desc'], 
                    meeting_type='R', worker_ids=Workers.objects.all()[0], recruitment_process_id=Recruitment_Process.objects.all()[0])
    meetings = Calendar.list_meetings()
    f = forms.DateField()
    
    return render(request,'testcalendar.html', {'meetings':meetings, 'form':f})

def create_meeting(request):
    workers = WorkersAPI.list_workers()
    tf = MeetingTypeForm(request.POST)
    if request.method=="POST":
        date = "01.01.2000 00:00"
        type = 'T'
        worker = WorkersAPI.get_worker(0)
        if (tf.is_valid()):
            type = tf.cleaned_data['Meeting_type']
            date = tf.cleaned_data['Meeting_date']
            workername = request.POST['workers'].split()
            worker = WorkersAPI.get_worker_by_name(workername[0], workername[1])
        
        Calendar.add_meeting(date=date, desc=request.POST['meeting_desc'], 
                    meeting_type=type, worker_ids=worker, recruitment_process_id=Recruitment_Process.objects.all()[0])
        response = redirect('/calendar/')
        return response
    f = forms.DateField()
    f2 = forms.ChoiceField()
    return render(request, 'calendarcreate.html', {'tf':tf, "workers":workers})

def edit_meeting(request, id):
    workers = WorkersAPI.list_workers()
    meeting = Calendar.get_meeting(id)
    tf = MeetingTypeForm(request.POST)
    worker = WorkersAPI.get_worker(0)
    if request.method=="POST":
        date = "01.01.2000 00:00"
        type = meeting.Meeting_type
        worker = worker
        if (tf.is_valid()):
            type = tf.cleaned_data['Meeting_type']
            date = tf.cleaned_data['Meeting_date']
            workername = request.POST['workers'].split()
            worker = WorkersAPI.get_worker_by_name(workername[0], workername[1])

        Calendar.edit_meeting(meeting_id = id, date=date, desc=request.POST['meeting_desc'], 
                    meeting_type=type, worker_ids=worker, recruitment_process_id=Recruitment_Process.objects.all()[0])
        meeting = Calendar.get_meeting(id)

    return render(request, 'calendaredit.html', {'meeting':meeting, 'tf':tf, "workers":workers, "worker":worker})

def delete_meeting(request, id):
    Calendar.delete_meeting(id)
    response = redirect('/calendar/')
    return response

def confirm_meeting(request, id):
    Calendar.confirm_meeting(id)
    response = redirect('/calendar/')
    return response

def cancel_meeting(request, id, desc):
    Calendar.cancel_meeting(id, desc)
    response = redirect('/calendar/')
    return response

class Home(View):
    template = 'home.html'
    login_url = 'login/'

    def get(self,request):
        worker = None
        if request.user.is_authenticated:
            worker = WorkersAPI.get_worker_by_user_id(request.user.id)
        return render(request, self.template, { 'worker':worker })


class Index(View):
    template = 'index.html'
    login_url = 'login/'

    def get(self, request):
        return render(request, self.template) 

class Login(View):
    template = 'login.html'
    login_url ='login/'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template,{'form': form})
    
    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect(self.request.GET.get('next', '/'))
            return response
        
        else: 
            return render(request,self.template, {'form':form})

def log_out(request):
    logout(request)
    response = redirect('/login/')
    return response
    
class calendar(LoginRequiredMixin, View):
    template = 'calendar.html'
    login_url = '/login'

    def get(self, request):
        meetings = Calendar.list_meetings()
        worker = None
        if request.user.is_authenticated:
            worker = WorkersAPI.get_worker_by_user_id(request.user.id)
        selected = 0
        return render(request, self.template, {'meetings':meetings, 'selected':selected, 'worker':worker}) 





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
        return redirect('interview_summary_page',id_process=id_process)

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

def process_sumary_page(request):
    pass

def recruiter_start_page(request):
    if(request.method=='POST'):
        return  redirect(recruiter_role_page,id_role=request.POST['role'])
    roles=list_candidates_roles()
    return render(request,'recruiter.html',{'roles':roles})

def recruiter_role_page(request,id_role):
    role = Candidates_Role.objects.get(ID=id_role)
    tests_with_processes = tests.return_test(id_role=id_role)
    procesess_without_tests = Recruitment_Process.objects.filter(Stage=1, ID_Candidates_Role=role)
    if(request.method=='POST'):
        if(request.POST['form_type']=='addtest'):
            return redirect(add_tests_page,id_role=id_role)
        if(request.POST['form_type']=='startinterview'):
            return redirect(choose_interview_candidate,id_role=id_role)

    return render(request,'recruterrole.html',{'role':role,'tests_with_processes':tests_with_processes,
                                                'procesess_without_tests':procesess_without_tests})

def choose_interview_candidate(request,id_role):

    processes = list_processes_by_role_and_stage(id_role=id_role, stage=2)
    if(request.method=='POST'):
        return redirect(add_interview_data_page,id_process=int(request.POST['process']))
    return render(request,'choosecandidate.html',{'processes':processes})


def add_tests_page(request,id_role):

    processes = list_processes_without_tests_by_role(id_role=id_role)
    role = Candidates_Role.objects.get(ID=id_role)
    if(request.method=='POST'):
        if(request.POST['form_type']=='addform'):
            processes_id_list=processes.values_list('ID',flat=True)
            for i in processes_id_list :
                print(request.POST[f'{i}'])
                if request.POST[f'{i}'] != '' :
                    p=int(request.POST[f'{i}'])
                    tests.add_test(id_process=i, id_worker=1, points=p)
        if(request.POST['form_type']=='backform'):
            return redirect(recruiter_start_page)

    return render(request, 'addtests.html',{'processes':processes, 'role':role})


