from Site.models import Candidates






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

def list_best_candidates(amount:int):
    pass

def list_candidates_with_role(role:str):
    pass

def search_candidates():
    pass

def hire_candidate():
    pass

def next_stage():
    pass

def add_test():
    pass

def edit_test():
    pass