# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KütüphaneKayitSistemi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(15, 270, 81, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_kitapTur = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_kitapTur.setGeometry(QtCore.QRect(20, 390, 111, 31))
        self.comboBox_kitapTur.setObjectName("comboBox_kitapTur")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.comboBox_kitapTur.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 71, 21))
        self.label_6.setObjectName("label_6")
        self.tbl_tablolistele = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_tablolistele.setGeometry(QtCore.QRect(310, 110, 521, 311))
        self.tbl_tablolistele.setRowCount(99999)
        self.tbl_tablolistele.setColumnCount(5)
        self.tbl_tablolistele.setObjectName("tbl_tablolistele")
        self.tbl_tablolistele.verticalHeader().setMinimumSectionSize(22)
        self.comboBox_kayitlaraGoreListele = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_kayitlaraGoreListele.setGeometry(QtCore.QRect(480, 10, 111, 31))
        self.comboBox_kayitlaraGoreListele.setObjectName("comboBox_kayitlaraGoreListele")
        self.comboBox_kayitlaraGoreListele.addItem("")
        self.comboBox_kayitlaraGoreListele.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 10, 71, 21))
        self.label_8.setObjectName("label_8")
        self.pushButton_kayitlaragoreListele = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kayitlaragoreListele.setGeometry(QtCore.QRect(610, 10, 131, 31))
        self.pushButton_kayitlaragoreListele.setObjectName("pushButton_kayitlaragoreListele")
        self.pushButton_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ekle.setGeometry(QtCore.QRect(20, 440, 121, 31))
        self.pushButton_ekle.setObjectName("pushButton_ekle")
        self.pushButton_sil = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sil.setGeometry(QtCore.QRect(160, 440, 121, 31))
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.pushButton_listele = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_listele.setGeometry(QtCore.QRect(300, 440, 121, 31))
        self.pushButton_listele.setObjectName("pushButton_listele")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(15, 130, 79, 21))
        self.label_3.setObjectName("label_3")
        self.calendarWidget_sonTeslim = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_sonTeslim.setGeometry(QtCore.QRect(10, 160, 291, 183))
        self.calendarWidget_sonTeslim.setNavigationBarVisible(True)
        self.calendarWidget_sonTeslim.setDateEditEnabled(True)
        self.calendarWidget_sonTeslim.setObjectName("calendarWidget_sonTeslim")
        self.comboBox_kitapTureGoreListele = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_kitapTureGoreListele.setGeometry(QtCore.QRect(480, 60, 111, 31))
        self.comboBox_kitapTureGoreListele.setObjectName("comboBox_kitapTureGoreListele")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.comboBox_kitapTureGoreListele.addItem("")
        self.pushButton_kitapTureGoreListele = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kitapTureGoreListele.setGeometry(QtCore.QRect(610, 60, 131, 31))
        self.pushButton_kitapTureGoreListele.setObjectName("pushButton_kitapTureGoreListele")
        self.lineEdit_aliciAra = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_aliciAra.setGeometry(QtCore.QRect(520, 450, 171, 21))
        self.lineEdit_aliciAra.setObjectName("lineEdit_aliciAra")
        self.pushButton_aliciAra = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_aliciAra.setGeometry(QtCore.QRect(710, 440, 121, 31))
        self.pushButton_aliciAra.setObjectName("pushButton_aliciAra")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 450, 51, 21))
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 231, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.verticalLayout_2.addWidget(self.lineEdit_ID)
        self.lineEdit_aliciAdSoyad = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_aliciAdSoyad.setObjectName("lineEdit_aliciAdSoyad")
        self.verticalLayout_2.addWidget(self.lineEdit_aliciAdSoyad)
        self.lineEdit_kitapIsmi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_kitapIsmi.setObjectName("lineEdit_kitapIsmi")
        self.verticalLayout_2.addWidget(self.lineEdit_kitapIsmi)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_kitapTur.setCurrentIndex(0)
        self.comboBox_kayitlaraGoreListele.setCurrentIndex(0)
        self.comboBox_kitapTureGoreListele.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kütüphane Kayıt Sistemi"))
        self.label_5.setText(_translate("MainWindow", "Ürün Açıklaması"))
        self.comboBox_kitapTur.setItemText(0, _translate("MainWindow", "Hikaye"))
        self.comboBox_kitapTur.setItemText(1, _translate("MainWindow", "Masal"))
        self.comboBox_kitapTur.setItemText(2, _translate("MainWindow", "Roman"))
        self.comboBox_kitapTur.setItemText(3, _translate("MainWindow", "Çizgi Roman"))
        self.comboBox_kitapTur.setItemText(4, _translate("MainWindow", "Tarih"))
        self.comboBox_kitapTur.setItemText(5, _translate("MainWindow", "Şiir"))
        self.comboBox_kitapTur.setItemText(6, _translate("MainWindow", "Bilim Kurgu"))
        self.comboBox_kitapTur.setItemText(7, _translate("MainWindow", "Fabl"))
        self.comboBox_kitapTur.setItemText(8, _translate("MainWindow", "Gerilim - Korku"))
        self.comboBox_kitapTur.setItemText(9, _translate("MainWindow", "Diğer"))
        self.label_6.setText(_translate("MainWindow", "Kitap Türü"))
        self.comboBox_kayitlaraGoreListele.setItemText(0, _translate("MainWindow", "Tüm Kayıtlar"))
        self.comboBox_kayitlaraGoreListele.setItemText(1, _translate("MainWindow", "Teslim Tarihi Geçenler"))
        self.label_8.setText(_translate("MainWindow", "Listeleme Türü"))
        self.pushButton_kayitlaragoreListele.setText(_translate("MainWindow", "Kayıtlara Göre Listele"))
        self.pushButton_ekle.setText(_translate("MainWindow", "Ekle"))
        self.pushButton_sil.setText(_translate("MainWindow", "Sil"))
        self.pushButton_listele.setText(_translate("MainWindow", "Kitapları Listele"))
        self.label_3.setText(_translate("MainWindow", "Son Teslim Tarihi"))
        self.comboBox_kitapTureGoreListele.setItemText(0, _translate("MainWindow", "Hikaye"))
        self.comboBox_kitapTureGoreListele.setItemText(1, _translate("MainWindow", "Masal"))
        self.comboBox_kitapTureGoreListele.setItemText(2, _translate("MainWindow", "Roman"))
        self.comboBox_kitapTureGoreListele.setItemText(3, _translate("MainWindow", "Çizgi Roman"))
        self.comboBox_kitapTureGoreListele.setItemText(4, _translate("MainWindow", "Tarih"))
        self.comboBox_kitapTureGoreListele.setItemText(5, _translate("MainWindow", "Şiir"))
        self.comboBox_kitapTureGoreListele.setItemText(6, _translate("MainWindow", "Bilim Kurgu"))
        self.comboBox_kitapTureGoreListele.setItemText(7, _translate("MainWindow", "Fabl"))
        self.comboBox_kitapTureGoreListele.setItemText(8, _translate("MainWindow", "Gerilim - Korku"))
        self.comboBox_kitapTureGoreListele.setItemText(9, _translate("MainWindow", "Diğer"))
        self.pushButton_kitapTureGoreListele.setText(_translate("MainWindow", "Kitap Türüne Göre Listele"))
        self.pushButton_aliciAra.setText(_translate("MainWindow", "Ara"))
        self.label_7.setText(_translate("MainWindow", "Alıcıyı Ara"))
        self.label_4.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Alıcı Ad Soyadı"))
        self.label.setText(_translate("MainWindow", "Kitap İsmi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
