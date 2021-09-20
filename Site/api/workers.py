
from Site.models                import Candidates, Workers, Workers_Role
from datetime                   import date


def add_worker(name:str,surname:str,birthday,worker_role:str):
    if worker_role=="":
        Workers.objects.create(Name=name,Surname=surname,Birthdate=birthday,ID_Workers_Role=None)
    else:
        role_obj, exist= Workers_Role.objects.get_or_create(Name=worker_role)
        Workers.objects.create(Name=name,Surname=surname,Birthdate=birthday,ID_Workers_Role=role_obj)

def list_workers():
    return Workers.objects.all()

def list_workers_except(role_id):
    return Workers.objects.all().exclude(ID_Workers_Role = role_id)

def get_worker(id):
    return Workers.objects.get(pk=id)

def get_worker_by_name(name:str, surname:str):
    return Workers.objects.filter(Name=name, Surname=surname).first()

def get_worker_by_user_id(id):
    return Workers.objects.filter(ID_User=id).first()

def delete_worker():
    pass

def search_workers():
    pass