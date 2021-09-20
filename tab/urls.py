"""tab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Site import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('testcalendar/', views.test_calendar_page, name='testcalendar'),
    path('index/', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('interview/<int:id_process>', views.add_interview_data_page,name='add_interview_data_page'),
    path('interview/interview_summary/<int:id_process>', views.interview_summary_page,name='interview_summary_page'),
    path('assistant/', views.assistant_page, name='assistant_page'),
    path('assistant/editcandidate/<int:id_candidate>', views.edit_candidate_page,name='edit_candidate_page'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('calendar/', views.calendar.as_view(), name='calendar'),
    path('calendar/edit/<int:id>', views.edit_meeting, name='editmeeting'),
    path('calendar/confirm/<int:id>', views.confirm_meeting, name='confirmmeeting'),
    path('calendar/cancel/<int:id>/<str:desc>', views.cancel_meeting, name='cancelmeeting'),
    path('calendar/delete/<int:id>', views.delete_meeting, name='deletemeeting'),
    path('calendar/create/', views.create_meeting, name='createmeeting'),
    path('interview/<int:id_process>', views.add_interview_data_page,name='add_interview_data_page'),
    path('interview/interview_summary/<int:id_process>', views.interview_summary_page,name='interview_summary_page'),
    path('candidates/editcandidate/<int:id_candidate>', views.edit_candidate_page,name='edit_candidate_page'),
    path('candidates/addcandidate/',views.add_candidate_page,name='add_candidate_page'),
    path('candidates/addprocess/<int:id_candidate>',views.add_process_page,name='add_process_page'),
    path('candidates/delete/<int:id>', views.delete_candidate, name='deletecandidate'),
    path('candidates/hire/<int:id>', views.hire_candidate, name='hirecandidate'),
    path('candidates/donthire/<int:id>', views.dont_hire_candidate, name='hirecandidate'),
    path('candidates/', views.candidates.as_view(), name='candidates'),
    path('recruiter/',views.recruiter_start_page,name='recruiter_start_page'),
    path('recruiter/<int:id_role>',views.recruiter_role_page,name='recruiter_role_page'),
    path('recruiter/addtests/<int:id_process>',views.add_tests_page,name='add_tests_page'),
    path('recruiter/choosecandidate/<int:id_role>',views.choose_interview_candidate,name='add_tests_page'),
    path('supervisor/',views.supervisor_page, name='supervisor_page'),
    path('interviews/', views.interviews.as_view(), name='interviews'),
]


