from django.db import models

class Candidates_Role(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(default="")
    
    class Meta:
        verbose_name = 'Candidate role'
        verbose_name_plural = 'Candidates roles'

class Candidates(models.Model): #TODO zmienić klucz obcy do Ról kandydatów 
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(default="",null=True)
    Surname = models.TextField(default="",null=True)
    Birthdate = models.DateField(auto_now=False, auto_now_add=False)
    Application_date = models.DateField(auto_now=False, auto_now_add=True)
    Phone_number=models.CharField(max_length=13, null=True) # istnije takie cos jak phone number 
    Sex = models.CharField(max_length=1, null=True)
    Email_address = models.EmailField(max_length=50,null=True)
    CV= models.TextField(default="")
    Motivation_letter = models.TextField(default="")
    Stage = models.CharField(max_length=1,default='1') #!
    Hired = models.CharField(max_length=1,default='P') # T - zatrudniony N -niezatrudniony P - in proces 
    ID_Candidates_Role = models.ForeignKey('Candidates_Role',default=None,null=True, on_delete= models.SET_NULL)  
    # CV= models.FilePathField(unique=True,path=None, match=None, recursive=recursive, max_length=200)
    def __str__(self): #musi być __str__ bo inaczej nie działa tylko wyświetla niapis że obiekt jest 
        return self.Name
    def __str__(self):
        return self.Surname
    def __str__(self):
        return self.Application_date
    def __str__(self):
        return self.Birthdate
    def __str__(self):
        return self.Phone_number
    
    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

class Workers_Role(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(null=True,unique=True,max_length=40,verbose_name='Role')

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Workers roles'

    def __str__(self): #konieczne jeśli w django admin chemy wybierać po nazwie roli a nie Role_object (1..n)
        return self.Name
    
class Workers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(default="",null=True, max_length=25)
    Surname = models.CharField(default="",null=True, max_length=25)
    Birthdate = models.DateField(auto_now=False, auto_now_add=False,null=True)
    Login = models.CharField(max_length=32,null=True)
    Password = models.CharField(max_length=32,null=False,default="")
    Email_address = models.EmailField(max_length=50,null=True)
    ID_Workers_Role = models.ForeignKey("Workers_Role", default=None, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'Workers'

class Tests(models.Model):
    ID = models.AutoField(primary_key=True)
    #Name = models.TextField(default="",unique=True) można by w sumie dodać nazwę testu W przypadku gdy połaczymy test bezposrednio z kandeydatem i roloa nie muimy nadwać nazwy bo test bedze przypisany do roli i kandydata
    Points = models.DecimalField(max_digits = 5, decimal_places = 2)
    ID_Candidates_Role = models.ForeignKey('Candidates_Role',default=None,null=False, on_delete= models.CASCADE)
    # ID_Candidates = models.ForeignKey('Candidates',default=None,null=False, on_delete= models.CASCADE)
    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'Tests'

class Recruitment_Meetings(models.Model):
    ID = models.AutoField(primary_key=True)
    Hard_skills = models.TextField(default="",null=True)
    Soft_skills = models.TextField(default="",null=True)
    Grade = models.IntegerField()
    Notes = models.TextField(default="",null=True)

    class Meta:
        verbose_name = 'meeting'
        verbose_name_plural = 'Recruitment meetings'

class Calendar(models.Model):
    ID = models.AutoField(primary_key=True)
    Meeting_date = models.DateField(auto_now=False, auto_now_add=False)
    Description = models.TextField(default="",null=True)
    Stage = models.CharField(max_length=1,default='1')
    Workers_ID_Worker = models.ForeignKey("Workers", default=None, null=True, on_delete=models.SET_NULL)
    Candidates_ID_Candidate = models.ForeignKey("Candidates", default=None, null=True, on_delete=models.SET_NULL)
    Tests_ID = models.ForeignKey("Tests", default=None, null=True, on_delete=models.SET_NULL)
    Recruitment_Meetings_ID = models.ForeignKey("Recruitment_Meetings", default=None, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'Calendar'

