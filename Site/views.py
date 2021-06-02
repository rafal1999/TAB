from django.shortcuts           import render
from django.http                import HttpResponse  
# from django.db.models.functions import Concat 
# from django.db.models           import F, Value
from Site.models                import Candidates, Workers, Workers_Role 
from datetime                   import date
from Site.api.workers           import add_worker
from django.views               import View
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth        import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
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

class Qbranchtest(View):
    template = 'qbranchtest.html'
    login_url = 'login/'

    def post(self, request):
        y=int(request.POST['worker_year_of_birth'])
        m=int(request.POST['worker_month_of_birth'])
        d=int(request.POST['worker_month_of_birth'])
        worker_role=request.POST['worker_role']
        workers = Workers.objects.all()
        add_worker(name=request.POST['worker_name'], surname=request.POST['worker_surname'], birthday=date(y,m,d), worker_role=worker_role)
        return render(request,'testworkers.html', {'workers':workers})


    def get(self, request):
        workers = Workers.objects.all()
        return render(request, self.template, {'workers':workers})


class Home(View):
    template = 'home.html'
    login_url = 'login/'

    def get(self, request):
        return render(request, self.template)


class Index(LoginRequiredMixin,View):
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
