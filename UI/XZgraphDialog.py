# -*- coding: utf-8 -*-

"""
Module implementing XZgraphDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog

from UI.Ui_XZgraphDialog import Ui_Dialog


class XZgraphDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(XZgraphDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window|Qt.WindowStaysOnTopHint)
        self.type=0#XZgraph
    
    @pyqtSlot()
    def on_actionColorFilling_triggered(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSlot()
    def on_actionHillShading_triggered(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSlot()
    def on_actionColorLining_triggered(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSlot()
    def on_actionSaving_triggered(self):
        """
        Slot documentation goes here.
        """
        pass

    def closeEvent(self, event):
        self.type=None
        del self