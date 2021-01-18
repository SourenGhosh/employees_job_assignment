from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms import inlineformset_factory
from job_manage.models import Verticals, Projects, Employees, Jobs, Joballocation
from .forms import JobForm
from .filters import JobFilter
# Create your views here.

def indexView(request):
    employee=Employees.objects.all()
    allocation = Joballocation.objects.all()
    myFilter = JobFilter(request.GET, queryset=allocation)
    allocation = myFilter.qs
    context = {'employee': employee, 'allocation': allocation, 'myFilter': myFilter}
    return render(request, "job_manage/manage1.html", context)


def indexView1(request, pk_test):
    employee=Employees.objects.get(id=pk_test)
    allocation = employee.joballocation_set.all()
    myFilter = JobFilter(request.GET, queryset=allocation)
    allocation = myFilter.qs
    context = {'employee': employee, 'allocation': allocation, 'myFilter': myFilter}
    return render(request, "job_manage/manage1.html", context)


'''
def manage_data1(request):
    if request.is_ajax and request.method == "POST":
        employee_res = request.POST['employee_htm']
        job_res = request.POST['job_htm']
        employee_and_job_list.object.create(employee=employee_res, job_type=job_res)
        form = manage_form(request.POST)

        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance,])
            return JsonResponse({"instance": ser_instance}, status=200)
            return HttpResponse("saved")

        else:
            return JsonResponse({"error": ""}, status=400)
'''

def updateJoballocation(request, pk):
    allocation_update = Joballocation.objects.get(id=pk)
    form = JobForm(instance=allocation_update)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=allocation_update)
        if form.is_valid():
            form.save()
            return redirect('indexView1', pk)
    context = {'form': form}
    return render(request, 'job_manage/job_update.html', context)
