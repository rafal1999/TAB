from Site.models import Candidates, Candidates_Role, Tests, Recruitment_Process






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

def list_processes_by_role(id_role):
    role=Candidates_Role.objects.get(ID=id_role)
    processes=Recruitment_Process.objects.filter(ID_Candidates_Role=role)
    return processes

def list_processes_by_role_and_stage(id_role,stage):
    processes = list_processes_by_role(id_role=id_role)
    processes = processes.filter(Stage=stage)
    return processes

def list_processes_without_tests_by_role(id_role):
    id_processes_with_role = list_processes_by_role(id_role=id_role).values_list('ID',flat=True)
    id_all_processes_with_tests = Tests.objects.values_list('ID_Recruitment_Process',flat=True)
    id_processes_with_role_without_tests = [item for item in  id_processes_with_role if 
                                            item not in id_all_processes_with_tests]
    print(id_processes_with_role_without_tests)
    processes= Recruitment_Process.objects.filter(ID__in=id_processes_with_role_without_tests)
    return processes

def add_process(id_candidate, id_role):
    process=Recruitment_Process.objects.filter(ID_Candidates=Candidates.objects.get(ID=id_candidate), ID_Candidates_Role= Candidates_Role.objects.get(ID=id_role))
    if (process.exists() == False):
        Recruitment_Process.objects.create(ID_Candidates=Candidates.objects.get(ID=id_candidate),
                                        ID_Candidates_Role=Candidates_Role.objects.get(ID=id_role),Stage=1)
