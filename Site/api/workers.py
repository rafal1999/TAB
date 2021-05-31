
from Site.models                import Candidates, Workers, Workers_Role 
from datetime                   import date

#TODO korekta dużych liter 
def add_worker(name:str,surname:str,birthday,worker_role:str):
    if worker_role=="":
        Workers.objects.create(Name=name,Surname=surname,Birthdate=birthday,ID_Workers_Role=None)
    else:
        role_obj, exist= Workers_Role.objects.get_or_create(Name=worker_role)
        Workers.objects.create(Name=name,Surname=surname,Birthdate=birthday,ID_Workers_Role=role_obj)

def delete_worker():
    pass

def search_workers():
    pass