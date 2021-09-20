from Site.models 				import Tests, Recruitment_Process, Workers
from Site.api.candidates 	 	import list_processes_by_role

def add_test(id_process, id_worker,points):


	Tests.objects.create(ID_Recruitment_Process=Recruitment_Process.objects.get(ID=id_process),
						ID_Workers=Workers.objects.get(ID=id_worker),Points=points)
	Recruitment_Process.objects.filter(ID=id_process).update(Stage=2)


def return_test(id_role):

	tests=Tests.objects.filter(ID_Recruitment_Process__in=Recruitment_Process.objects.filter(
							ID_Candidates_Role=id_role).values_list('ID',flat=True))
	return tests

def list_tests():
	return Tests.objects.all()