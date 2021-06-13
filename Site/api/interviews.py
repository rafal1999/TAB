from Site.models import Recruitment_Meetings


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