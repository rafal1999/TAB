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
from Site.api.candidates        import list_candidates, add_candidate
import Site.api.workers         as WorkersAPI
import Site.api.calendar        as Calendar
from Site.models                import Workers, Recruitment_Process 
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