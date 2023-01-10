from ast import Is, Str
import csv
import io
from pickle import NONE
from pydoc import stripid
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

from authentification.decorators import allowed_bendahara
from authentification.views import dataUserBenda
from authentification.models import UserModel
from sekretaris.forms import JenisAgendaForm
from .models import IuranModel,IuranRekapModel, UpdateIuranModel , IuranGenerateModel, KeuanganModel
from sekretaris.models import AgendaModel,AbsensiModel, JenisAgendaModel
from ketuawakil.models import AwigModel
from .forms import IuranForm, IuranUpdateForm, KeuanganForm
from django.db.models import Sum

from .models import UserProfileModel
from .forms import UserProfileForm
from django.contrib.auth.models import User

from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import StringIO, BytesIO


# Create your views here.
@allowed_bendahara(allowed_roles=dataUserBenda)
def dashboardUserBendahara(request):
    idLastAgenda = AgendaModel.objects.latest('id_agenda').id_agenda
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    dataABul = AgendaModel.objects.filter(id_jenis_agenda = 1).values()
    dataAPeng = AgendaModel.objects.filter(id_jenis_agenda = 2).values()
    dataAMed = AgendaModel.objects.filter(id_jenis_agenda = 4).values()
    dataAOgoh = AgendaModel.objects.filter(id_jenis_agenda = 5).values()
    dataAHut = AgendaModel.objects.filter(id_jenis_agenda = 6).values()

    # Absensi Bulanan
    arrABul = []
    for i in dataABul:
        arrABul.append(int(i['id_agenda']))
    arrTotalABul = []
    arrTotalHABul = []
    for j in arrABul:
        tempTotalABul = AbsensiModel.objects.filter(id_user = idUser, id_agenda = j).count()
        tempTotalHABul = AbsensiModel.objects.filter(id_user = idUser,id_agenda = j,status_absensi = 2).count()
        arrTotalABul.append(tempTotalABul)
        arrTotalHABul.append(tempTotalHABul)
    totalAbsensiBul = len(arrTotalABul)
    hadirAbsensiBul = arrTotalHABul.count(1)

    # Absensi Pengerampungan
    arrAPeng = []
    for i in dataAPeng:
        arrAPeng.append(int(i['id_agenda']))
    arrTotalAPeng = []
    arrTotalHAPeng = []
    for j in arrAPeng:
        tempTotalAPeng = AbsensiModel.objects.filter(id_user = idUser, id_agenda = j).count()
        tempTotalHAPeng = AbsensiModel.objects.filter(id_user = idUser,id_agenda = j,status_absensi = 2).count()
        arrTotalAPeng.append(tempTotalAPeng)
        arrTotalHAPeng.append(tempTotalHAPeng)
    totalAbsensiPeng = len(arrTotalAPeng)
    hadirAbsensiPeng = arrTotalHAPeng.count(1)

    # Absensi Madelokan
    arrAMed = []
    for i in dataAMed:
        arrAMed.append(int(i['id_agenda']))
    arrTotalAMed = []
    arrTotalHAMed = []
    for j in arrAMed:
        tempTotalAMed = AbsensiModel.objects.filter(id_user = idUser, id_agenda = j).count()
        tempTotalHAMed = AbsensiModel.objects.filter(id_user = idUser,id_agenda = j,status_absensi = 2).count()
        arrTotalAMed.append(tempTotalAMed)
        arrTotalHAMed.append(tempTotalHAMed)
    totalAbsensiMed = len(arrTotalAMed)
    hadirAbsensiMed = arrTotalHAMed.count(1)

    # Absensi Ogoh - Ogoh
    arrAOgoh = []
    for i in dataAOgoh:
        arrAOgoh.append(int(i['id_agenda']))
    arrTotalAOgoh = []
    arrTotalHAOgoh = []
    for j in arrAOgoh:
        tempTotalAOgoh = AbsensiModel.objects.filter(id_user = idUser, id_agenda = j).count()
        tempTotalHAOgoh = AbsensiModel.objects.filter(id_user = idUser,id_agenda = j,status_absensi = 2).count()
        arrTotalAOgoh.append(tempTotalAOgoh)
        arrTotalHAOgoh.append(tempTotalHAOgoh)
    totalAbsensiOgoh = len(arrTotalAOgoh)
    hadirAbsensiOgoh = arrTotalHAOgoh.count(1)

    # Absensi HUT
    arrAHut = []
    for i in dataAHut:
        arrAHut.append(int(i['id_agenda']))
    arrTotalAHut = []
    arrTotalHAHut = []
    for j in arrAHut:
        tempTotalAHut = AbsensiModel.objects.filter(id_user = idUser, id_agenda = j).count()
        tempTotalHAHut = AbsensiModel.objects.filter(id_user = idUser,id_agenda = j,status_absensi = 2).count()
        arrTotalAHut.append(tempTotalAHut)
        arrTotalHAHut.append(tempTotalHAHut)
    totalAbsensiHut = len(arrTotalAHut)
    hadirAbsensiHut = arrTotalHAHut.count(1)

    # Detail Absensi
    dataA = AbsensiModel.objects.all().filter(id_user = idUser)

    # Detail Iuran Belum dan Sudah Bayar
    dataIB = IuranRekapModel.objects.all().filter(id_user = idUser, status_iuran = 1)
    dataIS = IuranRekapModel.objects.all().filter(id_user = idUser, status_iuran = 2)

    totalIuranB = []
    for i in dataIB:
        if i =='' or i == None:
            totalIuranB.append(int(0))
        else :
            totalIuranB.append(i.id_agenda.id_iuran.jumlah_iuran)
    sumIuranB = sum(totalIuranB)

    totalIuranS = []
    for i in dataIS:
        if i =='' or i == None:
            totalIuranS.append(int(0))
        else :
            totalIuranS.append(i.id_agenda.id_iuran.jumlah_iuran)
    sumIuranS = sum(totalIuranS)

    data = {
        'totalAbsensiBul':totalAbsensiBul,
        'hadirAbsensiBul':hadirAbsensiBul,
        'totalAbsensiPeng':totalAbsensiPeng,
        'hadirAbsensiPeng':hadirAbsensiPeng,
        'totalAbsensiMed':totalAbsensiMed,
        'hadirAbsensiMed':hadirAbsensiMed,
        'totalAbsensiOgoh':totalAbsensiOgoh,
        'hadirAbsensiOgoh':hadirAbsensiOgoh,
        'totalAbsensiHut':totalAbsensiHut,
        'hadirAbsensiHut':hadirAbsensiHut,
        'dataA':dataA,
        'dataIB':dataIB,
        'dataIS':dataIS,
        'sumIuranB' : sumIuranB,
        'sumIuranS' : sumIuranS,
        'dataU' : dataU,

    }
    return render(request, 'dashboarduserbendahara.html',data)



@allowed_bendahara(allowed_roles=dataUserBenda)
def dashboardBenda(request):
    dataUKW = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)

    # Pemasukan Rapat Agenda
    sumDataPemKR = IuranRekapModel.objects.all().filter(status_iuran = 2)
    arrDataPemKR = []
    for i in sumDataPemKR:
        if i =='' or i == None:
            arrDataPemKR.append(int(0))
        else :
            arrDataPemKR.append(i.id_agenda.id_iuran.jumlah_iuran)
    sumTotalPemR = sum(arrDataPemKR)

    # Pemasukan Dana Hibah dan Penggalian Dana
    sumDataPem = KeuanganModel.objects.filter(tipe_keuangan = "Pemasukan").filter(Q(id_jenis_agenda = 4) | Q(id_jenis_agenda = 6)  | Q(id_jenis_agenda = 7)  | Q(id_jenis_agenda = 8)).aggregate(Sum('jumlah_keuangan'))
    arrSumDataPem = []
    if sumDataPem['jumlah_keuangan__sum'] == '' or sumDataPem['jumlah_keuangan__sum'] == None or sumDataPem['jumlah_keuangan__sum'] is None :
        arrSumDataPem.append(int(0))
    else:
        arrSumDataPem.append(int(sumDataPem['jumlah_keuangan__sum']))
    sumTotalPem = sum(arrSumDataPem)
    print(sumTotalPem)


    # Pengeluaran 
    sumDataPeng = KeuanganModel.objects.filter(tipe_keuangan = "Pengeluaran").aggregate(Sum('jumlah_keuangan'))
    arrSumDataPeng = []
    if sumDataPeng['jumlah_keuangan__sum'] == '' or sumDataPeng['jumlah_keuangan__sum'] ==None or sumDataPeng['jumlah_keuangan__sum'] is None:
        arrSumDataPeng.append(int('0'))
    else:
        arrSumDataPeng.append(int(sumDataPeng['jumlah_keuangan__sum']))
    sumTotalPeng = sum(arrSumDataPeng)
    print(sumTotalPeng)

    # Sisa Saldo
    sisaSaldo = (sumTotalPemR + sumTotalPem) - sumTotalPeng
    
   
    data = {
        'dataU':dataU,
        'sumTotalPemR' : sumTotalPemR,
        'sumTotalPem' : sumTotalPem,
        'sumTotalPeng' : sumTotalPeng,
        'sisaSaldo' : sisaSaldo,
        'dataUKW':dataUKW,
    }
    return render(request, 'dashboardbendahara.html',data)


# DATA RAPAT
@allowed_bendahara(allowed_roles=dataUserBenda)
def dataIuran(request):
    dataI = IuranModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    sumIuranBelumTerbayarkan = IuranRekapModel.objects.filter(status_iuran = 1).values().annotate(total_jumlah_iuran=Sum('total_iuran'))
    sumIuranSudahTerbayarkan = IuranRekapModel.objects.filter(status_iuran = 2).values().annotate(total_jumlah_iuran=Sum('total_iuran'))    
    data = {
        'dataI' : dataI,
        'sumIuranBelumTerbayarkan':sumIuranBelumTerbayarkan,
        'sumIuranSudahTerbayarkan':sumIuranSudahTerbayarkan,
        'dataU':dataU,

    }
    return render(request, 'iuran/iuran.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def tambahIuran(request):
    dataI = IuranModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataI': dataI,
        'dataU':dataU,
    }
    if request.method == 'POST':
        form = IuranForm(request.POST)
        current_user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()

            return redirect("/dataIuran")
        pass
    return render(request, 'iuran/tambahiuran.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def editIuran(request, id):
    dataI = IuranModel.objects.get(id_iuran=id)
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataI' : dataI,
        'dataU' : dataU,
    }
    current_user = request.user
    if request.method == 'POST':
        form = IuranForm(request.POST, instance = dataI)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataIuran")
        pass
    return render(request,"iuran/editiuran.html",data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def hapusIuran(request, id):
    dataI = IuranModel.objects.get(id_iuran=id)
    dataI.delete()
    return redirect("/dataIuran")

# DATA DASHBOARD RAPAT
@allowed_bendahara(allowed_roles=dataUserBenda)
def dataRapatIuran(request):
    dataAG = AgendaModel.objects.all()
    dataI = IuranModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)

    id_rapat_data = AgendaModel.objects.filter().values('id_agenda')

    # Check latest id before create rapat
    arrIdRapat = []
    for id_r in id_rapat_data :
        arrIdRapat.append(id_r['id_agenda'])

    # last_id = arrIdRapat[-1]

    if len(arrIdRapat) == 0:
        sumIuranTotal = 0
        sumIuranSudahBayar = 0
        sumIuranBelumBayar = 0
    else:
        last_id = arrIdRapat[-1]
        dataIRS = IuranRekapModel.objects.filter(status_iuran =2).aggregate(Sum('total_iuran'))
        dataIRB = IuranRekapModel.objects.filter(status_iuran =1,id_agenda=last_id).aggregate(Sum('total_iuran'))
        strSumIuranSudahBayar = dataIRS['total_iuran__sum']
        strSumIuranBelumBayar = dataIRB['total_iuran__sum']

        arrSumIuranBelumBayar = []
        if strSumIuranBelumBayar == '' or strSumIuranBelumBayar == None :
            sumIntIuranBelumBayar = '0'
            arrSumIuranBelumBayar.append(sumIntIuranBelumBayar)
        else :
            arrSumIuranBelumBayar.append(str(strSumIuranBelumBayar))
        str2SumIuranBelumBayar = ''.join(arrSumIuranBelumBayar)
        sumIuranBelumBayar = int(str2SumIuranBelumBayar)

        arrSumIuranSudahBayar = []
        if strSumIuranSudahBayar == '' or strSumIuranSudahBayar == None :
            sumIntIuranSudahBayar = '0'
            arrSumIuranSudahBayar.append(sumIntIuranSudahBayar)
        else :
            arrSumIuranSudahBayar.append(str(strSumIuranSudahBayar))
        str2SumIuranSudahBayar = ''.join(arrSumIuranSudahBayar)
        sumIuranSudahBayar = int(str2SumIuranSudahBayar)
        sumIuranTotal = sumIuranBelumBayar + sumIuranSudahBayar
    
    data = {
        'dataAG' : dataAG,
        'dataI' : dataI,
        'sumIuranBelumBayar':sumIuranBelumBayar,
        'sumIuranSudahBayar':sumIuranSudahBayar,
        'sumIuranTotal':sumIuranTotal,
        'dataU' : dataU,
    }
    return render(request, 'iuranrekap/iuranrekap.html',data)

# DATA ABSENSI IURAN
@allowed_bendahara(allowed_roles=dataUserBenda)
def dataRapatIuranDetail(request,id):
    idAgenda = id
    dataI = IuranRekapModel.objects.all().filter(id_agenda=id)
    dataID = IuranGenerateModel.objects.filter(id_agenda=id).values()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)

    arrDataID = []
    for i in dataID:
        arrDataID.append(int(i['id_user']))

    id_rapat_data = AgendaModel.objects.filter().values('id_agenda')

    # Check latest id before create rapat
    arrIdRapat = []
    for id_r in id_rapat_data :
        arrIdRapat.append(id_r['id_agenda'])

    # last_id = arrIdRapat[-1]

    if len(arrIdRapat) == 0:
        sumIuranTotal = 0
        sumIuranSudahBayar = 0
        sumIuranBelumBayar = 0
    else:
        last_id = arrIdRapat[-1]
        dataIRS = IuranRekapModel.objects.filter(status_iuran =2,id_agenda=id).aggregate(Sum('total_iuran'))
        dataIRB = IuranRekapModel.objects.filter(status_iuran =1,id_agenda=id).aggregate(Sum('total_iuran'))
        strSumIuranSudahBayar = dataIRS['total_iuran__sum']
        strSumIuranBelumBayar = dataIRB['total_iuran__sum']

        arrSumIuranBelumBayar = []
        if strSumIuranBelumBayar == '' or strSumIuranBelumBayar == None :
            sumIntIuranBelumBayar = '0'
            arrSumIuranBelumBayar.append(sumIntIuranBelumBayar)
        else :
            arrSumIuranBelumBayar.append(str(strSumIuranBelumBayar))
        str2SumIuranBelumBayar = ''.join(arrSumIuranBelumBayar)
        sumIuranBelumBayar = int(str2SumIuranBelumBayar)

        arrSumIuranSudahBayar = []
        if strSumIuranSudahBayar == '' or strSumIuranSudahBayar == None :
            sumIntIuranSudahBayar = '0'
            arrSumIuranSudahBayar.append(sumIntIuranSudahBayar)
        else :
            arrSumIuranSudahBayar.append(str(strSumIuranSudahBayar))
        str2SumIuranSudahBayar = ''.join(arrSumIuranSudahBayar)
        sumIuranSudahBayar = int(str2SumIuranSudahBayar)
        sumIuranTotal = sumIuranBelumBayar + sumIuranSudahBayar

    data = {
        'idAgenda':idAgenda,
        'dataI':dataI,
        'sumIuranSudahBayar':sumIuranSudahBayar,
        'sumIuranBelumBayar':sumIuranBelumBayar,
        'sumIuranTotal':sumIuranTotal,
        'dataU' : dataU,
    }

    if request.method == 'POST':
        idUser = request.POST.get('update_iuran')
        strIdUser = str(idUser)
        l = len(idUser)
        vii = strIdUser[0:l-1]
        strIdUserSplit = vii.split(',')
        print(strIdUserSplit)

        arrIdUserSplit = []
        for i in strIdUserSplit:
            if i == '':
                print('Empty')
            else:
                arrIdUserSplit.append(i)

        if not arrIdUserSplit :
            return redirect("/dataRapatIuran")
        else:
            arrIdUserSplit2 = arrIdUserSplit[1:]
            newArrIdUserSplit = []
            for d in arrIdUserSplit2:
                newArrIdUserSplit.append(int(d))

            if not newArrIdUserSplit:
                for a in arrDataID:

                    dataIU = IuranRekapModel.objects.get(id_user=int(a),id_agenda=id)
                    form = IuranUpdateForm(request.POST, instance = dataIU)
                    if form.is_valid():
                        obj = form.save(commit=False)
                        obj.status_iuran = 1
                        obj.save()
                return redirect("/dataRapatIuran")

            else :

                # Check latest id rapat pengerampungan
                id_rapat_data = AgendaModel.objects.filter(id_agenda = id).values('id_jenis_agenda')
                arrIdRapat = []
                for id_r in id_rapat_data :
                    arrIdRapat.append(str(id_r['id_jenis_agenda']))
                idJenisR= ''.join(arrIdRapat)
                print("Id Jenis Rapat : ",idJenisR)

                # If Pengerampungan or not
                if idJenisR == "2":
                    print('Yes Pengerampungan')
                    for b in newArrIdUserSplit:
                        arrDataRapatU = []
                        data_rapat_user = IuranRekapModel.objects.filter(id_user = int(b)).values('id_agenda')
                        for i_ru in data_rapat_user:
                            print(i_ru['id_agenda'])
                            arrDataRapatU.append(str(i_ru['id_agenda']))
                        print("data rapat user : ",arrDataRapatU)

                        for a in arrDataRapatU:
                            dataIU = IuranRekapModel.objects.get(id_user=int(b),id_agenda = int(a))
                            form = IuranUpdateForm(request.POST, instance = dataIU)
                            if form.is_valid():
                                obj = form.save(commit=False)
                                obj.status_iuran = 2
                                obj.save()
                else :
                    print('No Pengerampungan')
                    for b in newArrIdUserSplit:
                        dataIU = IuranRekapModel.objects.get(id_user=int(b),id_agenda=id)
                        form = IuranUpdateForm(request.POST, instance = dataIU)
                        if form.is_valid():
                            obj = form.save(commit=False)
                            obj.status_iuran = 2
                            obj.save()

                    diff = list((set(newArrIdUserSplit) | set(arrDataID)) - (set(newArrIdUserSplit) & set(arrDataID)))

                    for c in diff:
                        dataIU2 = IuranRekapModel.objects.get(id_user=int(c),id_agenda=id)
                        form2 = IuranUpdateForm(request.POST, instance = dataIU2)
                        if form2.is_valid():
                            obj2 = form2.save(commit=False)
                            obj2.status_iuran = 1
                            obj2.save()

                return redirect("/dataRapatIuran")
    return render(request, 'iuranrekap/iuranrekapdetail.html',data)

# DATA KEUANGAN
@allowed_bendahara(allowed_roles=dataUserBenda)
def dataKeuangan(request):
    dataK = KeuanganModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
  
    data = {
        'dataK' : dataK,
        'dataU' : dataU,
    }
    return render(request, 'keuangan/keuangan.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def tambahKeuangan(request):
    dataK = KeuanganModel.objects.all()
    dataJA = JenisAgendaModel.objects.all().filter(Q(id_jenis_agenda = 4) | Q(id_jenis_agenda = 5) | Q(id_jenis_agenda = 6) | Q(id_jenis_agenda = 7) | Q(id_jenis_agenda = 8))
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataK': dataK,
        'dataJA':dataJA,
        'dataU':dataU
    }
    if request.method == 'POST':
        form = KeuanganForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()

            return redirect("/dataKeuangan")
        pass
    return render(request, 'keuangan/tambahkeuangan.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def editKeuangan(request, id):
    dataK = KeuanganModel.objects.get(id_keuangan=id)
    dataJA = JenisAgendaModel.objects.all().filter(Q(id_jenis_agenda = 4) | Q(id_jenis_agenda = 5) | Q(id_jenis_agenda = 6) | Q(id_jenis_agenda = 7) | Q(id_jenis_agenda = 8))
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataK' : dataK,
        'dataJA':dataJA,
        'dataU':dataU,
    }
    current_user = request.user
    if request.method == 'POST':
        form = KeuanganForm(request.POST, request.FILES, instance = dataK)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataKeuangan")
        pass
    return render(request,"keuangan/editkeuangan.html",data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def hapusKeuangan(request, id):
    dataK = KeuanganModel.objects.get(id_keuangan=id)
    dataK.delete()
    return redirect("/dataKeuangan")

@allowed_bendahara(allowed_roles=dataUserBenda)
def changePassword(request):
    current_user = request.user
    strUsername = str(current_user.username)
    if request.method == 'POST':
        newPassword = request.POST['new_password']
        u = User.objects.get(username=strUsername)
        u.set_password(str(newPassword))
        u.save()
        return redirect('/bendahara')
    return render(request, 'password_change.html')

@allowed_bendahara(allowed_roles=dataUserBenda)
def editProfileBendahara(request):
    current_user = request.user
    dataU = UserProfileModel.objects.get(id=current_user.id)
    data = {
        'dataU' : dataU,
    }
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=dataU)
        current_user = request.user
        if form.is_valid():
            form.save()
            return redirect("/bendahara")
        pass

    return render(request,'editprofileuserbendahara.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_benda_csv_data_anggota(request):
    dataU = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Data-Anggota-ST-Dwi-Tunggal'+'-'+str(datetime.now())+'.csv'

    writer = csv.writer(response)
    dataHeader = ['Nama','Gender','Status Keanggotaan']
    writer.writerow(dataHeader)
    for data in dataU:
        if data.is_staff == 1:
            dataRole = 'Anggota'
            writer.writerow([data.full_name,data.gender,dataRole])
        elif data.is_staff == 2:
            dataRole = 'Bendahara'
            writer.writerow([data.full_name, data.gender,dataRole])
        elif data.is_staff == 3:
            dataRole = 'Sekretaris'
            writer.writerow([data.full_name ,data.gender,dataRole])
        elif data.is_staff == 4:
            dataRole = 'Ketua / Wakil'
            writer.writerow([data.full_name,data.gender,dataRole])
        else :
            print('Not Identify')
    return response

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_csv_data_iuran(request,id):
    dataI = IuranRekapModel.objects.all().filter(id_agenda=id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Data-Iuran-Anggota-ST-Dwi-Tunggal'+'-'+str(datetime.now())+'.csv'

    writer = csv.writer(response)
    dataHeader = ['Nama Rapat','Nama Anggota','Status Iuran']
    writer.writerow(dataHeader)
    for data in dataI:
        if data.status_iuran == 1 :
            statusIuran = 'Belum Bayar'
            writer.writerow([data.id_agenda.nama_agenda, data.id_user.full_name, statusIuran])
        elif data.status_iuran == 2 :
            statusIuran = 'Sudah Bayar'
            writer.writerow([data.id_agenda.nama_agenda, data.id_user.full_name, statusIuran])
        else :
            print('Not Identify')

    return response

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_csv_data_keuangan(request):
    dataK = KeuanganModel.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Data-Iuran-Anggota-ST-Dwi-Tunggal'+'-'+str(datetime.now())+'.csv'

    writer = csv.writer(response)
    dataHeader = ['Id. Keuangan','Nama Keuangann','Tipe Keuangan', 'Jenis Keuangan', 'Jumlah Keuangan', 'Deskripsi Keuangan']
    writer.writerow(dataHeader)
    for data in dataK:
        writer.writerow([data.id_keuangan, data.nama_keuangan, data.tipe_keuangan, data.id_jenis_agenda.nama_jenis_agenda, data.jumlah_keuangan, data.deskripsi_keuangan])

    return response

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_pdf_data_keuangan_kegiatan(request,id):
    dataKeuanganFile = KeuanganModel.objects.get(id_keuangan = id).file_path
    fs = FileSystemStorage()
    filename = str(dataKeuanganFile)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="keuangan-kegiatan'+'-'+str(datetime.now())+'.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_benda_pdf_data_anggota(request):
    dataU = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))
    dateNow = str(datetime.now())

    data = {'dataU' : dataU, 'dateNow':dateNow}
    template=get_template("data-anggota-pdf-benda.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-anggota'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_benda_pdf_data_keuangan(request):
    dataK = KeuanganModel.objects.all()
    dateNow = str(datetime.now())

    data = {'dataK' : dataK, 'dateNow':dateNow}
    template=get_template("keuangan/data-keuangan-pdf-benda.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-keuangan'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_benda_pdf_data_iuran(request,id):
    dataI = IuranRekapModel.objects.all().filter(id_agenda=id)
    dateNow = str(datetime.now())

    arrDataTA = []
    arrDataNA = []
    for i in dataI:
        arrDataTA.append(str(i.id_agenda.tanggal_agenda))
        arrDataNA.append(i.id_agenda.nama_agenda)
        break
    strDataTA = ''.join(arrDataTA)
    strDataNA = ''.join(arrDataNA)

    arrDateIuran = []
    for i in dataI:
        arrDateIuran.append(str(i.id_agenda.tanggal_agenda.day)+' '+ str(i.id_agenda.tanggal_agenda.strftime("%B")) +' '+ str(i.id_agenda.tanggal_agenda.year))
        break
    strDateIuran = ''.join(arrDateIuran)

    data = {'dataI' : dataI, 'dateNow':dateNow, 'strDataTA':strDataTA, 'strDataNA':strDataNA, 'strDateIuran':strDateIuran}
    template=get_template("iuran/data-iuran-pdf-benda.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-iuran'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

# Generate Iuran
# Generate Surat Agenda
@allowed_bendahara(allowed_roles=dataUserBenda)
def generateIuranAgenda(request):
    dataAG = AgendaModel.objects.all().filter(id_jenis_agenda = 2)
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataAG' : dataAG,
        'dataU':dataU
    }
    return render(request, 'generateiuran/agenda.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_benda_pdf_surat_agenda(request,id):
    import datetime as dt
    dataAG = AgendaModel.objects.all()
    dataI = IuranRekapModel.objects.all().filter(id_agenda=id)
    dataIAng = IuranRekapModel.objects.all().filter(status_iuran=1)

    arrData = []
    for i in dataIAng:
        dataTemp = {
            'id_user' : i.id_user.id,
            'id_jenis_agenda' : i.id_agenda.id_jenis_agenda,
            'iuran' : i.iuran,
        }
        arrData.append(dataTemp)

    df = pd.DataFrame(arrData)
    df2 = df.groupby(['id_user','id_jenis_agenda']).sum()
    df3 = df.groupby(['id_user']).sum()
    df_final = df2.reset_index()
    df_final2 = df3.reset_index()
    
    dataIuran = []
    for index,i in df_final.iterrows():
        tempD = {
            'id_user' : i['id_user'],
            'id_jenis_agenda' : i['id_jenis_agenda'],
            'jumlah_iuran' : i['iuran']
        }
        dataIuran.append(tempD)

    dataTotalIuran = []
    for index,i in df_final2.iterrows():
        tempD1 = {
            'id_user' : i['id_user'],
            'total_iuran' : i['iuran']
        }
        dataTotalIuran.append(tempD1)

    dateNow = dt.datetime.today()
    yearLetter = str(dateNow.year)

    data = {'dataAG' : dataAG, 'dataI' : dataI, 'dataIAng' : dataIAng, 'yearLetter':yearLetter, 'dataIuran' : dataIuran, 'dataTotalIuran' : dataTotalIuran}
    template=get_template("generateiuran/data-iuran-agenda.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="surat-agenda-iuran'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

# DATA AWIG
@allowed_bendahara(allowed_roles=dataUserBenda)
def dataAwig(request):
    dataA = AwigModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
  
    data = {
        'dataA' : dataA,
        'dataU' : dataU,
    }
    return render(request, 'awigbenda.html',data)

@allowed_bendahara(allowed_roles=dataUserBenda)
def export_pdf_data_awigawig_benda(request,id):
    from datetime import datetime
    dataAwigFile = AwigModel.objects.get(id_awigawig = id).awigawig_path
    fs = FileSystemStorage()
    filename = str(dataAwigFile)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="awigawig-stdt'+'-'+str(datetime.now())+'.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')





