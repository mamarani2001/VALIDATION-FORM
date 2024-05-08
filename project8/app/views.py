from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.


def insert_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method == 'POST':
        SFO=SchoolForm(request.POST)
        if SFO.is_valid():
            sname=SFO.cleaned_data.get('sname')
            sprincipal=SFO.cleaned_data.get('sprincipal')
            saddress = SFO.cleaned_data.get('saddress')
            SO=School(sname=sname, saddress=saddress, sprincipal=sprincipal)
            SO.save()
            return HttpResponse('Insert_School is done successfully')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_school.html',d)