from django.shortcuts           import redirect, render
from django.http                import HttpResponse  
# from django.db.models.functions import Concat 
# from django.db.models           import F, Value
from Site.models                import Candidates, Workers, Workers_Role 
from datetime                   import date, datetime
from Site.api.workers           import add_worker
from django.views               import View
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth        import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from Site.api.candidates        import list_candidates, add_candidate
import Site.api.calendar        as Calendar
from Site.models                import Workers, Recruitment_Process 
from django                     import forms               
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
    if request.method=="POST":
        myDate = request.POST['date']
        
        Calendar.add_meeting(date=datetime.strptime(myDate, "%d/%m/%Y %H:%M"), desc=request.POST['meeting_desc'], 
                    meeting_type=request.POST['meeting_type'], worker_ids=Workers.objects.all()[0], recruitment_process_id=Recruitment_Process.objects.all()[0])
        response = redirect('/calendar/')
        return response
    f = forms.DateField()
    f2 = forms.ChoiceField()
    return render(request, 'calendarcreate.html')

def edit_meeting(request, id):
    if request.method=="POST":
        myDate = request.POST['date']
        
        Calendar.edit_meeting(meeting_id = id, date=datetime.strptime(myDate, "%d/%m/%Y %H:%M"), desc=request.POST['meeting_desc'], 
                    meeting_type=request.POST['meeting_type'], worker_ids=Workers.objects.all()[0], recruitment_process_id=Recruitment_Process.objects.all()[0])
    meeting = Calendar.get_meeting(id)
    f = forms.DateField()
    return render(request, 'calendaredit.html', {'meeting':meeting})

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
        return render(request, self.template)


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
        if user is  None:
            login(request, user)
            return render(request, self.template)
        
        else: 
            return render(request,self.template, {'form':form})

class calendar(View):
    template = 'calendar.html'
    login_url = 'login/'

    def get(self, request):
        meetings = Calendar.list_meetings()
        selected = 0
        return render(request, self.template, {'meetings':meetings, 'selected':selected}) 