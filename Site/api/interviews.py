from Site.models import Recruitment_Meetings, Candidates, Recruitment_Process, Workers

def add_interview(date, recruitment_process_id, worker_ids):
	Recruitment_Meetings.objects.create(Hard_skills="", Soft_skills="", Grade=0, Notes="", Date=date,
										ID_Recruitment_Process=recruitment_process_id, ID_Workers=worker_ids)

def save_interview(interview_id, hard_skills:str, soft_skills:str, grade, notes:str):
	interview = Recruitment_Meetings.objects.get(pk=interview_id)
	interview.Hard_skills = hard_skills
	interview.Soft_skills = soft_skills
	interview.Grade = grade
	interview.Notes = notes
	interview.save()
	
def delete_interview(interview_id):
    Recruitment_Meetings.objects.filter(pk=interview_id).delete()

def list_interviews():
	return Recruitment_Meetings.objects.all()

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