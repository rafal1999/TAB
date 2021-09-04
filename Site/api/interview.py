
from Site.models import Candidates, Recruitment_Meetings, Recruitment_Process, Workers


#TO DO zamisat worker id wpisz dane z sesji
def add_interview_data(id_process,id_worker, hard_skils, soft_skils, grade, notes):
    Recruitment_Meetings.objects.create(ID_Recruitment_Process =Recruitment_Process.objects.get(ID=id_process),
                                        ID_Workers =Workers.objects.get(ID=id_worker)
                                        ,Hard_skills=hard_skils, Soft_skills=soft_skils,
                                        Grade=grade, Notes=notes)



def check_if_interview_took_place(id_process):
    
    if Recruitment_Meetings.objects.filter(ID=id_process).exists():
        return True
    else:
        return False