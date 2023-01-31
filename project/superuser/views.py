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
from .models import UserModel, TentangCompanyModel, VisiCompanyModel, KegiatanCompanyModel, PengurusCompanyModel, BeritaModel, BeritaEditModel, NarahubungCompanyModel, BeritaCommentModel, CommentEditModel
from .forms import UserForm, TentangForm, VisiForm, KegiatanForm, PengurusForm, NarahubungForm, EmailForm, BeritaForm, BeritaEditForm, CommentForm, UploadBeritaForm
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

# Tentang Company
@allowed_superuser(allowed_roles=dataSuperuser)
def editTentangCompany(request):
    dataT = TentangCompanyModel.objects.get(id_tentang_company=1)
    data = {
        'dataT':dataT
    }
    if request.method == 'POST':
        form = TentangForm(request.POST, request.FILES, instance = dataT)
        if form.is_valid():
            form.save()
            return redirect("/superuser")
        pass

    return render(request,"edittentangcompany.html",data)

# Visi Company
@allowed_superuser(allowed_roles=dataSuperuser)
def dataVisiCompany(request):
    dataV = VisiCompanyModel.objects.all()
    data = {
        'dataV' : dataV,
    }
    return render(request, 'visi/visi.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def tambahVisiCompany(request):
    dataV= VisiCompanyModel.objects.all()
    data = {
        'dataV': dataV,
    }
    if request.method == 'POST':
        form = VisiForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            form.save()
            return redirect("/dataVisiCompany")
        pass
    return render(request, 'visi/tambahvisi.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def editVisiCompany(request, id):
    dataV = VisiCompanyModel.objects.get(id_visi_company=id)
    data = {
        'dataV' : dataV,
    }
    current_user = request.user
    if request.method == 'POST':
        form = VisiForm(request.POST, request.FILES, instance = dataV)
        if form.is_valid():
            form.save()
            return redirect("/dataVisiCompany")
        pass
    return render(request,"visi/editvisi.html",data)

@allowed_superuser(allowed_roles=dataSuperuser)
def hapusVisiCompany(request, id):
    dataV = VisiCompanyModel.objects.get(id_visi_company=id)
    dataV.delete()
    return redirect("/dataVisiCompany")

# Kegiatan Company
@allowed_superuser(allowed_roles=dataSuperuser)
def dataKegiatanCompany(request):
    dataK = KegiatanCompanyModel.objects.all()
    data = {
        'dataK' : dataK,
    }
    return render(request, 'kegiatan/kegiatan.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def tambahKegiatanCompany(request):
    dataK= KegiatanCompanyModel.objects.all()
    data = {
        'dataK': dataK,
    }
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            form.save()
            return redirect("/dataKegiatanCompany")
        pass
    return render(request, 'kegiatan/tambahkegiatan.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def editKegiatanCompany(request, id):
    dataK = KegiatanCompanyModel.objects.get(id_kegiatan_company=id)
    data = {
        'dataK' : dataK,
    }
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES, instance = dataK)
        if form.is_valid():
            form.save()
            return redirect("/dataKegiatanCompany")
        pass
    return render(request,"kegiatan/editkegiatan.html",data)

@allowed_superuser(allowed_roles=dataSuperuser)
def hapusKegiatanCompany(request, id):
    dataK = KegiatanCompanyModel.objects.get(id_kegiatan_company=id)
    dataK.delete()
    return redirect("/dataKegiatanCompany")

# Pengurus Company
@allowed_superuser(allowed_roles=dataSuperuser)
def dataPengurusCompany(request):
    dataP = PengurusCompanyModel.objects.all()
    data = {
        'dataP' : dataP,
    }
    return render(request, 'pengurus/pengurus.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def tambahPengurusCompany(request):
    dataP= PengurusCompanyModel.objects.all()
    data = {
        'dataP': dataP,
    }
    if request.method == 'POST':
        form = PengurusForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            form.save()
            return redirect("/dataPengurusCompany")
        pass
    return render(request, 'pengurus/tambahpengurus.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def editPengurusCompany(request, id):
    dataP = PengurusCompanyModel.objects.get(id_pengurus_company=id)
    data = {
        'dataP' : dataP,
    }
    if request.method == 'POST':
        form = PengurusForm(request.POST, request.FILES, instance = dataP)
        if form.is_valid():
            form.save()
            return redirect("/dataPengurusCompany")
        pass
    return render(request,"pengurus/editpengurus.html",data)

@allowed_superuser(allowed_roles=dataSuperuser)
def hapusPengurusCompany(request, id):
    dataP = PengurusCompanyModel.objects.get(id_pengurus_company=id)
    dataP.delete()
    return redirect("/dataPengurusCompany")

def profileCompany (request):
    dataT = TentangCompanyModel.objects.all().filter(id_tentang_company = 1)
    dataV = VisiCompanyModel.objects.all().filter()
    dataK = KegiatanCompanyModel.objects.all().filter()
    dataP = PengurusCompanyModel.objects.all().filter()
    dataId = BeritaModel.objects.all().filter()
    dataN = NarahubungCompanyModel.objects.get(id_narahubung = 1)
    
    arrayLastId = []
    for i in dataId:
        arrayLastId.append(i.id_berita)

    revArray = arrayLastId[::-1]
    dataB = BeritaModel.objects.all().filter(Q(id_berita = revArray[0]) | Q(id_berita = revArray[1]) | Q(id_berita= revArray[2])).order_by('-id_berita')

    data = {
        'dataT' : dataT,
        'dataV' : dataV,
        'dataK' : dataK,
        'dataP' : dataP,
        'dataB' : dataB,
        'dataN' : dataN,
    }
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        pass

    return render(request,'profilecompany.html',data)


# BLOG
def blog(request):

    dataB = BeritaModel.objects.all().filter().order_by('-id_berita')

    dataId = BeritaModel.objects.all().filter()
    arrayLastId = []
    for i in dataId:
        arrayLastId.append(i.id_berita)
    revArray = arrayLastId[::-1]
    dataBSide = BeritaModel.objects.all().filter(Q(id_berita = revArray[0]) | Q(id_berita = revArray[1]) | Q(id_berita= revArray[2]) | Q(id_berita= revArray[3]) | Q(id_berita= revArray[4])).order_by('-id_berita')

    data = {
        'dataB' : dataB,
        'dataBSide' : dataBSide,
    }
    return render(request,'blog/blog.html',data)

def blogDetail (request, id):
    dataB = BeritaModel.objects.get(id_berita=id)
    dataDetail = BeritaModel.objects.get(id_berita = id)
    dataComment = BeritaCommentModel.objects.all().filter(id_berita = id)
    dataCountComment = BeritaCommentModel.objects.all().filter(id_berita = id).count()
    dataId = BeritaModel.objects.all().filter()
    arrayLastId = []
    for i in dataId:
        arrayLastId.append(i.id_berita)
    revArray = arrayLastId[::-1]
    dataBSide = BeritaModel.objects.all().filter(Q(id_berita = revArray[0]) | Q(id_berita = revArray[1]) | Q(id_berita= revArray[2]) | Q(id_berita= revArray[3]) | Q(id_berita= revArray[4])).order_by('-id_berita')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        form2 = BeritaForm(request.POST, instance = dataB)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_berita = id
            obj.created_at = datetime.now()
            obj.save()
            obj2 = form2.save(commit=False)
            obj2.count_comment = str(int(dataCountComment) + 1)
            obj2.save()
            return redirect("/blogDetail/%s" %str(id))
        pass

    data = {
        'dataDetail' : dataDetail,
        'dataComment' : dataComment,
        'dataBSide' : dataBSide,
        'dataCountComment' : dataCountComment,
    }
    return render(request, 'blog/blogdetail.html', data)

@allowed_superuser(allowed_roles=dataSuperuser)
def dataBlogCompany(request):
    dataB = BeritaModel.objects.all()
    data = {
        'dataB' : dataB,
    }
    return render(request, 'blog/datablog.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def tambahBlogCompany(request):
    dataB= BeritaModel.objects.all()
    data = {
        'dataB': dataB,
    }
    if request.method == 'POST':
        form = UploadBeritaForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            form.save()
            return redirect("/dataBlogCompany")
        pass
    return render(request, 'blog/tambahblog.html',data)

@allowed_superuser(allowed_roles=dataSuperuser)
def editBlogCompany(request, id):
    dataB = BeritaEditModel.objects.get(id_berita=id)
    dataC = BeritaCommentModel.objects.all().filter(id_berita=id)
    data = {
        'dataB' : dataB,
        'dataC' : dataC,
    }
    if request.method == 'POST':
        form = BeritaEditForm(request.POST, request.FILES, instance = dataB)
        if form.is_valid():
            form.save()
            return redirect("/dataBlogCompany")
        pass
    return render(request,"blog/editblog.html",data)

@allowed_superuser(allowed_roles=dataSuperuser)
def hapusBlogCompany(request, id):
    dataB = BeritaModel.objects.get(id_berita=id)
    dataB.delete()
    return redirect("/dataBlogCompany")

@allowed_superuser(allowed_roles=dataSuperuser)
def hapusBlogCommentCompany(request, id):
    idBerita= BeritaCommentModel.objects.get(id_comment = id).id_berita
    dataC = BeritaCommentModel.objects.get(id_comment=id)
    dataB = BeritaModel.objects.get(id_berita=idBerita)
    dataCountComment = BeritaCommentModel.objects.all().filter(id_berita = idBerita).count()
    form2 = BeritaForm(instance = dataB)
    print('data :', dataCountComment)
    countT = int(dataCountComment) - 1
    print('hasil :', countT)
    obj2 = form2.save(commit=False)
    obj2.count_comment = countT
    dataC.delete()
    obj2.save()
    return redirect("/dataBlogCompany")

# Narahubung
@allowed_superuser(allowed_roles=dataSuperuser)
def narahubungCompany(request):
    dataN = NarahubungCompanyModel.objects.get(id_narahubung=1)
    data = {
        'dataN':dataN
    }
    if request.method == 'POST':
        form = NarahubungForm(request.POST, instance = dataN)
        if form.is_valid():
            form.save()
            return redirect("/superuser")
        pass

    return render(request,"narahubung/editnarahubung.html",data)





