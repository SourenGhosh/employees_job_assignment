from django.contrib import admin
from django import forms
from job_manage.models import Verticals, Projects, Employees, Jobs, Joballocation
# Register your models here.
admin.site.register(Verticals)
admin.site.register(Projects)
admin.site.register(Employees)
admin.site.register(Jobs)
admin.site.register(Joballocation)
