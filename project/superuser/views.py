import csv
import io
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
import numpy
import pandas as pd
from django.shortcuts import render

from unicodedata import name
from unittest import result
from django.shortcuts import render
import pandas as pd
import csv, io
from django.shortcuts import render
from django.contrib import messages
from pymysql import NULL, Timestamp

import statsmodels.api as sm
from datetime import date, datetime
import math
from itertools import groupby
from operator import itemgetter
from django.shortcuts import render, redirect

from authentification.decorators import allowed_superuser
from authentification.views import dataSuperuser
from .models import UserModel
from .forms import UserForm
from django.db.models import Q


# Create your views here.
@allowed_superuser(allowed_roles=dataSuperuser)
def dataUser(request):
    dataU = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))
    countDataA = UserModel.objects.all().filter(is_staff = 1).count()
    countDataP = UserModel.objects.all().filter(Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4)).count()
    countDataAM = UserModel.objects.all().filter(is_staff = 1, gender = 'L').count()
    countDataAF = UserModel.objects.all().filter(is_staff = 1, gender = 'P').count()
    data = {
        'dataU' : dataU,
        'countDataA' : countDataA,
        'countDataP' : countDataP,
        'countDataAM' : countDataAM,
        'countDataAF' : countDataAF,
    }
    return render(request, 'superuser.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def editUser(request, id):
    dataU = UserModel.objects.get(id=id)
    current_user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance = dataU)
        if form.is_valid():
            form.save()
            return redirect("/superuser")
        pass
    return render(request,"editdatauser.html",{'dataU':dataU})

def profileCompany (request):
    return render(request,'profilecompany.html')





