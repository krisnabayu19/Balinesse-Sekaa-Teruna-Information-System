import os
from pickle import APPEND
from pickletools import pyint
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render, redirect

from authentification.decorators import allowed_anggota
from authentification.views import dataUserAnggota
from bendahara.models import IuranRekapModel
import ketuawakil
from sekretaris.models import AbsensiModel, AgendaModel, UserRekapAbsensi
from ketuawakil.models import AwigModel
from django.db.models import Sum

from .models import UserProfileModel
from .forms import UserProfileForm
from django.contrib.auth.models import User

import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
@allowed_anggota(allowed_roles=dataUserAnggota)
def dashboardAnggota(request):
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
    totalAbsensiBul = arrTotalABul.count(1)
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
    totalAbsensiPeng = arrTotalAPeng.count(1)
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
    totalAbsensiMed = arrTotalAMed.count(1)
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
    totalAbsensiOgoh = arrTotalAOgoh.count(1)
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
    totalAbsensiHut = arrTotalAHut.count(1)
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
        'dataU':dataU,
    }
    return render(request, 'dashboardanggota.html',data)

@allowed_anggota(allowed_roles=dataUserAnggota)
def changePassword(request):
    current_user = request.user
    strUsername = str(current_user.username)
    if request.method == 'POST':
        newPassword = request.POST['new_password']
        u = User.objects.get(username=strUsername)
        u.set_password(str(newPassword))
        u.save()
        return redirect('/anggota')
    return render(request, 'password_change.html')

def get_file_path(request, filename):
    filename_original = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, filename_original)
    return os.path.join('uploads/', filename)


@allowed_anggota(allowed_roles=dataUserAnggota)
def editProfileAnggota(request):
    current_user = request.user
    dataU = UserProfileModel.objects.get(id=current_user.id)
    data = {
        'dataU' : dataU,
    }
    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES, instance=dataU)
        if form.is_valid():
            form.save()
            return redirect("/anggota")
        pass

    return render(request,'editprofileuseranggota.html',data)

# DATA AWIG
@allowed_anggota(allowed_roles=dataUserAnggota)
def dataAwig(request):
    dataA = AwigModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
  
    data = {
        'dataA' : dataA,
        'dataU' : dataU,
    }
    return render(request, 'awig_anggota.html',data)

@allowed_anggota(allowed_roles=dataUserAnggota)
def export_pdf_data_awigawig_anggota(request,id):
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


