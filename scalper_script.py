# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:35:08 2022

@author: ADMIN
"""

#Installation of Packages
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
import os
import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime


class ScalperKel(QDialog):
    def __init__(self):
        super(ScalperKel, self).__init__()
        loadUi('./UI/main_page.ui', self)
        self.username.textChanged.connect(self.username_tab)
        self.mt5_server.textChanged.connect(self.server_tab)
        self.password.textChanged.connect(self.password_tab)
        self.run.clicked.connect(self.runScalper)

    def username_tab(self):
        try:
            self.user = int(self.username.text())
            print('USERNAME: ', self.user)
            type(self.user)
        except:
            self.username.clear()
            QMessageBox.information(self, "ERROR", "Please put the correct XM/MT5 Account Username!!...")
    
    def server_tab(self):
        self.server = self.mt5_server.text()
        print('SERVER NAME: ', self.server)
        type(self.server)
        
    def password_tab(self):
        self.password_value = self.password.text()
        print('PASSWORD: ', self.password_value)
        #type(self.password_value)
        
    def runScalper(self):
        try:
            QMessageBox.information(self, "ALERT", "Please wait will initialized your account!!...")
            # mt.initialize()
            # init_mt5 = mt.login(self.user, self.password_value, self.server)
            # init_mt5
            #print(init_mt5)
            if not mt5.initialize(login=self.user, server=self.server,password=self.password_value):
                print("initialize() failed, error code =",mt5.last_error())
                #quit()
                QMessageBox.information(self, "ERROR", "initialize() failed, error code =",mt5.last_error())
            else:
                QMessageBox.information(self, "SUCCESSFUL", "Succesfully connected to your MT5 Account!!...")
        except Exception as e:
            QMessageBox.information(self, "ERROR", "Please Properly Check the Username, Password and Server and Make sure that you already open the MT5 Desktop!!...")
            print(e)
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()                   #Stacking all the UI file into one list
    main = ScalperKel()
    widget.addWidget(main)                               #Adding main class into the stackedwidgets
    widget.show()
    sys.exit(app.exec_())  
