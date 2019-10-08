# -*- coding: utf-8 -*-

"""
Module implementing AboutDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_aboutDlg import Ui_Dialog


class AboutDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
