from django.contrib import admin
from .models import TblProjectAttraction,TblProject,TblCity,TblAttraction,TblMember
# Register your models here.

admin.site.register(TblProject)
admin.site.register(TblProjectAttraction)
admin.site.register(TblCity)
admin.site.register(TblAttraction)
admin.site.register(TblMember)