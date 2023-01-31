from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from authentification import views
from superuser import views as sviews
from sekretaris import views as skviews
from bendahara import views as sbviews
from anggota import views as saviews
from ketuawakil import views as skwviews
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sviews.profileCompany, name='profilecompany'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('blog/',sviews.blog, name='blog'),
    path('blogDetail/<int:id>',sviews.blogDetail),

    # Access Denied
    path('accessdenied/', views.accessdenied, name='accessdenied'),

    # Superuser
    path('superuser/', sviews.dataUser, name='superuser'),
    path('editUser/<int:id>',sviews.editUser),
    path('editTentangCompany/',sviews.editTentangCompany, name='editTentangCompany'),
    path('dataVisiCompany/',sviews.dataVisiCompany, name='dataVisiCompany'),
    path('tambahVisiCompany/',sviews.tambahVisiCompany, name='tambahVisiCompany'),
    path('hapusVisiCompany/<int:id>',sviews.hapusVisiCompany),
    path('editVisiCompany/<int:id>',sviews.editVisiCompany),
    path('dataKegiatanCompany/',sviews.dataKegiatanCompany, name='dataKegiatanCompany'),
    path('tambahKegiatanCompany/',sviews.tambahKegiatanCompany, name='tambahKegiatanCompany'),
    path('editKegiatanCompany/<int:id>',sviews.editKegiatanCompany),
    path('hapusKegiatanCompany/<int:id>',sviews.hapusKegiatanCompany),
    path('dataPengurusCompany/',sviews.dataPengurusCompany, name='dataPengurusCompany'),
    path('tambahPengurusCompany/',sviews.tambahPengurusCompany, name='tambahPengurusCompany'),
    path('editPengurusCompany/<int:id>',sviews.editPengurusCompany),
    path('hapusPengurusCompany/<int:id>',sviews.hapusPengurusCompany),
    path('editNarahubungCompany/',sviews.narahubungCompany, name='editNarahubungCompany'),
    path('tambahBlogCompany/',sviews.tambahBlogCompany, name='tambahBlogCompany'),
    path('dataBlogCompany/',sviews.dataBlogCompany, name='dataBlogCompany'),
    path('editBlogCompany/<int:id>',sviews.editBlogCompany),
    path('hapusBlogCompany/<int:id>',sviews.hapusBlogCompany),
    path('hapusCommentCompany/<int:id>',sviews.hapusBlogCommentCompany),


    # Executive
    # path('executive/', views.homeexecutive, name='homeexecutive'),

    # Sekretaris
    path('usersekretaris/', skviews.dashboardUserSekretaris, name='dashboardUserSekretaris'),
    path('sekretaris/', skviews.dashboardSekre, name='dashboardSekretaris'),
    path('dataJenisAgenda/', skviews.dataJenisAgenda, name='dataJenisAgenda'),
    path('tambahJenisAgenda/',skviews.tambahJenisAgenda, name='tambahJenisAgenda'),
    path('editJenisAgenda/<int:id>',skviews.editJenisAgenda),
    path('hapusJenisAgenda/<int:id>',skviews.hapusJenisAgenda),
    path('dataAgenda/', skviews.dataAgenda, name='dataAgenda'),
    path('tambahAgenda/',skviews.tambahAgenda, name='tambahAgenda'),
    path('editAgenda/<int:id>',skviews.editAgenda),
    path('hapusAgenda/<int:id>',skviews.hapusAgenda),
    path('dataLpj/', skviews.dataLpj, name='dataLpj'),
    path('tambahLpj/',skviews.tambahLpj, name='tambahLpj'),
    path('editLpj/<int:id>',skviews.editLpj),
    path('hapusLpj/<int:id>',skviews.hapusLpj),
    path('dataAbsensi/<int:id>', skviews.dataAbsensi),
    path('password-change-sekretaris/', skviews.changePassword, name='changePassword'),
    path('editProfileSekretaris/', skviews.editProfileSekretaris, name='editProfileSekretaris'),
    path('export-sekre-csv-data-anggota/',skviews.export_sekre_csv_data_anggota, name='export-sekre-csv-data-anggota'),
    path('export-csv-data-agenda/',skviews.export_csv_data_agenda, name='export-csv-data-agenda'),
    path('export-csv-data-lpj/',skviews.export_csv_data_lpj, name='export-csv-data-lpj'),
    path('export-csv-data-absensi/<int:id>',skviews.export_csv_data_absensi),
    path('export-pdf-data-lpj-kegiatan/<int:id>',skviews.export_pdf_data_lpj_kegiatan),
    path('export-sekre-pdf-data-agenda/',skviews.export_sekre_pdf_data_agenda, name='export-sekre-pdf-data-agenda'),
    path('export-sekre-pdf-data-anggota/',skviews.export_sekre_pdf_data_anggota, name='export-sekre-pdf-data-anggota'),
    path('export-sekre-pdf-data-lpj/',skviews.export_sekre_pdf_data_lpj, name='export-sekre-pdf-data-lpj'),
    path('export-sekre-pdf-data-absensi/<int:id>',skviews.export_sekre_pdf_data_absensi),
    path('generateSuratAgenda/', skviews.generateSuratAgenda, name='generateSuratAgenda'),
    path('generateSuratAnggotaAgenda/<int:id>', skviews.export_sekre_pdf_surat_agenda),
    path('dataAwigSekre/', skviews.dataAwig, name='dataAwigSekre'),
    path('export-pdf-data-awigawig-sekre/<int:id>',skviews.export_pdf_data_awigawig_sekre),


    # Bendahara
    path('userbendahara/', sbviews.dashboardUserBendahara, name='dashboardUserBendahara'),
    path('bendahara/', sbviews.dashboardBenda, name='dashboardBendahara'),
    path('dataIuran/', sbviews.dataIuran, name='dataIuran'),
    path('tambahIuran/',sbviews.tambahIuran, name='tambahIuran'),
    path('editIuran/<int:id>',sbviews.editIuran),
    path('hapusIuran/<int:id>',sbviews.hapusIuran),
    path('dataRapatIuran/', sbviews.dataRapatIuran, name='dataRapatIuran'),
    path('dataRapatIuranDetail/<int:id>', sbviews.dataRapatIuranDetail),
    path('dataKeuangan/', sbviews.dataKeuangan, name='dataKeuangan'),
    path('tambahKeuangan/',sbviews.tambahKeuangan, name='tambahKeuangan'),
    path('editKeuangan/<int:id>',sbviews.editKeuangan),
    path('hapusKeuangan/<int:id>',sbviews.hapusKeuangan),
    path('password-change-bendahara/', sbviews.changePassword, name='changePassword'),
    path('editProfileBendahara/', sbviews.editProfileBendahara, name='editProfileBendahara'),
    path('export-benda-csv-data-anggota/',sbviews.export_benda_csv_data_anggota, name='export-benda-csv-data-anggota'),
    path('export-csv-data-keuangan/',sbviews.export_csv_data_keuangan, name='export-csv-data-keuangan'),
    path('export-csv-data-iuran/<int:id>',sbviews.export_csv_data_iuran),
    path('export-pdf-data-keuangan-kegiatan/<int:id>',sbviews.export_pdf_data_keuangan_kegiatan),
    path('export-benda-pdf-data-anggota/',sbviews.export_benda_pdf_data_anggota, name='export-benda-pdf-data-anggota'),
    path('export-benda-pdf-data-iuran/<int:id>',sbviews.export_benda_pdf_data_iuran),
    path('export-benda-pdf-data-keuangan/',sbviews.export_benda_pdf_data_keuangan,name='export-benda-pdf-data-keuangan'),
    path('generateIuranAgenda/', sbviews.generateIuranAgenda, name='generateIuranAgenda'),
    path('generateIuranAnggotaAgenda/<int:id>', sbviews.export_benda_pdf_surat_agenda),
    path('dataAwigBenda/', sbviews.dataAwig, name='dataAwigBenda'),
    path('export-pdf-data-awigawig-benda/<int:id>',sbviews.export_pdf_data_awigawig_benda),


    # Anggota
    path('anggota/', saviews.dashboardAnggota, name='dashboardAnggota'),
    path('password-change-anggota/', saviews.changePassword, name='changePassword'),
    path('editProfileAnggota/', saviews.editProfileAnggota, name='editProfileAnggota'),
    path('dataAwigAnggota/', saviews.dataAwig, name='dataAwigAnggota'),
    path('export-pdf-data-awigawig-anggota/<int:id>',saviews.export_pdf_data_awigawig_anggota),

    # Ketua dan Wakil
    path('ketuawakil/', skwviews.dashboardKetuaWakil, name='dashboardKetuaWakil'),
    path('userKetuaWakil/', skwviews.dashboardUserKetuaWakil, name='dashboardUserKetuaWakil'),
    path('password-change-ketuawakil/', skwviews.changePassword, name='changePassword'),
    path('editProfileKetuaWakil/', skwviews.editProfileKetuaWakil, name='editProfileKetuaWakil'),
    path('export-pdf-data-lpj-kegiatan-ketua/<int:id>',skwviews.export_pdf_data_lpj_kegiatan_ketua),
    path('export-pdf-data-keuangan-kegiatan-ketua/<int:id>',skwviews.export_pdf_data_keuangan_kegiatan_ketua),
    path('dataAwig/', skwviews.dataAwig, name='dataAwig'),
    path('tambahAwig/',skwviews.tambahAwig, name='tambahAwig'),
    path('editAwig/<int:id>',skwviews.editAwig),
    path('hapusAwig/<int:id>',skwviews.hapusAwig),
    path('export-pdf-data-awigawig-ketua/<int:id>',skwviews.export_pdf_data_awigawig_ketua),
    path('dataEmail/', skwviews.dataEmail, name='dataEmail'),
    path('hapusEmail/<int:id>',skwviews.hapusEmail),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
