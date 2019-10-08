# -*- coding: utf-8 -*-

"""
Module implementing GridContourMapDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog,QApplication,QSizePolicy,QWidget

from UI.Ui_GridContourMapDialog import Ui_GridContourMapDialog

class GridContourMapDialog(QDialog, Ui_GridContourMapDialog):
    """
    Class documentation goes here.
    """
    def __init__(self,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(GridContourMapDialog, self).__init__(parent)
        self.setupUi(self)
        # self.setStyleSheet('background-color:white;')
        self.setWindowFlags(Qt.Window|Qt.WindowStaysOnTopHint)#WindowMinimizeButtonHint,Qt.WindowMaximizeButtonHint,Qt.WindowCloseButtonHint)
        self.type=0#contourMap

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

    # @pyqtSlot(str)
    # def on_comboBox_currentIndexChanged(self, p0):
    #     """
    #     Slot documentation goes here.
    #
    #     @param p0 DESCRIPTION
    #     @type str
    #     """
    #     self.contourMapWgt.mpl.setCmap(p0)
    #     pass

    def closeEvent(self, event):
        self.type=None
        del self


if __name__ == "__main__":
    import  sys
    app = QApplication(sys.argv)
    ui =GridContourMapDialog()
    ui.show()
    sys.exit(app.exec_())
    

