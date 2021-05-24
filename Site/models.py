from django.db import models

class Candidates_Role(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(default="")

class Candidates(models.Model):
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
    
class Workers_Role(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(default="",unique=True)

    def __str__(self):
        return self.Name
    
class Workers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(default="",null=True)
    Surname = models.TextField(default="",null=True)
    Birthdate = models.DateField(auto_now=False, auto_now_add=False,null=True)
    Login = models.CharField(max_length=32,null=True)
    Password = models.CharField(max_length=32,null=False,default="")
    Email_address = models.EmailField(max_length=50,null=True)
    ID_Workers_Role = models.ForeignKey("Workers_Role", default=None, null=True, on_delete=models.SET_NULL)

class Tests(models.Model):
    ID = models.AutoField(primary_key=True)
    #Name = models.TextField(default="",unique=True) można by w sumie dodać nazwę testu
    Points = models.DecimalField(max_digits = 5, decimal_places = 2)

class Recruitment_Meetings(models.Model):
    ID = models.AutoField(primary_key=True)
    Hard_skills = models.TextField(default="",null=True)
    Soft_skills = models.TextField(default="",null=True)
    Grade = models.IntegerField()
    Notes = models.TextField(default="",null=True)

class Calendar(models.Model):
    ID = models.AutoField(primary_key=True)
    Meeting_date = models.DateField(auto_now=False, auto_now_add=False)
    Description = models.TextField(default="",null=True)
    Stage = models.CharField(max_length=1,default='1')
    Workers_ID_Worker = models.ForeignKey("Workers", default=None, null=True, on_delete=models.SET_NULL)
    Candidates_ID_Candidate = models.ForeignKey("Candidates", default=None, null=True, on_delete=models.SET_NULL)
    Tests_ID = models.ForeignKey("Tests", default=None, null=True, on_delete=models.SET_NULL)
    Recruitment_Meetings_ID = models.ForeignKey("Recruitment_Meetings", default=None, null=True, on_delete=models.SET_NULL)

