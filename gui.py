# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Jun 03 21:18:53 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(1000, 700)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-20, -10, 1041, 741))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.Loading = QtGui.QWidget()
        self.Loading.setObjectName(_fromUtf8("Loading"))
        self.label_3 = QtGui.QLabel(self.Loading)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 791, 451))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("Image/main.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar_StartProgram = QtGui.QProgressBar(self.Loading)
        self.progressBar_StartProgram.setGeometry(QtCore.QRect(150, 440, 451, 23))
        self.progressBar_StartProgram.setAutoFillBackground(False)
        self.progressBar_StartProgram.setProperty("value", 0)
        self.progressBar_StartProgram.setTextVisible(False)
        self.progressBar_StartProgram.setObjectName(_fromUtf8("progressBar_StartProgram"))
        self.testButton = QtGui.QPushButton(self.Loading)
        self.testButton.setGeometry(QtCore.QRect(240, 10, 131, 23))
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.stackedWidget.addWidget(self.Loading)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.Button_Next1 = QtGui.QPushButton(self.page)
        self.Button_Next1.setGeometry(QtCore.QRect(550, 540, 201, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(20)
        self.Button_Next1.setFont(font)
        self.Button_Next1.setObjectName(_fromUtf8("Button_Next1"))
        self.radioButton_new = QtGui.QRadioButton(self.page)
        self.radioButton_new.setGeometry(QtCore.QRect(60, 140, 82, 17))
        self.radioButton_new.setObjectName(_fromUtf8("radioButton_new"))
        self.radioButton_loadOld = QtGui.QRadioButton(self.page)
        self.radioButton_loadOld.setGeometry(QtCore.QRect(50, 370, 121, 41))
        self.radioButton_loadOld.setObjectName(_fromUtf8("radioButton_loadOld"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(600, 80, 361, 241))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-g3105-782.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(800, 390, 221, 211))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("Image/spinacz.png")))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(790, 320, 61, 51))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/rafal/Desktop/Rysunek.svg-g3105-782.png")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(830, 370, 21, 21))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/rafal/Desktop/Rysunek.svg-g3105-782.png")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(180, 60, 401, 211))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-rect3152-5-157.png")))
        self.label_10.setScaledContents(True)
        self.label_10.setIndent(-2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(180, 290, 401, 211))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-rect3152-5-157.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setIndent(-1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(670, 100, 241, 121))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_LoadMainFile_Name = QtGui.QLineEdit(self.page)
        self.lineEdit_LoadMainFile_Name.setGeometry(QtCore.QRect(340, 110, 201, 21))
        self.lineEdit_LoadMainFile_Name.setObjectName(_fromUtf8("lineEdit_LoadMainFile_Name"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(210, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(200, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Button_LoadMainFilePath = QtGui.QPushButton(self.page)
        self.Button_LoadMainFilePath.setEnabled(True)
        self.Button_LoadMainFilePath.setGeometry(QtCore.QRect(440, 160, 101, 31))
        self.Button_LoadMainFilePath.setObjectName(_fromUtf8("Button_LoadMainFilePath"))
        self.Line_LoadMainFile_Path = QtGui.QLineEdit(self.page)
        self.Line_LoadMainFile_Path.setEnabled(True)
        self.Line_LoadMainFile_Path.setGeometry(QtCore.QRect(200, 210, 341, 21))
        self.Line_LoadMainFile_Path.setReadOnly(True)
        self.Line_LoadMainFile_Path.setObjectName(_fromUtf8("Line_LoadMainFile_Path"))
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(200, 360, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Button_LoadConfigPath = QtGui.QPushButton(self.page)
        self.Button_LoadConfigPath.setEnabled(True)
        self.Button_LoadConfigPath.setGeometry(QtCore.QRect(440, 380, 101, 31))
        self.Button_LoadConfigPath.setObjectName(_fromUtf8("Button_LoadConfigPath"))
        self.Line_LoadConfig_Path = QtGui.QLineEdit(self.page)
        self.Line_LoadConfig_Path.setEnabled(True)
        self.Line_LoadConfig_Path.setGeometry(QtCore.QRect(200, 420, 341, 21))
        self.Line_LoadConfig_Path.setReadOnly(True)
        self.Line_LoadConfig_Path.setObjectName(_fromUtf8("Line_LoadConfig_Path"))
        self.Button_Podglad = QtGui.QPushButton(self.page)
        self.Button_Podglad.setEnabled(True)
        self.Button_Podglad.setGeometry(QtCore.QRect(440, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.Button_Podglad.setFont(font)
        self.Button_Podglad.setObjectName(_fromUtf8("Button_Podglad"))
        self.Button_Podglad2 = QtGui.QPushButton(self.page)
        self.Button_Podglad2.setEnabled(True)
        self.Button_Podglad2.setGeometry(QtCore.QRect(440, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.Button_Podglad2.setFont(font)
        self.Button_Podglad2.setObjectName(_fromUtf8("Button_Podglad2"))
        self.listWidget_MainFile_Podglad = QtGui.QListWidget(self.page)
        self.listWidget_MainFile_Podglad.setGeometry(QtCore.QRect(80, 20, 681, 571))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.listWidget_MainFile_Podglad.setFont(font)
        self.listWidget_MainFile_Podglad.setProperty("isWrapping", False)
        self.listWidget_MainFile_Podglad.setWordWrap(True)
        self.listWidget_MainFile_Podglad.setObjectName(_fromUtf8("listWidget_MainFile_Podglad"))
        self.Button_ClosePodglad = QtGui.QPushButton(self.page)
        self.Button_ClosePodglad.setEnabled(True)
        self.Button_ClosePodglad.setGeometry(QtCore.QRect(640, 550, 101, 31))
        self.Button_ClosePodglad.setObjectName(_fromUtf8("Button_ClosePodglad"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.Button_ShowRaport = QtGui.QPushButton(self.page_2)
        self.Button_ShowRaport.setGeometry(QtCore.QRect(550, 540, 201, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(20)
        self.Button_ShowRaport.setFont(font)
        self.Button_ShowRaport.setObjectName(_fromUtf8("Button_ShowRaport"))
        self.Button_BackToPage_1 = QtGui.QPushButton(self.page_2)
        self.Button_BackToPage_1.setGeometry(QtCore.QRect(60, 540, 201, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(20)
        self.Button_BackToPage_1.setFont(font)
        self.Button_BackToPage_1.setIconSize(QtCore.QSize(32, 32))
        self.Button_BackToPage_1.setObjectName(_fromUtf8("Button_BackToPage_1"))
        self.label_23 = QtGui.QLabel(self.page_2)
        self.label_23.setGeometry(QtCore.QRect(30, 40, 711, 401))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAutoFillBackground(False)
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-rect3038-977.png")))
        self.label_23.setScaledContents(True)
        self.label_23.setWordWrap(False)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.Button_LoadOutFileCandidate = QtGui.QPushButton(self.page_2)
        self.Button_LoadOutFileCandidate.setGeometry(QtCore.QRect(60, 310, 81, 71))
        self.Button_LoadOutFileCandidate.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-path3297-4294966409.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_LoadOutFileCandidate.setIcon(icon)
        self.Button_LoadOutFileCandidate.setIconSize(QtCore.QSize(50, 50))
        self.Button_LoadOutFileCandidate.setObjectName(_fromUtf8("Button_LoadOutFileCandidate"))
        self.Button_RemoveOutFileCandidate = QtGui.QPushButton(self.page_2)
        self.Button_RemoveOutFileCandidate.setGeometry(QtCore.QRect(230, 310, 81, 71))
        self.Button_RemoveOutFileCandidate.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-path3297-4294966531.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_RemoveOutFileCandidate.setIcon(icon1)
        self.Button_RemoveOutFileCandidate.setIconSize(QtCore.QSize(50, 50))
        self.Button_RemoveOutFileCandidate.setObjectName(_fromUtf8("Button_RemoveOutFileCandidate"))
        self.listWidget_OutFiles = QtGui.QListWidget(self.page_2)
        self.listWidget_OutFiles.setGeometry(QtCore.QRect(460, 90, 256, 192))
        self.listWidget_OutFiles.setProperty("isWrapping", False)
        self.listWidget_OutFiles.setObjectName(_fromUtf8("listWidget_OutFiles"))
        self.Button_LoadOutFileCandidateFromWWW = QtGui.QPushButton(self.page_2)
        self.Button_LoadOutFileCandidateFromWWW.setGeometry(QtCore.QRect(150, 310, 81, 71))
        self.Button_LoadOutFileCandidateFromWWW.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-path3008-154.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_LoadOutFileCandidateFromWWW.setIcon(icon2)
        self.Button_LoadOutFileCandidateFromWWW.setIconSize(QtCore.QSize(50, 50))
        self.Button_LoadOutFileCandidateFromWWW.setObjectName(_fromUtf8("Button_LoadOutFileCandidateFromWWW"))
        self.label_13 = QtGui.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(80, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.listWidget_CandidateOutFiles = QtGui.QListWidget(self.page_2)
        self.listWidget_CandidateOutFiles.setGeometry(QtCore.QRect(60, 90, 256, 192))
        self.listWidget_CandidateOutFiles.setObjectName(_fromUtf8("listWidget_CandidateOutFiles"))
        self.Button_RemoveOutFile = QtGui.QPushButton(self.page_2)
        self.Button_RemoveOutFile.setGeometry(QtCore.QRect(480, 310, 81, 71))
        self.Button_RemoveOutFile.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/rafal/Desktop/PlagiatDrawable/Rysunek.svg-path3297-4294966531.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_RemoveOutFile.setIcon(icon3)
        self.Button_RemoveOutFile.setIconSize(QtCore.QSize(50, 50))
        self.Button_RemoveOutFile.setObjectName(_fromUtf8("Button_RemoveOutFile"))
        self.label_21 = QtGui.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(170, 370, 51, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.Button_AddOutFromCandidate = QtGui.QPushButton(self.page_2)
        self.Button_AddOutFromCandidate.setGeometry(QtCore.QRect(330, 180, 111, 51))
        self.Button_AddOutFromCandidate.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Image/Rysunek.svg-path3010-4294966726.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_AddOutFromCandidate.setIcon(icon4)
        self.Button_AddOutFromCandidate.setIconSize(QtCore.QSize(100, 50))
        self.Button_AddOutFromCandidate.setObjectName(_fromUtf8("Button_AddOutFromCandidate"))
        self.label_14 = QtGui.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(490, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.listWidget_wwwFromMainFile = QtGui.QListWidget(self.page_2)
        self.listWidget_wwwFromMainFile.setGeometry(QtCore.QRect(460, 90, 311, 331))
        self.listWidget_wwwFromMainFile.setObjectName(_fromUtf8("listWidget_wwwFromMainFile"))
        self.label_22 = QtGui.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(500, 380, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.listWidget_MainFile = QtGui.QListWidget(self.page_3)
        self.listWidget_MainFile.setGeometry(QtCore.QRect(40, 210, 431, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.listWidget_MainFile.setFont(font)
        self.listWidget_MainFile.setProperty("isWrapping", False)
        self.listWidget_MainFile.setWordWrap(True)
        self.listWidget_MainFile.setObjectName(_fromUtf8("listWidget_MainFile"))
        self.listWidget_OutFilesList = QtGui.QListWidget(self.page_3)
        self.listWidget_OutFilesList.setGeometry(QtCore.QRect(480, 110, 381, 61))
        self.listWidget_OutFilesList.setObjectName(_fromUtf8("listWidget_OutFilesList"))
        self.listWidget_ChoosenOutFile = QtGui.QListWidget(self.page_3)
        self.listWidget_ChoosenOutFile.setGeometry(QtCore.QRect(480, 210, 391, 291))
        self.listWidget_ChoosenOutFile.setWordWrap(True)
        self.listWidget_ChoosenOutFile.setObjectName(_fromUtf8("listWidget_ChoosenOutFile"))
        self.Button_BackToPage_2 = QtGui.QPushButton(self.page_3)
        self.Button_BackToPage_2.setGeometry(QtCore.QRect(60, 540, 201, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(20)
        self.Button_BackToPage_2.setFont(font)
        self.Button_BackToPage_2.setObjectName(_fromUtf8("Button_BackToPage_2"))
        self.label_numberOfSentences = QtGui.QLabel(self.page_3)
        self.label_numberOfSentences.setGeometry(QtCore.QRect(290, 40, 111, 31))
        self.label_numberOfSentences.setObjectName(_fromUtf8("label_numberOfSentences"))
        self.label_numberOfRepeatSentences = QtGui.QLabel(self.page_3)
        self.label_numberOfRepeatSentences.setGeometry(QtCore.QRect(290, 90, 111, 31))
        self.label_numberOfRepeatSentences.setObjectName(_fromUtf8("label_numberOfRepeatSentences"))
        self.label_repeatSentencesProcent = QtGui.QLabel(self.page_3)
        self.label_repeatSentencesProcent.setGeometry(QtCore.QRect(290, 130, 111, 31))
        self.label_repeatSentencesProcent.setObjectName(_fromUtf8("label_repeatSentencesProcent"))
        self.comboBox_MethodList = QtGui.QComboBox(self.page_3)
        self.comboBox_MethodList.setGeometry(QtCore.QRect(510, 80, 69, 22))
        self.comboBox_MethodList.setObjectName(_fromUtf8("comboBox_MethodList"))
        self.comboBox_MethodList.addItem(_fromUtf8(""))
        self.comboBox_MethodList.addItem(_fromUtf8(""))
        self.horizontalSlider_Threshold = QtGui.QSlider(self.page_3)
        self.horizontalSlider_Threshold.setGeometry(QtCore.QRect(630, 80, 160, 19))
        self.horizontalSlider_Threshold.setMinimum(1)
        self.horizontalSlider_Threshold.setMaximum(100)
        self.horizontalSlider_Threshold.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Threshold.setObjectName(_fromUtf8("horizontalSlider_Threshold"))
        self.label_15 = QtGui.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(50, 40, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(50, 80, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(50, 120, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(220, 170, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(610, 170, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.page_3)
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QtCore.QRect(630, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_numberOfThreshold = QtGui.QLabel(self.page_3)
        self.label_numberOfThreshold.setGeometry(QtCore.QRect(800, 70, 111, 31))
        self.label_numberOfThreshold.setObjectName(_fromUtf8("label_numberOfThreshold"))
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.radioButton_new, self.radioButton_loadOld)
        MainWindow.setTabOrder(self.radioButton_loadOld, self.lineEdit_LoadMainFile_Name)
        MainWindow.setTabOrder(self.lineEdit_LoadMainFile_Name, self.Button_LoadMainFilePath)
        MainWindow.setTabOrder(self.Button_LoadMainFilePath, self.Line_LoadMainFile_Path)
        MainWindow.setTabOrder(self.Line_LoadMainFile_Path, self.Button_LoadConfigPath)
        MainWindow.setTabOrder(self.Button_LoadConfigPath, self.Line_LoadConfig_Path)
        MainWindow.setTabOrder(self.Line_LoadConfig_Path, self.testButton)
        MainWindow.setTabOrder(self.testButton, self.Button_ShowRaport)
        MainWindow.setTabOrder(self.Button_ShowRaport, self.Button_BackToPage_1)
        MainWindow.setTabOrder(self.Button_BackToPage_1, self.listWidget_MainFile)
        MainWindow.setTabOrder(self.listWidget_MainFile, self.listWidget_OutFilesList)
        MainWindow.setTabOrder(self.listWidget_OutFilesList, self.listWidget_ChoosenOutFile)
        MainWindow.setTabOrder(self.listWidget_ChoosenOutFile, self.Button_BackToPage_2)
        MainWindow.setTabOrder(self.Button_BackToPage_2, self.comboBox_MethodList)
        MainWindow.setTabOrder(self.comboBox_MethodList, self.horizontalSlider_Threshold)
        MainWindow.setTabOrder(self.horizontalSlider_Threshold, self.Button_Next1)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.testButton.setText(_translate("MainWindow", "spamToLoadButton XD", None))
        self.Button_Next1.setText(_translate("MainWindow", "Dalej", None))
        self.radioButton_new.setText(_translate("MainWindow", "Nowy projekt", None))
        self.radioButton_loadOld.setText(_translate("MainWindow", "Istnięjący projekt", None))
        self.label_12.setText(_translate("MainWindow", "CZESC JESTEM KAMIL JEBAC GETERY", None))
        self.label.setText(_translate("MainWindow", "Nazwa projektu :", None))
        self.label_5.setText(_translate("MainWindow", "Wprowadź plik referencyjny", None))
        self.Button_LoadMainFilePath.setText(_translate("MainWindow", "Odtwórz", None))
        self.Line_LoadMainFile_Path.setPlaceholderText(_translate("MainWindow", "Ścieżka do pliku", None))
        self.label_6.setText(_translate("MainWindow", "Ścieżka do projektu", None))
        self.Button_LoadConfigPath.setText(_translate("MainWindow", "Odtwórz", None))
        self.Line_LoadConfig_Path.setPlaceholderText(_translate("MainWindow", "Ścieżka do istniejącego projektu", None))
        self.Button_Podglad.setText(_translate("MainWindow", "Podgląd", None))
        self.Button_Podglad2.setText(_translate("MainWindow", "Podgląd", None))
        self.Button_ClosePodglad.setText(_translate("MainWindow", "Zamknij", None))
        self.Button_ShowRaport.setText(_translate("MainWindow", "Raport", None))
        self.Button_BackToPage_1.setText(_translate("MainWindow", "Powrót", None))
        self.label_13.setText(_translate("MainWindow", "Zasoby do porówniania", None))
        self.label_21.setText(_translate("MainWindow", "WWW", None))
        self.label_14.setText(_translate("MainWindow", "Przetworzone zasoby", None))
        self.label_22.setText(_translate("MainWindow", "Kliknij dwukrotnie, aby dodać", None))
        self.Button_BackToPage_2.setText(_translate("MainWindow", "Powrót", None))
        self.label_numberOfSentences.setText(_translate("MainWindow", "TextLabel", None))
        self.label_numberOfRepeatSentences.setText(_translate("MainWindow", "TextLabel", None))
        self.label_repeatSentencesProcent.setText(_translate("MainWindow", "TextLabel", None))
        self.comboBox_MethodList.setItemText(0, _translate("MainWindow", "I metoda", None))
        self.comboBox_MethodList.setItemText(1, _translate("MainWindow", "II metoda", None))
        self.label_15.setText(_translate("MainWindow", "Ilość zdań w pliku głównym:", None))
        self.label_16.setText(_translate("MainWindow", "Ilość zdań powtórzonych:", None))
        self.label_17.setText(_translate("MainWindow", "Współczynnik plagiatu:", None))
        self.label_18.setText(_translate("MainWindow", "Plik główny", None))
        self.label_19.setText(_translate("MainWindow", "Plik porównywany", None))
        self.label_20.setText(_translate("MainWindow", "Współczynnik odrzucenia", None))
        self.label_numberOfThreshold.setText(_translate("MainWindow", "TextLabel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

