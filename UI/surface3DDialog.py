# -*- coding: utf-8 -*-

"""
Module implementing surface3DDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog,QApplication

from UI.Ui_surface3DDialog import Ui_surface3DDialog


class surface3DDialog(QDialog, Ui_surface3DDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(surface3DDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window|Qt.WindowStaysOnTopHint)
        self.type=1#surface3D

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

if __name__ == "__main__":
    import  sys
    app = QApplication(sys.argv)
    ui =surface3DDialog()
    ui.show()
    sys.exit(app.exec_())