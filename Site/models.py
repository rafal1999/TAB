from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from enum import Enum

SEX_FEMALE = 'F'
SEX_MALE = 'M'
SEX_UNSURE = 'U'

SEX_OPTIONS = (
    (SEX_UNSURE, 'Unsure'),
    (SEX_FEMALE, 'Female'),
    (SEX_MALE, 'Male'),
    )

class sex_choice(Enum):
    Man = 'Man'
    Woman = 'Woman'

STAGE_ZERO   = '0' # kandydat zgłoszony
STAGE_FIRST  = '1' # test napisany               #TODO może zmienić na inty w bazie łatwiej sortować??
STAGE_SECOND = '2' # po rozmowie rekrutacyjnej
STAGE_THIRD  = '3' # po rozmowie finalnej po której dostaje odp tak/nie 

STAGE_OPTIONS = (     #TODO W miejsca 0,1,2 nadać opisy jakie by były fajne (to co ma się wyświetlać) 
    (STAGE_ZERO, '0'),      #!
    (STAGE_FIRST, '1'),     #!
    (STAGE_SECOND, '2'),    #!
    (STAGE_THIRD, '3')      #!
    )
class stage_choice(Enum): #TODO można zmienić nazwy na troche inne etapy albo juz wgl kolejna tabela do entapów 
    first = 'first'
    second = 'second'
    third = 'third'

HIRED_YES        = 'Y'
HIRED_NO         = 'N'
HIRED_IN_PROCESS = 'P'

HIRED_OPTIONS = (
    (STAGE_SECOND, 'In process'),
    (HIRED_IN_PROCESS, 'Yes'),
    (HIRED_NO, 'No'),
    )

PRESENT_YES =  'Y'
PRESENT_NO = 'N'
PRESENT_UNKNOWN = 'U'

PRESENT_OPTIONS = (
    (PRESENT_UNKNOWN, 'Unknown'),
    (PRESENT_YES, 'Yes'),
    (PRESENT_NO, 'No'),
)

class hired_choice(Enum):
    in_process = "In process"
    yes = "Yes"
    no = "No"

class Candidates_Role(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(default=None,null=False, max_length=25)
    
    class Meta:
        verbose_name = 'Candidate role'
        verbose_name_plural = 'Candidates roles'

    def __str__(self):
        return self.Name
    

class Candidates(models.Model): #TODO zmienić klucz obcy do Ról kandydatów 
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(default=None,null=False, max_length=25)
    Surname = models.CharField(default=None,null=False, max_length=25)
    Birthdate = models.DateField(auto_now=False, auto_now_add=False)
    Application_date = models.DateField(auto_now=False, auto_now_add=True)
    Phone_number=models.CharField(max_length=13, null=True)
    Sex = models.CharField(max_length=1, null=True,default=None, choices=SEX_OPTIONS)#=[(tag,tag.value) for tag in sex_choice])
    Email_address = models.EmailField(max_length=50,null=True)
    CV= models.TextField(default="")                                                                                #TODO mozliwa zmiana argumentów gdzy dojdzemy do implemetacji cv
    Motivation_letter = models.TextField(default="")                                                                #TODO mozliwa zmiana argumentów gdzy dojdzemy do implementacji
    Stage = models.CharField(max_length=1,default='',choices=STAGE_OPTIONS)#choices=[(tag,tag.value) for tag in stage_choice]) 
    Hired = models.CharField(max_length=10,default='',choices=HIRED_OPTIONS)# choices=[(tag,tag.value) for tag in hired_choice])
    ID_Candidates_Role = models.ForeignKey('Candidates_Role',default=None,null=True, on_delete= models.SET_NULL)  
    # CV_v2= models.FilePathField(unique=True,path=None, match=None,max_length=200) #TODO trzeba przetestować bardziej wnikliwie 
    
    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'
    
    def __str__(self):
        return self.Name + self.Surname
    

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
    Password = models.CharField(max_length=32,null=False,default="") #TODO password bo widac hasło w
    Email_address = models.EmailField(max_length=50,null=True)
    ID_Workers_Role = models.ForeignKey("Workers_Role", default=None, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'Workers'
    
    def __str__(self):
        return self.Name +' '+self.Surname
    

class Tests(models.Model):
    ID = models.AutoField(primary_key=True)
    #Name = models.TextField(default="",unique=True) można by w sumie dodać nazwę testu W przypadku gdy połaczymy test bezposrednio z kandeydatem i roloa nie muimy nadwać nazwy bo test bedze przypisany do roli i kandydata
    Points = models.DecimalField(max_digits = 5, decimal_places = 2,validators=[MaxValueValidator(100),MinValueValidator(0)],null=True )
    ID_Candidates_Role = models.ForeignKey('Candidates_Role',default=None,null=False,verbose_name='Role', on_delete= models.CASCADE)
    # ID_Candidates = models.ForeignKey('Candidates',default=None,null=False, on_delete= models.CASCADE)
    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'Tests'

class Recruitment_Meetings(models.Model):
    ID = models.AutoField(primary_key=True)
    Hard_skills = models.TextField(default="",null=True)
    Soft_skills = models.TextField(default="",null=True)
    Grade = models.DecimalField(max_digits = 2, decimal_places = 0, validators=[MaxValueValidator(10),MinValueValidator(0)])
    Notes = models.TextField(default="",null=True)

    class Meta:
        verbose_name = 'meeting'
        verbose_name_plural = 'Recruitment meetings'

class Calendar(models.Model):
    ID = models.AutoField(primary_key=True)
    Meeting_date = models.DateField(auto_now=False, auto_now_add=False)
    Description = models.TextField(default="",null=True)
    # Stage = models.CharField(max_length=1,default='1') USELESS!!!! w kandydatach już mamy stage 
    Workers_ID_Worker = models.ForeignKey("Workers", default=None,verbose_name='Worker' ,null=True, on_delete=models.SET_NULL)
    Candidates_ID_Candidate = models.ForeignKey("Candidates", default=None, null=True, verbose_name='Candidate' ,on_delete=models.SET_NULL)
    Tests_ID = models.ForeignKey("Tests", default=None, null=True,verbose_name= "Test", on_delete=models.SET_NULL)
    Recruitment_Meetings_ID = models.ForeignKey("Recruitment_Meetings", default="", verbose_name='Recruitment meeting', null=True, on_delete=models.SET_NULL)
    Worker_present = models.CharField(max_length=1,default=PRESENT_UNKNOWN,choices=PRESENT_OPTIONS, verbose_name='Worker present')
    Candidate_present = models.CharField(max_length=1,default=PRESENT_UNKNOWN,choices=PRESENT_OPTIONS, verbose_name='Candidate present')

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'Calendar'

