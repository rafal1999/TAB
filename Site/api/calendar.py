from Site.models import Calendar
from Site import constants


def get_meeting(meeting_id):
    return Calendar.objects.get(pk=meeting_id)

def add_meeting(date, desc:str, meeting_type:str, worker_ids, recruitment_process_id):
    Calendar.objects.create(Meeting_date=date, Description=desc, Cancel_reason="", Meeting_type=meeting_type, Meeting_status='P', 
                            ID_Workers=worker_ids, ID_Recruitment_Process=recruitment_process_id)

def edit_meeting(meeting_id, date, desc:str, meeting_type:str, worker_ids, recruitment_process_id):
    meeting = Calendar.objects.get(pk=meeting_id)
    meeting.Meeting_date=date
    meeting.Description=desc
    meeting.Meeting_type=meeting_type
    meeting.ID_Workers=worker_ids
    meeting.ID_Recruitment_Process=recruitment_process_id
    meeting.Meeting_status = constants.MEETING_STATUS_PLANNED
    meeting.save()

def delete_meeting(meeting_id):
    Calendar.objects.filter(pk=meeting_id).delete()

def confirm_meeting(meeting_id):
    meeting = Calendar.objects.get(pk=meeting_id)
    meeting.Cancel_reason = ""
    meeting.Meeting_status = constants.MEETING_STATUS_CONFIRMED
    meeting.save()

def cancel_meeting(meetingId, reason:str):
    meeting = Calendar.objects.get(pk=meetingId)
    meeting.Cancel_reason = reason
    meeting.Meeting_status = constants.MEETING_STATUS_CANCELLED
    meeting.save()

def uncancel_meeting(meeting_id):
    meeting = Calendar.objects.get(pk=meeting_id)
    meeting.Cancel_reason = ""
    meeting.Meeting_status = constants.MEETING_STATUS_PLANNED
    meeting.save()

def list_meetings():
    return Calendar.objects.all()