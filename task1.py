# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xyz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QDockWidget, QApplication, QMessageBox, QColorDialog, QCheckBox, QDial, QMenu, QActionGroup,
   #                          QAction, QTextEdit, QFileDialog, QSlider, QLCDNumber, QLabel, QPushButton, QGridLayout, QDialog, QMenuBar, QStatusBar, QWidget, QComboBox, QRadioButton) 
import pandas as pd
from pyqtgraph import PlotWidget
import os 
import pathlib


class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 0, 85, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 0, 85, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 0, 85, 71))
        self.pushButton_3.setObjectName("pushButton_3")


        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 80, 781, 451))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuchannel_1 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_1.setObjectName("menuchannel_1")
        self.menuchannel_2 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_2.setObjectName("menuchannel_2")
        self.menuchannel_3 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_3.setObjectName("menuchannel_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_channel_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_channel_2.setObjectName("actionopen_channel_2")
        self.actionopen_channel_1 = QtWidgets.QAction(MainWindow)
        self.actionopen_channel_1.setCheckable(False)
        self.actionopen_channel_1.setWhatsThis("")
        self.actionopen_channel_1.setObjectName("actionopen_channel_1")
        self.actionopen_channel_3 = QtWidgets.QAction(MainWindow)
        self.actionopen_channel_3.setObjectName("actionopen_channel_3")
        self.menuchannel_1.addAction(self.actionopen_channel_1)
        self.menuchannel_2.addAction(self.actionopen_channel_2)
        self.menuchannel_3.addAction(self.actionopen_channel_3)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuchannel_1.menuAction())
        self.menubar.addAction(self.menuchannel_2.menuAction())
        self.menubar.addAction(self.menuchannel_3.menuAction())


        #self.pushButton.clicked.connect(lambda : self.open_sheet())

        self.actionopen_channel_1.triggered.connect(lambda : self.open_sheet())
        self.pushButton_3.clicked.connect(lambda : self.reset())

        self.actionopen_channel_2.triggered.connect(lambda : self.open_sheet())

        self.actionopen_channel_3.triggered.connect(lambda : self.open_sheet())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Resume"))
        self.pushButton_2.setText(_translate("MainWindow", "pause"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuchannel_1.setTitle(_translate("MainWindow", "channel 1"))
        self.menuchannel_2.setTitle(_translate("MainWindow", "channel 2"))
        self.menuchannel_3.setTitle(_translate("MainWindow", "channel 3"))
        self.actionopen_channel_2.setText(_translate("MainWindow", "open channel 2"))
        self.actionopen_channel_1.setText(_translate("MainWindow", "open channel 1"))
        self.actionopen_channel_3.setText(_translate("MainWindow", "open channel 3"))
    def open_sheet(self):
        fname = QtGui.QFileDialog.getOpenFileName( self, 'Open only txt or CSV', os.getenv('HOME') )
        #path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'))
        path = fname[0]
        if pathlib.Path(path).suffix == ".txt" :
            self.show_txt(path)
        elif pathlib.Path(path).suffix == ".csv" :
            self.show_csv(path)
       

    def show_csv(self,path) :

        y= pd.read_csv(path,  header=None).values
        y=np.squeeze(y)
        x = np.arange(0,np.prod(y.shape))
        self.graphicsView.plot(x,y)

            

        
    
    def show_txt(self,path) :
        data = np.genfromtxt(path, delimiter = ',')
        x= data[: , 0]
        y =data[: , 1]
        self.graphicsView.plot(x,y)


    def reset(self) :
        self.graphicsView.clear()
    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
