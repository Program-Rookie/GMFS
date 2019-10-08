# -*- coding: utf-8 -*-

"""
Module implementing yQGeoMagFieldSettingDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog,QApplication,QWidget

from UI.Ui_GeoMagFieldSettingDialog import Ui_yQGeoMagFieldSettingDialog


class yQGeoMagFieldSettingDialog(QDialog, Ui_yQGeoMagFieldSettingDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(yQGeoMagFieldSettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.accept = False

    def set(self, T0, I0, D0):
        self.T0.setText(str(T0))
        self.I0.setText(str(I0))
        self.D0.setText(str(D0))

    def get(self):
        a = int(self.T0.text())
        b = int(self.I0.text())
        c = int(self.D0.text())
        return a, b, c
    
    @pyqtSlot()
    def on_okButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.accept=True
