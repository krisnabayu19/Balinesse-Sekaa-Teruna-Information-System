from ast import Delete
import calendar
import csv
import io
import mimetypes
import os
from pydoc import stripid
from pyexpat.errors import messages
from urllib import response
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
from datetime import date,datetime
import math
from itertools import groupby
from operator import itemgetter
from django.shortcuts import render, redirect

from authentification.decorators import allowed_sekretaris
from authentification.views import dataUserSekre
from .models import AgendaModel,LpjModel,AbsensiModel,AbsensiGenerateModel,UpdateAbsensiModel,JenisAgendaModel
from authentification.models import UserModel
from bendahara.models import IuranModel, IuranGenerateModel, IuranRekapModel
from ketuawakil.models import AwigModel
from .forms import AgendaForm,LpjForm,AbsensiForm,JenisAgendaForm
from django.db.models import Sum

from .models import UserProfileModel
from .forms import UserProfileForm
from django.contrib.auth.models import User

# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile

from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from io import StringIO, BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django.template.loader import get_template
from deep_translator import PonsTranslator
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator




# Create your views here.
@allowed_sekretaris(allowed_roles=dataUserSekre)
def dashboardUserSekretaris(request):
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
        'sumIuranB':sumIuranB,
        'sumIuranS':sumIuranS,
        'dataU':dataU,
    }
    return render(request, 'dashboardusersekretaris.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def dashboardSekre(request):

    dataUKW = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    countDataRB = AgendaModel.objects.filter(id_jenis_agenda=1).count()
    countDataRP = AgendaModel.objects.filter(id_jenis_agenda=2).count()
    countDataLpj = LpjModel.objects.filter().count()
    countDataA = AgendaModel.objects.filter().count()
    data = {
        'dataUKW':dataUKW,
        'countDataRB' : countDataRB,
        'countDataRP' : countDataRP,
        'countDataLpj' : countDataLpj,
        'countDataA':countDataA,
        'dataU' : dataU,
    }
    return render(request, 'dashboardsekretaris.html',data)



# DATA JENIS AGENDA
@allowed_sekretaris(allowed_roles=dataUserSekre)
def dataJenisAgenda(request):
    dataJA = JenisAgendaModel.objects.all()
    countDataJA = JenisAgendaModel.objects.filter().count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataJA' : dataJA,
        'countDataJA' : countDataJA,
        'dataU' : dataU,
    }
    return render(request, 'jenisagenda/jenisagenda.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def tambahJenisAgenda(request):
    countDataJA = JenisAgendaModel.objects.filter().count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'countDataJA':countDataJA,
        'dataU':dataU,
    }

    if request.method == 'POST':
        form = JenisAgendaForm(request.POST)
        current_user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataJenisAgenda")
        pass
    return render(request, 'jenisagenda/tambahjenisagenda.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def editJenisAgenda(request, id):
    dataJA = JenisAgendaModel.objects.get(id_jenis_agenda=id)
    countDataJA = LpjModel.objects.filter().count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataJA' : dataJA,
        'countDataLpj':countDataJA,
        'dataU':dataU,
    }
    current_user = request.user
    if request.method == 'POST':
        form = JenisAgendaForm(request.POST, instance = dataJA)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataJenisAgenda")
        pass
    return render(request,"jenisagenda/editjenisagenda.html",data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def hapusJenisAgenda(request, id):
    dataJA = JenisAgendaModel.objects.get(id_jenis_agenda=id)
    dataJA.delete()
    return redirect("/dataJenisAgenda")


# DATA RAPAT
@allowed_sekretaris(allowed_roles=dataUserSekre)
def dataAgenda(request):
    dataAG = AgendaModel.objects.all()
    countDataRB = AgendaModel.objects.filter(id_jenis_agenda=1).count()
    countDataRP = AgendaModel.objects.filter(id_jenis_agenda=2).count()
    countDataRI = AgendaModel.objects.filter(id_jenis_agenda=3).count()
    dataI = IuranModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataAG' : dataAG,
        'dataI' : dataI,
        'countDataRB' : countDataRB,
        'countDataRP' : countDataRP,
        'countDataRI' : countDataRI,
        'dataU':dataU
    }
    return render(request, 'agenda/agenda.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def tambahAgenda(request):
    dataUser = UserModel.objects.filter(is_active=1,verified=1).filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4)).values()
    countDataRB = AgendaModel.objects.filter(id_jenis_agenda=1).count()
    countDataRP = AgendaModel.objects.filter(id_jenis_agenda=2).count()
    countDataRI = AgendaModel.objects.filter(id_jenis_agenda=3).count()
    dataI = IuranModel.objects.all()
    dataJA = JenisAgendaModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)

    data = {
        'dataI': dataI,
        'dataJA':dataJA,
        'countDataRB' : countDataRB,
        'countDataRP' : countDataRP,
        'countDataRI' : countDataRI,
        'dataU':dataU,
    }
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        current_user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()

            id_rapat_data = AgendaModel.objects.filter().values('id_agenda')
            id_iuran_data = request.POST['id_iuran']

            # Check latest id before create rapat
            arrIdRapat = []
            for id_r in id_rapat_data :
                arrIdRapat.append(id_r['id_agenda'])
            last_id = arrIdRapat[-1]

            # Check First Data on Database
            if len(arrIdRapat) == 1:
                print('yes first data')

                # Generate Data Absensi
                for i in dataUser:
                    absensiObj = AbsensiGenerateModel.objects.create(
                        id_agenda = last_id,
                        id_user = i['id'],
                        )
                    absensiObj.save()

                dataJumlahIuran = IuranModel.objects.filter(id_iuran=int(id_iuran_data)).values('jumlah_iuran')
                arr2dataJumlahIuran = []
                for k in dataJumlahIuran:
                    arr2dataJumlahIuran.append(str(k['jumlah_iuran']))
                valueJumlahIuran = ''.join(arr2dataJumlahIuran)

                # Generate Data Iuran
                for i in dataUser:
                    totalIuran = int(valueJumlahIuran)
                    print(totalIuran)
                    iuranObj = IuranGenerateModel.objects.create(
                        id_agenda = last_id,
                        id_user = i['id'],
                        iuran = int(valueJumlahIuran),
                        total_iuran = totalIuran,
                        )
                    iuranObj.save()

            else:
                print('no first data')
                dataJumlahIuran = IuranModel.objects.filter(id_iuran=int(id_iuran_data)).values('jumlah_iuran')

                arr2dataJumlahIuran = []
                for k in dataJumlahIuran:
                    arr2dataJumlahIuran.append(str(k['jumlah_iuran']))
                
                valueJumlahIuran = ''.join(arr2dataJumlahIuran)

                # Generate Data Absensi
                for i in dataUser:
                    absensiObj = AbsensiGenerateModel.objects.create(
                        id_agenda = last_id,
                        id_user = i['id'],
                        )
                    absensiObj.save()

                id_jenis_agenda = request.POST['id_jenis_agenda']

                # Check Agenda Pengerampungan
                if id_jenis_agenda == "2":
                    print('Yes Pengerampungan')

                    id_rapat_peng_data = AgendaModel.objects.filter(id_jenis_agenda = 2).values('id_agenda')

                    # Check latest id rapat pengerampungan
                    arrIdRapatPeng = []
                    for id_rp in id_rapat_peng_data :
                        arrIdRapatPeng.append(id_rp['id_agenda'])
                    
                    # Check first rapat pengerampungan
                    if len(arrIdRapatPeng) == 1:
                        print("First Rapat Pengerampungan")
                        for i in dataUser:
                            print(i['id'])
                            result = IuranRekapModel.objects.filter(status_iuran = 1, id_user=int(i['id'])).values('id_user').annotate(total_jumlah_iuran=Sum('total_iuran'))

                            arrDataJumlahIuran =[]
                            for j in result:
                                arrDataJumlahIuran.append(str(j['total_jumlah_iuran']))

                            if not arrDataJumlahIuran:
                                totalIuran = int(valueJumlahIuran)
                                print(totalIuran)
                                iuranObj = IuranGenerateModel.objects.create(
                                    id_agenda = last_id,
                                    id_user = i['id'],
                                    iuran = int(valueJumlahIuran),
                                    total_iuran = totalIuran,
                                    )
                                iuranObj.save()
                            else:
                                strJumlahIuran = ''.join(arrDataJumlahIuran)
                                totalIuran = (int(strJumlahIuran)+int(valueJumlahIuran))
                                print(totalIuran)
                                iuranObj = IuranGenerateModel.objects.create(
                                    id_agenda = last_id,
                                    id_user = i['id'],
                                    iuran = int(valueJumlahIuran),
                                    total_iuran = totalIuran,
                                    )
                                iuranObj.save()
                    else:
                        print("No First Rapat Pengerampungan")
                        last_id_rp = arrIdRapatPeng[-2]
                        print("Last ID Peng : ",last_id_rp)

                        for i in dataUser:
                            print(last_id_rp)

                            # Last id data rapat pengerampungan
                            resultPeng = IuranRekapModel.objects.filter(status_iuran = 1, id_user=int(i['id']), id_agenda = last_id_rp).values('id_user').annotate(total_jumlah_iuran=Sum('total_iuran'))
                            arrDataJumlahIuranLastP =[]
                            for j in resultPeng:
                                arrDataJumlahIuranLastP.append(str(j['total_jumlah_iuran']))
                            strJumlahIuranLastP = ''.join(arrDataJumlahIuranLastP)
                            print(strJumlahIuranLastP)

                            # Id after last id rapat pengerampungan
                            resultPeng1 = IuranRekapModel.objects.filter(status_iuran = 1, id_user=int(i['id']), id_agenda__gt = last_id_rp).values('id_user').annotate(total_jumlah_iuran=Sum('total_iuran'))
                            arrDataJumlahIuranALastP =[]
                            for k in resultPeng1:
                                arrDataJumlahIuranALastP.append(str(k['total_jumlah_iuran']))
                            strJumlahIuranALastP = ''.join(arrDataJumlahIuranALastP)

                            # Rekap iuran last pengerampungan
                            arrNewData = []
                            if strJumlahIuranLastP == '' or strJumlahIuranLastP == None :
                                arrNewData.append('0')
                            else :
                                arrNewData.append(str(strJumlahIuranLastP))
                            strJumlahIuranLastP1 = ''.join(arrNewData)

                            # Rekap iuran after last pengerampungan
                            arrNewData1 = []
                            if strJumlahIuranALastP == '' or strJumlahIuranALastP == None :
                                arrNewData1.append('0')
                            else :
                                arrNewData1.append(str(strJumlahIuranALastP))
                            strJumlahIuranALastP1 = ''.join(arrNewData1)

                            totalIuranFix = int(strJumlahIuranLastP1) + int(strJumlahIuranALastP1)

                            iuranObj = IuranGenerateModel.objects.create(
                                id_agenda = last_id,
                                id_user = i['id'],
                                iuran = int(valueJumlahIuran),
                                total_iuran = totalIuranFix + int(valueJumlahIuran),
                                )
                            iuranObj.save()
                else :
                    print('No Pengerampungan')

                    # Generate Data Iuran
                    for i in dataUser:
                        totalIuran = int(valueJumlahIuran)
                        print(totalIuran)
                        iuranObj = IuranGenerateModel.objects.create(
                            id_agenda = last_id,
                            id_user = i['id'],
                            iuran = int(valueJumlahIuran),
                            total_iuran = totalIuran,
                            )
                        iuranObj.save()
            return redirect("/dataAgenda")
        pass
    return render(request, 'agenda/tambahagenda.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def editAgenda(request, id):
    dataAG = AgendaModel.objects.get(id_agenda=id)
    dataI = IuranModel.objects.all()
    dataJA = JenisAgendaModel.objects.all()
    countDataRB = AgendaModel.objects.filter(id_jenis_agenda=1).count()
    countDataRP = AgendaModel.objects.filter(id_jenis_agenda=2).count()
    countDataRI = AgendaModel.objects.filter(id_jenis_agenda=3).count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataAG' : dataAG,
        'dataI' : dataI,
        'dataJA':dataJA,
        'countDataRB' : countDataRB,
        'countDataRP' : countDataRP,
        'countDataRI' : countDataRI,
        'dataU':dataU,
    }
    current_user = request.user
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance = dataAG)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataAgenda")
        pass
    return render(request,"agenda/editagenda.html",data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def hapusAgenda(request, id):
    dataR = AgendaModel.objects.get(id_agenda=id)
    dataR.delete()
    return redirect("/dataAgenda")


# DATA LPJ
@allowed_sekretaris(allowed_roles=dataUserSekre)
def dataLpj(request):
    dataL = LpjModel.objects.all()
    countDataLpj = LpjModel.objects.filter().count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataL' : dataL,
        'countDataLpj':countDataLpj,
        'dataU':dataU,
    }
    return render(request, 'lpj/lpj.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def tambahLpj(request):
    countDataLpj = LpjModel.objects.filter().count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'countDataLpj':countDataLpj,
        'dataU':dataU,
    }

    if request.method == 'POST':
        form = LpjForm(request.POST,request.FILES)
        current_user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataLpj")
        pass
    return render(request, 'lpj/tambahlpj.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def editLpj(request, id):
    dataL = LpjModel.objects.get(id_lpj=id)
    countDataLpj = LpjModel.objects.filter().count()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataL' : dataL,
        'countDataLpj':countDataLpj,
        'dataU':dataU,
    }
    current_user = request.user
    if request.method == 'POST':
        form = LpjForm(request.POST, request.FILES, instance = dataL)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataLpj")
        pass
    return render(request,"lpj/editlpj.html",data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def hapusLpj(request, id):
    dataL = LpjModel.objects.get(id_lpj=id)
    dataL.delete()
    return redirect("/dataLpj")


# DATA Update ABSENSI
@allowed_sekretaris(allowed_roles=dataUserSekre)
def dataAbsensi(request,id):
    idAgenda = id
    dataA = AbsensiModel.objects.all().filter(id_agenda=id)
    dataAD = AbsensiGenerateModel.objects.filter(id_agenda=id).values()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    
    arrDataAD = []
    for i in dataAD:
        arrDataAD.append(int(i['id_user']))

    if request.method == 'POST':
        idUser = request.POST.get('update_absensi')
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
            return redirect("/dataAgenda")
        else:
            arrIdUserSplit2 = arrIdUserSplit[1:]
            newArrIdUserSplit = []
            for d in arrIdUserSplit2:
                newArrIdUserSplit.append(int(d))

            if not newArrIdUserSplit:
                for a in arrDataAD:
                    dataAU = AbsensiModel.objects.get(id_user=int(a),id_agenda=id)
                    form = AbsensiForm(request.POST, instance = dataAU)
                    if form.is_valid():
                        obj = form.save(commit=False)
                        obj.status_absensi = 1
                        obj.save()
                return redirect("/dataAgenda")

            else :

                for b in newArrIdUserSplit:
                    dataAU = AbsensiModel.objects.get(id_user=int(b),id_agenda=id)
                    form = AbsensiForm(request.POST, instance = dataAU)
                    if form.is_valid():
                        obj = form.save(commit=False)
                        obj.status_absensi = 2
                        obj.save()

                diff = list((set(newArrIdUserSplit) | set(arrDataAD)) - (set(newArrIdUserSplit) & set(arrDataAD)))

                for c in diff:
                    dataAU2 = AbsensiModel.objects.get(id_user=int(c),id_agenda=id)
                    form2 = AbsensiForm(request.POST, instance = dataAU2)
                    if form2.is_valid():
                        obj2 = form2.save(commit=False)
                        obj2.status_absensi = 1
                        obj2.save()

                return redirect("/dataAgenda")

    return render(request, 'absensi/absensi.html',{'dataA' : dataA,'dataU' : dataU, 'idAgenda' : idAgenda})

@allowed_sekretaris(allowed_roles=dataUserSekre)
def changePassword(request):
    current_user = request.user
    strUsername = str(current_user.username)
    if request.method == 'POST':
        newPassword = request.POST['new_password']
        u = User.objects.get(username=strUsername)
        u.set_password(str(newPassword))
        u.save()
        return redirect('/sekretaris')
    return render(request, 'password_change.html')

@allowed_sekretaris(allowed_roles=dataUserSekre)
def editProfileSekretaris(request):
    current_user = request.user
    dataU = UserProfileModel.objects.get(id=current_user.id)
    data = {
        'dataU' : dataU,
    }
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance = dataU)
        current_user = request.user
        if form.is_valid():
            form.save()
            return redirect("/sekretaris")
        pass

    return render(request,'editprofileusersekretaris.html',data)


# Export CSV
@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_sekre_csv_data_anggota(request):
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

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_csv_data_agenda(request):
    dataAG = AgendaModel.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Data-Agenda-Anggota-ST-Dwi-Tunggal'+'-'+str(datetime.now())+'.csv'

    writer = csv.writer(response)
    dataHeader = ['Tanggal Agenda','Nama Agenda','Jenis Agenda','Deskripsi Anggota', 'Jumlah Iuran', 'Hasil Agenda']
    writer.writerow(dataHeader)
    for data in dataAG:
        writer.writerow([data.tanggal_agenda, data.nama_agenda, data.id_jenis_agenda.nama_jenis_agenda, data.deskripsi_agenda, data.id_iuran.jumlah_iuran, data.hasil_agenda ])
    return response

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_csv_data_lpj(request):
    dataLpj = LpjModel.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Data-Lpj-Anggota-ST-Dwi-Tunggal'+'-'+str(datetime.now())+'.csv'

    writer = csv.writer(response)
    dataHeader = ['Tanggal LPJ','Nama LPJ','Deskripsi LPJ']
    writer.writerow(dataHeader)
    for data in dataLpj:
        writer.writerow([data.tanggal_lpj, data.nama_lpj, data.deskripsi_lpj])
    return response

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_csv_data_absensi(request,id):

    dataA = AbsensiModel.objects.all().filter(id_agenda=id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Data-Absensi-Anggota-ST-Dwi-Tunggal'+'-'+str(datetime.now())+'.csv'

    writer = csv.writer(response)
    dataHeader = ['Nama Rapat','Nama Anggota','Status Absensi']
    writer.writerow(dataHeader)
    for data in dataA:
        if data.status_absensi == 1 :
            statusAbsensi = 'Tidak Hadir'
            writer.writerow([data.id_agenda.nama_agenda, data.id_user.full_name, statusAbsensi])
        elif data.status_absensi == 2 :
            statusAbsensi = 'Hadir'
            writer.writerow([data.id_agenda.nama_agenda, data.id_user.full_name, statusAbsensi])
        else :
            print('Not Identify')

    return response


# Export PDF
@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_pdf_data_lpj_kegiatan(request,id):
    dataLpjFile = LpjModel.objects.get(id_lpj = id).file_path
    fs = FileSystemStorage()
    filename = str(dataLpjFile)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="lpj-kegiatan'+'-'+str(datetime.now())+'.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_sekre_pdf_data_anggota(request):
    dataU = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))
    dateNow = str(datetime.now())

    data = {'dataU' : dataU, 'dateNow':dateNow}
    template=get_template("data-anggota-pdf-sekre.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-anggota'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_sekre_pdf_data_agenda(request):
    dataAG = AgendaModel.objects.all()
    dateNow = str(datetime.now())

    data = {'dataAG' : dataAG, 'dateNow':dateNow}
    template=get_template("agenda/data-agenda-pdf-sekre.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-agenda'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_sekre_pdf_data_lpj(request):
    dataL = LpjModel.objects.all()
    dateNow = str(datetime.now())

    data = {'dataL' : dataL, 'dateNow':dateNow}
    template=get_template("lpj/data-LPJ-pdf-sekre.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-lpj'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_sekre_pdf_data_absensi(request,id):
    dataA = AbsensiModel.objects.all().filter(id_agenda=id)
    dateNow = str(datetime.now())

    arrDataTA = []
    arrDataNA = []
    for i in dataA:
        arrDataTA.append(str(i.id_agenda.tanggal_agenda))
        arrDataNA.append(i.id_agenda.nama_agenda)
        break
    strDataTA = ''.join(arrDataTA)
    strDataNA = ''.join(arrDataNA)

    arrDateMeet = []
    for i in dataA:
        arrDateMeet.append(str(i.id_agenda.tanggal_agenda.day)+' '+ str(i.id_agenda.tanggal_agenda.strftime("%B")) +' '+ str(i.id_agenda.tanggal_agenda.year))
        break
    strDateMeet = ''.join(arrDateMeet)


    data = {'dataA' : dataA, 'dateNow':dateNow, 'strDataTA':strDataTA, 'strDataNA':strDataNA, 'strDateMeet':strDateMeet}
    template=get_template("absensi/data-absensi-pdf-sekre.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="data-absensi'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")


# Generate Surat Agenda
@allowed_sekretaris(allowed_roles=dataUserSekre)
def generateSuratAgenda(request):
    dataAG = AgendaModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataAG' : dataAG,
        'dataU':dataU
    }
    return render(request, 'generatesurat/agenda.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_sekre_pdf_surat_agenda(request,id):
    import datetime as dt
    dataAG = AgendaModel.objects.all()
    dataA = AbsensiModel.objects.all().filter(id_agenda=id)

    dateNow = dt.datetime.today()
    currentDate = dt.date.today()
    currentMonthName = currentDate.strftime("%B")
    indoMonth = MyMemoryTranslator(source="en", target="id").translate(text=str(currentMonthName))
    dateCreated = str(dateNow.day) + ' ' + str(indoMonth)+ ' ' +str(dateNow.year)

    arrDateMeet = []
    for i in dataA:
        arrDateMeet.append(str(i.id_agenda.tanggal_agenda.day)+' '+ MyMemoryTranslator(source="en", target="id").translate(text=str(i.id_agenda.tanggal_agenda.strftime("%B"))) +' '+ str(i.id_agenda.tanggal_agenda.year))
        break
    strDateMeet = ''.join(arrDateMeet)

    yearLetter = str(dateNow.year)

    data = {'dataAG' : dataAG, 'dataA' : dataA, 'dateNow':dateNow, 'dateCreated':dateCreated, 'strDateMeet':strDateMeet, 'yearLetter' : yearLetter}
    template=get_template("generatesurat/data-surat-agenda.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        result = HttpResponse(response.getvalue(),content_type="application/pdf")
        result['Content-Disposition'] = 'attachment; filename="surat-agenda'+'-'+str(datetime.now())+'.pdf"'
        return result
    else:
        return HttpResponse("Error Generating PDF")

# DATA AWIG
@allowed_sekretaris(allowed_roles=dataUserSekre)
def dataAwig(request):
    dataA = AwigModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
  
    data = {
        'dataA' : dataA,
        'dataU' : dataU,
    }
    return render(request, 'awig.html',data)

@allowed_sekretaris(allowed_roles=dataUserSekre)
def export_pdf_data_awigawig_sekre(request,id):
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







