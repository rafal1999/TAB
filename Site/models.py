from django.contrib.auth.models import User
from django.db              import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms           import ModelForm, PasswordInput
from Site import constants


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
    Sex = models.CharField(max_length=1, null=True,default=None, choices=constants.SEX_OPTIONS)#=[(tag,tag.value) for tag in sex_choice])
    Email_address = models.EmailField(max_length=50,null=True)
    CV= models.TextField(default="")                                                                                #TODO mozliwa zmiana argumentów gdzy dojdzemy do implemetacji cv
    Motivation_letter = models.TextField(default="")                                                                #TODO mozliwa zmiana argumentów gdzy dojdzemy do implementacji
    Hired = models.CharField(max_length=10,default='',choices=constants.HIRED_OPTIONS)# choices=[(tag,tag.value) for tag in hired_choice])
    
    # CV_v2= models.FilePathField(unique=True,path=None, match=None,max_length=200) #TODO trzeba przetestować bardziej wnikliwie 
    
    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'
    
    def __str__(self):
        return self.Name +' '+ self.Surname
    
class Recruitment_Process(models.Model):
    ID = models.AutoField(primary_key=True)
    Stage = models.CharField(max_length=1,default='',choices=constants.STAGE_OPTIONS)#choices=[(tag,tag.value) for tag in stage_choice]) 
    ID_Candidates_Role = models.ForeignKey('Candidates_Role',default=None,null=True,verbose_name='Candidate role', on_delete= models.SET_NULL)
    ID_Candidates = models.ForeignKey("Candidates", default=None, null=True, verbose_name='Candidate' ,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Recruitment process'

    def __str__(self):
        return str(self.ID_Candidates.Name + ' ' + self.ID_Candidates.Surname + ' ' + self.ID_Candidates_Role.Name)


class Workers_Role(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(null=True,unique=True,max_length=40,verbose_name='Role')

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Workers roles'

    def __str__(self): 
        return self.Name

class Workers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(default="",null=True, max_length=25)
    Surname = models.CharField(default="",null=True, max_length=25)
    Birthdate = models.DateField(auto_now=False, auto_now_add=False,null=True)
    Email_address = models.EmailField(max_length=50,null=True)
    ID_Workers_Role = models.ForeignKey("Workers_Role", default=None, null=True, verbose_name='Role' , on_delete=models.SET_NULL)
    ID_User = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'Workers'
    
    def __str__(self):
        return self.Name +' '+self.Surname
    


class Tests(models.Model):
    ID = models.AutoField(primary_key=True)
    Points = models.DecimalField(max_digits = 5, decimal_places = 2,validators=[MaxValueValidator(100),MinValueValidator(0)],null=True )
    Check_out_date = models.DateField(auto_now=False, auto_now_add=True) 
    ID_Recruitment_Process = models.OneToOneField("Recruitment_Process", default=None, null=True, verbose_name='Candidate and his role' ,on_delete=models.SET_NULL)
    ID_Workers =  models.ForeignKey("Workers", default=None, null=True,verbose_name="Worker" ,on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'Tests'

class Recruitment_Meetings(models.Model):
    ID = models.AutoField(primary_key=True)
    Hard_skills = models.TextField(default="",null=True)
    Soft_skills = models.TextField(default="",null=True)
    Grade = models.DecimalField(max_digits = 2, decimal_places = 0, validators=[MaxValueValidator(10),MinValueValidator(0)])
    Notes = models.TextField(default="",null=True)
    Date = models.DateField(auto_now=False, auto_now_add=True)
    ID_Recruitment_Process = models.ForeignKey("Recruitment_Process", default=None, null=True, verbose_name='Recruitment process' ,on_delete=models.SET_NULL)
    ID_Workers = models.ForeignKey("Workers", default=None,verbose_name='Worker' ,null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = 'meeting'
        verbose_name_plural = 'Recruitment meetings'

class Calendar(models.Model):
    ID = models.AutoField(primary_key=True)
    Meeting_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    Description = models.TextField(default="",null=True)
    Cancel_reason = models.TextField(default="", null=True)
    Meeting_type = models.CharField(max_length=1, null=True,default=None, choices=constants.MEETING_TYPE_OPTIONS)
    Meeting_status = models.CharField(max_length=1, null=False,default='U', choices=constants.MEETING_STATUS_OPTIONS)
    ID_Workers = models.ForeignKey("Workers", default=None,verbose_name='Worker', null=True, on_delete=models.SET_NULL)
    ID_Recruitment_Process = models.ForeignKey("Recruitment_Process", default=None, null=True, verbose_name='Recruitment process', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'Calendar'

        

class Workers_Form(ModelForm):

   class Meta:
        model = Workers
        widgets = {
            'Password': PasswordInput(),
        }
        fields = [f.name for f in Workers._meta.fields]