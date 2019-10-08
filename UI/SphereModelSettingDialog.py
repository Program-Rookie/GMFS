# -*- coding: utf-8 -*-

"""
Module implementing SphereModelSettingDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog

from UI.Ui_SphereModelSettingDialog import Ui_SphereModelSettingDialog


class SphereModelSettingDialog(QDialog, Ui_SphereModelSettingDialog):
    """
    Class documentation goes here.
    """
    def __init__(self,isMag,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SphereModelSettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.accept = False
        if isMag:
            self.labelProperty.setText("磁化率")
            self.labelUnit.setText('(单位:SI)')
        else:
            self.labelProperty.setText("密度")
            self.labelUnit.setText('(单位:g/cm^3)')

        self.m_isMag=isMag

    def set(self,center,radius,property):
        self.centerX.setText(str(center[0]))
        self.centerY.setText(str(center[1]))
        self.centerZ.setText(str(center[2]))
        self.radius.setText(str(radius))
        self.property.setText(str(property))

    def get(self):
        x = int(self.centerX.text())
        y = int(self.centerY.text())
        z = int(self.centerZ.text())
        radius=int(self.radius.text())
        property=float(self.property.text())
        return [x,y,z], radius,property
    @pyqtSlot()
    def on_okButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.accept = True