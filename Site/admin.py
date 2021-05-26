from django.contrib import admin
from .models        import Workers, Workers_Role, Candidates, Candidates_Role, Tests, Calendar, Recruitment_Meetings

# Register your models here.

class Workers_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Workers._meta.fields]

class Workers_Role_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Workers_Role._meta.fields]

class Candidates_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Candidates._meta.fields]

class Candidates_Role_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Candidates_Role._meta.fields]

class Tests_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Tests._meta.fields]


class Recruitment_Meetings_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Recruitment_Meetings._meta.fields]


class Calendar_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Calendar._meta.fields]


admin.site.register(Workers,Workers_Admin)
admin.site.register(Workers_Role,Workers_Role_Admin)
admin.site.register(Candidates,Candidates_Admin)
admin.site.register(Candidates_Role,Candidates_Role_Admin)
admin.site.register(Tests,Tests_Admin)
admin.site.register(Calendar,Calendar_Admin)
admin.site.register(Recruitment_Meetings,Recruitment_Meetings_Admin)