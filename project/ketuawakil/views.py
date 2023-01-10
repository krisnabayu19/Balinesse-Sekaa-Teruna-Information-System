from datetime import date, datetime
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render, redirect

from authentification.decorators import allowed_ketuawakil
from authentification.views import dataUserKetuaWakil
from authentification.models import UserModel
from bendahara.models import IuranRekapModel, KeuanganModel
from sekretaris.models import AbsensiModel, AgendaModel, LpjModel
from django.db.models import Sum

from .models import UserProfileModel, AwigModel
from .forms import UserProfileForm, AwigForm
from django.contrib.auth.models import User

from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def dashboardUserKetuaWakil(request):
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
        'dataU' : dataU,
    }
    return render(request, 'dashboarduserketuawakil.html',data)

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def changePassword(request):
    current_user = request.user
    strUsername = str(current_user.username)
    if request.method == 'POST':
        newPassword = request.POST['new_password']
        u = User.objects.get(username=strUsername)
        u.set_password(str(newPassword))
        u.save()
        return redirect('/ketuawakil')
    return render(request, 'password_change.html')

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def editProfileKetuaWakil(request):
    current_user = request.user
    dataU = UserProfileModel.objects.get(id=current_user.id)
    data = {
        'dataU' : dataU,
    }
    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES, instance=dataU)
        if form.is_valid():
            form.save()
            return redirect("/ketuawakil")
        pass

    return render(request,'editprofileuserketuawakil.html',data)

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def dashboardKetuaWakil(request):
    dataK = KeuanganModel.objects.all()
    dataLPJ = LpjModel.objects.all()
    dataUKW = UserModel.objects.all().filter(Q(is_staff = 1) | Q(is_staff = 2) | Q(is_staff = 3) | Q(is_staff = 4))
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    countDataRB = AgendaModel.objects.filter(id_jenis_agenda=1).count()
    countDataRP = AgendaModel.objects.filter(id_jenis_agenda=2).count()
    countDataLpj = LpjModel.objects.filter().count()
    countDataA = AgendaModel.objects.filter().count()

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
        'countDataRB':countDataRB,
        'countDataRP':countDataRP,
        'countDataLpj':countDataLpj,
        'countDataA':countDataA,
        'sumTotalPemR' : sumTotalPemR,
        'sumTotalPem' : sumTotalPem,
        'sumTotalPeng' : sumTotalPeng,
        'sisaSaldo' : sisaSaldo,
        'dataUKW':dataUKW,
        'dataK':dataK,
        'dataLPJ':dataLPJ,

    }
    return render(request,'dashboardketuawakil.html',data)

# DATA AWIG
@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def dataAwig(request):
    dataA = AwigModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
  
    data = {
        'dataA' : dataA,
        'dataU' : dataU,
    }
    return render(request, 'awigawig/awig.html',data)

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def tambahAwig(request):
    dataA = AwigModel.objects.all()
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataA': dataA,
        'dataU':dataU
    }
    if request.method == 'POST':
        form = AwigForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()

            return redirect("/dataAwig")
        pass
    return render(request, 'awigawig/tambahawig.html',data)

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def editAwig(request, id):
    dataA = AwigModel.objects.get(id_awigawig=id)
    current_user = request.user
    idUser = current_user.id
    dataU = UserProfileModel.objects.get(id=idUser)
    data = {
        'dataA' : dataA,
        'dataU':dataU,
    }
    current_user = request.user
    if request.method == 'POST':
        form = AwigForm(request.POST, request.FILES, instance = dataA)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_user_created = current_user.id
            obj.save()
            return redirect("/dataAwig")
        pass
    return render(request,"awigawig/editawig.html",data)

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def hapusAwig(request, id):
    dataA = AwigModel.objects.get(id_awigawig=id)
    dataA.delete()
    return redirect("/dataAwig")

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def export_pdf_data_lpj_kegiatan_ketua(request,id):
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

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def export_pdf_data_keuangan_kegiatan_ketua(request,id):
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

@allowed_ketuawakil(allowed_roles=dataUserKetuaWakil)
def export_pdf_data_awigawig_ketua(request,id):
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

        

