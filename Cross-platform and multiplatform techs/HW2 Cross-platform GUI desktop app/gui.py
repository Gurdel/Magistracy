# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 475)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 475))
        MainWindow.setMaximumSize(QtCore.QSize(700, 475))
        MainWindow.setSizeIncrement(QtCore.QSize(700, 475))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 72))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBoxTemplate = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxTemplate.setObjectName("comboBoxTemplate")
        self.comboBoxTemplate.addItem("")
        self.comboBoxTemplate.addItem("")
        self.comboBoxTemplate.addItem("")
        self.gridLayout.addWidget(self.comboBoxTemplate, 0, 1, 1, 2)
        self.paramB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.paramB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramB.setMinimum(-100.0)
        self.paramB.setSingleStep(0.1)
        self.paramB.setProperty("value", 1.0)
        self.paramB.setObjectName("paramB")
        self.gridLayout.addWidget(self.paramB, 3, 1, 1, 1)
        self.paramC = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.paramC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramC.setMinimum(-100.0)
        self.paramC.setSingleStep(0.1)
        self.paramC.setProperty("value", 1.0)
        self.paramC.setObjectName("paramC")
        self.gridLayout.addWidget(self.paramC, 3, 2, 1, 1)
        self.paramA = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.paramA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramA.setMinimum(-100.0)
        self.paramA.setSingleStep(0.1)
        self.paramA.setProperty("value", 3.0)
        self.paramA.setObjectName("paramA")
        self.gridLayout.addWidget(self.paramA, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 231, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.paramNewton_x = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.paramNewton_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramNewton_x.setMinimum(-100.0)
        self.paramNewton_x.setSingleStep(0.1)
        self.paramNewton_x.setProperty("value", 0.0)
        self.paramNewton_x.setObjectName("paramNewton_x")
        self.gridLayout_2.addWidget(self.paramNewton_x, 1, 1, 1, 1)
        self.solveNewton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.solveNewton.setObjectName("solveNewton")
        self.gridLayout_2.addWidget(self.solveNewton, 0, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 220, 231, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.solveDichotomy = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.solveDichotomy.setAutoFillBackground(False)
        self.solveDichotomy.setObjectName("solveDichotomy")
        self.gridLayout_3.addWidget(self.solveDichotomy, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.paramDichotomy_a = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.paramDichotomy_a.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramDichotomy_a.setMinimum(-100.0)
        self.paramDichotomy_a.setSingleStep(0.1)
        self.paramDichotomy_a.setProperty("value", -1.0)
        self.paramDichotomy_a.setObjectName("paramDichotomy_a")
        self.gridLayout_3.addWidget(self.paramDichotomy_a, 2, 0, 1, 1)
        self.paramDichotomy_b = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.paramDichotomy_b.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramDichotomy_b.setMinimum(-100.0)
        self.paramDichotomy_b.setSingleStep(0.1)
        self.paramDichotomy_b.setProperty("value", 1.0)
        self.paramDichotomy_b.setObjectName("paramDichotomy_b")
        self.gridLayout_3.addWidget(self.paramDichotomy_b, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 2)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 340, 231, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.solveSecant = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.solveSecant.setAutoFillBackground(False)
        self.solveSecant.setObjectName("solveSecant")
        self.gridLayout_4.addWidget(self.solveSecant, 0, 2, 1, 1)
        self.paramSecant_x2 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        self.paramSecant_x2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramSecant_x2.setMinimum(-100.0)
        self.paramSecant_x2.setSingleStep(0.1)
        self.paramSecant_x2.setProperty("value", -2.0)
        self.paramSecant_x2.setObjectName("paramSecant_x2")
        self.gridLayout_4.addWidget(self.paramSecant_x2, 2, 0, 1, 1)
        self.paramSecant_x1 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        self.paramSecant_x1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramSecant_x1.setMinimum(-100.0)
        self.paramSecant_x1.setSingleStep(0.1)
        self.paramSecant_x1.setProperty("value", 0.0)
        self.paramSecant_x1.setObjectName("paramSecant_x1")
        self.gridLayout_4.addWidget(self.paramSecant_x1, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 2)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(300, 30, 91, 45))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.paramE = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.paramE.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramE.setDecimals(5)
        self.paramE.setMinimum(1e-05)
        self.paramE.setSingleStep(0.0001)
        self.paramE.setProperty("value", 0.0001)
        self.paramE.setObjectName("paramE")
        self.gridLayout_5.addWidget(self.paramE, 1, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(270, 380, 411, 41))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btnOpenFile = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.gridLayout_6.addWidget(self.btnOpenFile, 0, 0, 1, 1)
        self.btnSaveToFile = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.btnSaveToFile.setObjectName("btnSaveToFile")
        self.gridLayout_6.addWidget(self.btnSaveToFile, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 91, 411, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(100, 100))
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTask = QtWidgets.QAction(MainWindow)
        self.actionTask.setObjectName("actionTask")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menuHelp.addAction(self.actionTask)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAuthor)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EquationSolver"))
        self.label_4.setText(_translate("MainWindow", "Template"))
        self.comboBoxTemplate.setItemText(0, _translate("MainWindow", "A*x + B*cos(x) + C"))
        self.comboBoxTemplate.setItemText(1, _translate("MainWindow", "A*x^2 + B*x + C"))
        self.comboBoxTemplate.setItemText(2, _translate("MainWindow", "A*x * exp(B*x) + C"))
        self.label.setText(_translate("MainWindow", "A"))
        self.label_2.setText(_translate("MainWindow", "B"))
        self.label_3.setText(_translate("MainWindow", "C"))
        self.label_7.setText(_translate("MainWindow", "x0"))
        self.label_8.setText(_translate("MainWindow", "Newton (tangent) method"))
        self.solveNewton.setText(_translate("MainWindow", "solve"))
        self.solveDichotomy.setText(_translate("MainWindow", "solve"))
        self.label_9.setText(_translate("MainWindow", "[ a ;"))
        self.label_11.setText(_translate("MainWindow", " b ]"))
        self.label_10.setText(_translate("MainWindow", "Dichotomy method"))
        self.solveSecant.setText(_translate("MainWindow", "solve"))
        self.label_14.setText(_translate("MainWindow", "X[0-1]"))
        self.label_12.setText(_translate("MainWindow", "X[0-2]"))
        self.label_13.setText(_translate("MainWindow", "Secant (chord) method"))
        self.label_5.setText(_translate("MainWindow", "e"))
        self.btnOpenFile.setText(_translate("MainWindow", "Solve file"))
        self.btnSaveToFile.setText(_translate("MainWindow", "Save to file"))
        self.textBrowser.setMarkdown(_translate("MainWindow", "Welcome!\n"
"\n"
"Choose template, enter template parameters and accuracy e.\n"
"\n"
"Enter numeric method params and click \"solve\" button.\n"
"\n"
"For getting data from file click \"Solve file\" button.\n"
"\n"
"For saving output to file click \"Save to file\" button.\n"
"\n"
"Click \"Menu\" for seeing additional information.\n"
"\n"
""))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose template, enter template parameters and accuracy e.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter numeric method params and click &quot;solve&quot; button.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For getting data from file click &quot;Solve file&quot; button.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For saving output to file click &quot;Save to file&quot; button.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click &quot;Menu&quot; for seeing additional information.</p></body></html>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Menu"))
        self.actionTask.setText(_translate("MainWindow", "Task"))
        self.actionDocumentation.setText(_translate("MainWindow", "Help"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))