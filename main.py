import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from kutuphanekayitui import *
import sqlite3

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


baglanti = sqlite3.connect("kayit.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists kayıt (id int,aliciadsoyad text, kitapAdi text, sonteslimTarihi int, kitapTur text)")
baglanti.commit()


def kayit_ekle():
    id = ui.lineEdit_ID.text()
    AliciAdSoyad = ui.lineEdit_aliciAdSoyad.text()
    Kitapisim = ui.lineEdit_kitapIsmi.text()
    cal = ui.calendarWidget_sonTeslim.selectedDate()
    tarih = (str(cal.toPyDate()))
    kitaptur = ui.comboBox_kitapTur.currentText()

    try:
        ekle = "insert into kayıt (id, aliciadsoyad, kitapAdi, sonteslimTarihi, kitapTur) values (?,?,?,?,?)"
        islem.execute(ekle,(id,AliciAdSoyad,Kitapisim,tarih,kitaptur))
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı",5000)
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Eklenemedi! ==="+str(error))
    kayit_listele()



def kayit_listele():
    ui.tbl_tablolistele.clear()
    ui.tbl_tablolistele.setHorizontalHeaderLabels(("ID","Alıcı Ad Soyad", "Kitap İsmi", "Son Teslim Tarihi", "Kitap Tür"))
    ui.tbl_tablolistele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    sorgu = "select * from kayıt"
    islem.execute(sorgu)

    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tbl_tablolistele.setItem(indexSatir, indexSutun,QTableWidgetItem(str(kayitSutun)))

kayit_listele()


def ture_gore_listele():
    listelenecek_kategori = ui.comboBox_kitapTureGoreListele.currentText()

    sorgu = "select * from kayıt where kitapTur = ?"
    islem.execute(sorgu,(listelenecek_kategori,))
    ui.tbl_tablolistele.clear()
    ui.tbl_tablolistele.setHorizontalHeaderLabels(("ID", "Alıcı Ad Soyad", "Kitap İsmi", "Son Teslim Tarihi", "Kitap Tür"))
    ui.tbl_tablolistele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tbl_tablolistele.setItem(indexSatir, indexSutun,QTableWidgetItem(str(kayitSutun)))


def kayita_gore_listele():
    listelenecek_kayit = ui.comboBox_kayitlaraGoreListele.currentText()

    if listelenecek_kayit == "Teslim Tarihi Geçenler":

        sorgu = "select * from kayıt order by sonteslimTarihi"
        islem.execute(sorgu)
        ui.tbl_tablolistele.clear()
        ui.tbl_tablolistele.setHorizontalHeaderLabels(("ID", "Alıcı Ad Soyad", "Kitap İsmi", "Son Teslim Tarihi", "Kitap Tür"))
        ui.tbl_tablolistele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for indexSatir,kayitNumarasi in enumerate(islem):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                ui.tbl_tablolistele.setItem(indexSatir, indexSutun,QTableWidgetItem(str(kayitSutun)))

    if listelenecek_kayit == "Tüm Kayıtlar":
        kayit_listele()




def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere, "Silme Onayı","Silmek İstediğinizden Emin Misiniz ?",
    QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tbl_tablolistele.selectedItems()
        silinecek_kayit = secilen_kayit[0].text()

        sorgu = "delete from kayıt where id = ?"

        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Başarıyla Silindi",2000)
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Silinirken Hata Oluştu! === "+str(error))

    else:
        ui.statusbar.showMessage("Silme İşlemi İptal Edildi", 2000)
    kayit_listele()


def aliciyi_ara():
    alici = ui.lineEdit_aliciAra.text()

    sorgu = "select * from kayıt where aliciadsoyad = ?"
    islem.execute(sorgu,(alici,))
    ui.tbl_tablolistele.clear()
    ui.tbl_tablolistele.setHorizontalHeaderLabels(("ID", "Alıcı Ad Soyad", "Kitap İsmi", "Son Teslim Tarihi", "Kitap Tür"))
    ui.tbl_tablolistele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tbl_tablolistele.setItem(indexSatir, indexSutun,QTableWidgetItem(str(kayitSutun)))


ui.pushButton_ekle.clicked.connect(kayit_ekle)
ui.pushButton_listele.clicked.connect(kayit_listele)
ui.pushButton_sil.clicked.connect(kayit_sil)
ui.pushButton_kitapTureGoreListele.clicked.connect(ture_gore_listele)
ui.pushButton_kayitlaragoreListele.clicked.connect(kayita_gore_listele)
ui.pushButton_aliciAra.clicked.connect(aliciyi_ara)


sys.exit(uygulama.exec_())