# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created: Thu Jun 19 22:00:13 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 650)
        MainWindow.setMinimumSize(QtCore.QSize(800, 650))
        MainWindow.setMaximumSize(QtCore.QSize(800, 650))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 205, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 205, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 205, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 205, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar_GenerateOutFile = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_GenerateOutFile.setGeometry(QtCore.QRect(10, 590, 781, 16))
        self.progressBar_GenerateOutFile.setAutoFillBackground(False)
        self.progressBar_GenerateOutFile.setProperty("value", 0)
        self.progressBar_GenerateOutFile.setTextVisible(False)
        self.progressBar_GenerateOutFile.setObjectName(_fromUtf8("progressBar_GenerateOutFile"))
        self.Button_LoadOutFile = QtGui.QPushButton(self.centralwidget)
        self.Button_LoadOutFile.setGeometry(QtCore.QRect(400, 6, 91, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/rafal/.designer/backup/Image/Rysunek.svg-path3297-4294966409.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_LoadOutFile.setIcon(icon)
        self.Button_LoadOutFile.setIconSize(QtCore.QSize(25, 25))
        self.Button_LoadOutFile.setObjectName(_fromUtf8("Button_LoadOutFile"))
        self.listWidget_MainFile = QtGui.QListWidget(self.centralwidget)
        self.listWidget_MainFile.setGeometry(QtCore.QRect(10, 156, 381, 391))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.listWidget_MainFile.setFont(font)
        self.listWidget_MainFile.setProperty("isWrapping", False)
        self.listWidget_MainFile.setWordWrap(True)
        self.listWidget_MainFile.setObjectName(_fromUtf8("listWidget_MainFile"))
        self.Button_LoadMainFilePath = QtGui.QPushButton(self.centralwidget)
        self.Button_LoadMainFilePath.setGeometry(QtCore.QRect(70, 6, 91, 31))
        self.Button_LoadMainFilePath.setObjectName(_fromUtf8("Button_LoadMainFilePath"))
        self.listWidget_OutFilesList = QtGui.QListWidget(self.centralwidget)
        self.listWidget_OutFilesList.setGeometry(QtCore.QRect(400, 46, 391, 61))
        self.listWidget_OutFilesList.setObjectName(_fromUtf8("listWidget_OutFilesList"))
        self.horizontalSlider_Threshold = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_Threshold.setEnabled(False)
        self.horizontalSlider_Threshold.setGeometry(QtCore.QRect(500, 126, 160, 19))
        self.horizontalSlider_Threshold.setMinimum(1)
        self.horizontalSlider_Threshold.setMaximum(100)
        self.horizontalSlider_Threshold.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Threshold.setObjectName(_fromUtf8("horizontalSlider_Threshold"))
        self.label_numberOfThreshold = QtGui.QLabel(self.centralwidget)
        self.label_numberOfThreshold.setGeometry(QtCore.QRect(670, 116, 131, 31))
        self.label_numberOfThreshold.setObjectName(_fromUtf8("label_numberOfThreshold"))
        self.listWidget_ChoosenOutFile = QtGui.QListWidget(self.centralwidget)
        self.listWidget_ChoosenOutFile.setGeometry(QtCore.QRect(400, 156, 391, 391))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.listWidget_ChoosenOutFile.setFont(font)
        self.listWidget_ChoosenOutFile.setWordWrap(True)
        self.listWidget_ChoosenOutFile.setObjectName(_fromUtf8("listWidget_ChoosenOutFile"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QtCore.QRect(510, 96, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.Button_LoadOutFileCandidateFromWWW = QtGui.QPushButton(self.centralwidget)
        self.Button_LoadOutFileCandidateFromWWW.setGeometry(QtCore.QRect(540, 6, 101, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/rafal/.designer/backup/Image/Rysunek.svg-path3008-154.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_LoadOutFileCandidateFromWWW.setIcon(icon1)
        self.Button_LoadOutFileCandidateFromWWW.setIconSize(QtCore.QSize(25, 25))
        self.Button_LoadOutFileCandidateFromWWW.setObjectName(_fromUtf8("Button_LoadOutFileCandidateFromWWW"))
        self.comboBox_MethodList = QtGui.QComboBox(self.centralwidget)
        self.comboBox_MethodList.setGeometry(QtCore.QRect(410, 126, 69, 22))
        self.comboBox_MethodList.setObjectName(_fromUtf8("comboBox_MethodList"))
        self.comboBox_MethodList.addItem(_fromUtf8(""))
        self.comboBox_MethodList.addItem(_fromUtf8(""))
        self.listWidget_errorList = QtGui.QListWidget(self.centralwidget)
        self.listWidget_errorList.setEnabled(False)
        self.listWidget_errorList.setGeometry(QtCore.QRect(10, 550, 781, 41))
        self.listWidget_errorList.setObjectName(_fromUtf8("listWidget_errorList"))
        self.Button_RemoveOutFile = QtGui.QPushButton(self.centralwidget)
        self.Button_RemoveOutFile.setGeometry(QtCore.QRect(690, 6, 91, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/rafal/.designer/backup/Image/Rysunek.svg-path3297-4294966531.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_RemoveOutFile.setIcon(icon2)
        self.Button_RemoveOutFile.setIconSize(QtCore.QSize(25, 25))
        self.Button_RemoveOutFile.setObjectName(_fromUtf8("Button_RemoveOutFile"))
        self.Button_LoadConfigPath = QtGui.QPushButton(self.centralwidget)
        self.Button_LoadConfigPath.setGeometry(QtCore.QRect(230, 6, 91, 31))
        self.Button_LoadConfigPath.setObjectName(_fromUtf8("Button_LoadConfigPath"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 381, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 227, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 227, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 227, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 227, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(50, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_numberOfSentences = QtGui.QLabel(self.groupBox)
        self.label_numberOfSentences.setGeometry(QtCore.QRect(240, 10, 111, 41))
        self.label_numberOfSentences.setText(_fromUtf8(""))
        self.label_numberOfSentences.setObjectName(_fromUtf8("label_numberOfSentences"))
        self.label_repeatSentencesProcent = QtGui.QLabel(self.groupBox)
        self.label_repeatSentencesProcent.setGeometry(QtCore.QRect(240, 80, 111, 21))
        self.label_repeatSentencesProcent.setText(_fromUtf8(""))
        self.label_repeatSentencesProcent.setObjectName(_fromUtf8("label_repeatSentencesProcent"))
        self.label_numberOfRepeatSentences = QtGui.QLabel(self.groupBox)
        self.label_numberOfRepeatSentences.setGeometry(QtCore.QRect(240, 50, 111, 21))
        self.label_numberOfRepeatSentences.setText(_fromUtf8(""))
        self.label_numberOfRepeatSentences.setObjectName(_fromUtf8("label_numberOfRepeatSentences"))
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(50, 40, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(50, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.Button_Przelicz = QtGui.QPushButton(self.centralwidget)
        self.Button_Przelicz.setGeometry(QtCore.QRect(690, 120, 91, 31))
        self.Button_Przelicz.setIcon(icon2)
        self.Button_Przelicz.setIconSize(QtCore.QSize(25, 25))
        self.Button_Przelicz.setObjectName(_fromUtf8("Button_Przelicz"))
        self.lineEdit_wwwPath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_wwwPath.setGeometry(QtCore.QRect(410, 380, 211, 31))
        self.lineEdit_wwwPath.setObjectName(_fromUtf8("lineEdit_wwwPath"))
        self.lineEdit_wwwPath.setVisible(False)
        self.Button_AddWWW = QtGui.QPushButton(self.centralwidget)
        self.Button_AddWWW.setGeometry(QtCore.QRect(630, 380, 91, 31))
        self.Button_AddWWW.setIcon(icon2)
        self.Button_AddWWW.setIconSize(QtCore.QSize(25, 25))
        self.Button_AddWWW.setObjectName(_fromUtf8("Button_AddWWW"))
        self.listWidget_wwwFromMainFile = QtGui.QListWidget(self.centralwidget)
        self.listWidget_wwwFromMainFile.setGeometry(QtCore.QRect(410, 90, 311, 291))
        self.listWidget_wwwFromMainFile.setObjectName(_fromUtf8("listWidget_wwwFromMainFile"))
        self.listWidget_wwwFromMainFile.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuResources = QtGui.QMenu(self.menubar)
        self.menuResources.setObjectName(_fromUtf8("menuResources"))
        self.menuO_programie = QtGui.QMenu(self.menubar)
        self.menuO_programie.setObjectName(_fromUtf8("menuO_programie"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionDodaj_plik = QtGui.QAction(MainWindow)
        self.actionDodaj_plik.setObjectName(_fromUtf8("actionDodaj_plik"))
        self.actionDodaj_WWW = QtGui.QAction(MainWindow)
        self.actionDodaj_WWW.setObjectName(_fromUtf8("actionDodaj_WWW"))
        self.actionUsu_plik = QtGui.QAction(MainWindow)
        self.actionUsu_plik.setObjectName(_fromUtf8("actionUsu_plik"))
        self.actionNowy_projekt = QtGui.QAction(MainWindow)
        self.actionNowy_projekt.setObjectName(_fromUtf8("actionNowy_projekt"))
        self.actionOtw_rz_projekt = QtGui.QAction(MainWindow)
        self.actionOtw_rz_projekt.setObjectName(_fromUtf8("actionOtw_rz_projekt"))
        self.actionDokumentacja = QtGui.QAction(MainWindow)
        self.actionDokumentacja.setObjectName(_fromUtf8("actionDokumentacja"))
        self.menuFile.addAction(self.actionNowy_projekt)
        self.menuFile.addAction(self.actionOtw_rz_projekt)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuResources.addAction(self.actionDodaj_plik)
        self.menuResources.addAction(self.actionDodaj_WWW)
        self.menuResources.addAction(self.actionUsu_plik)
        self.menuO_programie.addAction(self.actionDokumentacja)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuResources.menuAction())
        self.menubar.addAction(self.menuO_programie.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Button_LoadOutFile.setText(_translate("MainWindow", "Dodaj pllik", None))
        self.Button_LoadMainFilePath.setText(_translate("MainWindow", "Nowy projekt", None))
        self.label_numberOfThreshold.setText(_translate("MainWindow", "0", None))
        self.label_20.setText(_translate("MainWindow", "Współczynnik odrzucenia", None))
        self.Button_LoadOutFileCandidateFromWWW.setText(_translate("MainWindow", "Dodaj WWW", None))
        self.comboBox_MethodList.setItemText(0, _translate("MainWindow", "I metoda", None))
        self.comboBox_MethodList.setItemText(1, _translate("MainWindow", "II metoda", None))
        self.Button_RemoveOutFile.setText(_translate("MainWindow", "Usuń plik", None))
        self.Button_LoadConfigPath.setText(_translate("MainWindow", "Otwórz projekt", None))
        self.groupBox.setTitle(_translate("MainWindow", "Statystyka", None))
        self.label_15.setText(_translate("MainWindow", "Ilość zdań w pliku głównym:", None))
        self.label_17.setText(_translate("MainWindow", "Współczynnik plagiatu:", None))
        self.label_16.setText(_translate("MainWindow", "Ilość zdań powtórzonych:", None))
        self.Button_Przelicz.setText(_translate("MainWindow", "Przelicz", None))
        self.Button_AddWWW.setText(_translate("MainWindow", "Dodaj", None))
        self.Button_AddWWW.setVisible(False)
        self.menuFile.setTitle(_translate("MainWindow", "Projekt", None))
        self.menuResources.setTitle(_translate("MainWindow", "Zasoby", None))
        self.menuO_programie.setTitle(_translate("MainWindow", "O programie", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionDodaj_plik.setText(_translate("MainWindow", "Dodaj plik", None))
        self.actionDodaj_WWW.setText(_translate("MainWindow", "Dodaj WWW", None))
        self.actionUsu_plik.setText(_translate("MainWindow", "Usuń plik", None))
        self.actionNowy_projekt.setText(_translate("MainWindow", "Nowy projekt", None))
        self.actionOtw_rz_projekt.setText(_translate("MainWindow", "Otwórz projekt", None))
        self.actionDokumentacja.setText(_translate("MainWindow", "Pomoc", None))

