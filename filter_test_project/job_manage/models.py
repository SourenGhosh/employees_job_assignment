from django.db import models
from datetime import datetime
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.
class Verticals(models.Model):
    vert = models.CharField(max_length=100)

    def __str__(self):
        return self.vert


class Projects(models.Model):
    vert = models.ForeignKey(Verticals, on_delete = models.CASCADE)
    proj = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.proj

class Employees(models.Model):
    employee_name = models.CharField(max_length=100, null= True, blank=True)


    def __str__(self):
        return self.employee_name

class Jobs(models.Model):
    vert = models.ForeignKey(Verticals, on_delete = models.CASCADE, null=True)
    proj = ChainedForeignKey(Projects, chained_field="vert", chained_model_field="vert", show_all=False, auto_choose=True, sort=True)
    job_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.job_name

   
class Joballocation(models.Model):
    employees = models.ForeignKey('Employees', on_delete = models.CASCADE)
    job_name = models.ForeignKey('Jobs', on_delete=models.CASCADE, null= True)
    scheduled_date = models.DateField(null=True, blank=True)
    shift_1_start_time = models.TimeField(null=True, blank=True)
    shift_1_end_time =  models.TimeField(null=True, blank=True)
    shift_1_job = models.CharField(max_length=100, null=True, blank = True)
    shift_2_start_time = models.TimeField(null=True, blank=True)
    shift_2_end_time =  models.TimeField(null=True, blank=True)
    shift_2_job = models.CharField(max_length=100, null=True, blank = True)
    shift_3_start_time = models.TimeField(null=True, blank=True)
    shift_3_end_time =  models.TimeField(null=True, blank=True)
    shift_3_job = models.CharField(max_length=100, null=True, blank = True)
    shift_4_start_time = models.TimeField(null=True, blank=True)
    shift_4_end_time =  models.TimeField(null=True, blank=True)
    shift_4_job = models.CharField(max_length=100, null=True, blank = True)
    shift_5_start_time = models.TimeField(null=True, blank=True)
    shift_5_end_time =  models.TimeField(null=True, blank=True)
    shift_5_job = models.CharField(max_length=100, null=True, blank = True)
    shift_6_start_time = models.TimeField(null=True, blank=True)
    shift_6_end_time =  models.TimeField(null=True, blank=True)
    shift_6_job = models.CharField(max_length=100, null=True, blank = True)
    shift_7_start_time = models.TimeField(null=True, blank=True)
    shift_7_end_time =  models.TimeField(null=True, blank=True)
    shift_7_job = models.CharField(max_length=100, null=True, blank = True)
    shift_8_start_time = models.TimeField(null=True, blank=True)
    shift_8_end_time =  models.TimeField(null=True, blank=True)
    shift_8_job = models.CharField(max_length=100, null=True, blank = True)
    shift_9_start_time = models.TimeField(null=True, blank=True)
    shift_9_end_time =  models.TimeField(null=True, blank=True)
    shift_9_job = models.CharField(max_length=100, null=True, blank = True)
    shift_10_start_time = models.TimeField(null=True, blank=True)
    shift_10_end_time =  models.TimeField(null=True, blank=True)
    shift_10_job = models.CharField(max_length=100, null=True, blank = True)

