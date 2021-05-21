from django.contrib import admin
from .models        import Workers, Workers_Role

# Register your models here.

class Workers_Admin(admin.ModelAdmin):
    list_display = [f.name for f in Workers._meta.fields]



admin.site.register(Workers,Workers_Admin)