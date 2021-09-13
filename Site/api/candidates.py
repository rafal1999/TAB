from Site.models import Candidates, Candidates_Role, Recruitment_Process






def add_candidate(name:str,surname:str,birthday,phone_number,sex,email,cv,
                    motivation_letter,hired):
    
    Candidates.objects.create(Name=name,Surname=surname,Birthdate=birthday,
                                Phone_number=phone_number,Sex=sex,CV=cv,
                                Motivation_letter=motivation_letter,Hired=hired)

def edit_candidate(id,name,surname,birthday,phone_number,sex,email,cv,
                    motivation_letter):
    Candidates.objects.filter(ID=id).update(Name=name,Surname=surname,Birthdate=birthday,
                                Phone_number=phone_number,Sex=sex,CV=cv,
                                Motivation_letter=motivation_letter)



def list_candidates():
    return Candidates.objects.all() 

def list_candidates_roles():
    return Candidates_Role.objects.all()

def delete_candidate(id):
    Candidates.objects.filter(pk=id).delete()

def add_process(id_candidate, id_role):
    Recruitment_Process.objects.create(ID_Candidates=Candidates.objects.get(ID=id_candidate),ID_Candidates_Role=Candidates_Role.objects.get(ID=id_role),Stage=1)

def list_processes():
    return Recruitment_Process.objects.all()

def get_process(id):
    return Recruitment_Process.objects.get(pk=id)

