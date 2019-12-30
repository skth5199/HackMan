from django.contrib import admin
from .models import *
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('username','name1','name2','name3','name4', 'phone' ,'count')

class SubAdmin(admin.ModelAdmin):
    list_display = ('username','sublink')

class WifiAdmin(admin.ModelAdmin):
    list_display = ('username','pawd')

class CafeAdmin(admin.ModelAdmin):
    list_display = ('food','category','brand','quantity','time')

class JudgeAdmin(admin.ModelAdmin):
    list_display = ('username','score','tname')


admin.site.register(team, TeamAdmin)
admin.site.register(submissions, SubAdmin)
admin.site.register(wifi, WifiAdmin)
admin.site.register(cafe, CafeAdmin)
admin.site.register(judges, JudgeAdmin)


