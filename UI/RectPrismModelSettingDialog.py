# -*- coding: utf-8 -*-

"""
Module implementing RectPrismModelSettingDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog

from UI.Ui_RectPrismModelSettingDialog import Ui_RectPrismModelSettingDialog


class RectPrismModelSettingDialog(QDialog, Ui_RectPrismModelSettingDialog):
    """
    Class documentation goes here.
    """
    def __init__(self,isMag, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(RectPrismModelSettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.accept = False
        if isMag:
            self.labelProperty.setText("磁化率")
            self.labelUnit.setText('(单位:SI)')
        else:
            self.labelProperty.setText("密度")
            self.labelUnit.setText('(单位:g/cm^3)')

        self.m_isMag = isMag

    def set(self,center,size,property):
        self.centerX.setText(str(center[0]))
        self.centerY.setText(str(center[1]))
        self.centerZ.setText(str(center[2]))
        self.Length.setText(str(size[0]))
        self.Width.setText(str(size[1]))
        self.Height.setText(str(size[2]))
        self.property.setText(str(property))

    def get(self):
        x = int(self.centerX.text())
        y = int(self.centerY.text())
        z = int(self.centerZ.text())

        length=int(self.Length.text())
        width=int(self.Width.text())
        height=int(self.Height.text())

        property=float(self.property.text())
        return [x,y,z],[length,width,height],property
    @pyqtSlot()
    def on_pushButton_OK_clicked(self):
        """
        Slot documentation goes here.
        """
        self.accept = True