# -*- coding: utf-8 -*-

"""
Module implementing GridSettingDialog.
"""

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog, QMenu,QApplication

from UI.Ui_GridSettingDialog import Ui_GridSettingDialog


class GridSettingDialog(QDialog, Ui_GridSettingDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(GridSettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.accept = False

    def set(self,xyRanges,size):
        self.lineEdit_xMin.setText(str(xyRanges[0]))
        self.lineEdit_xMax.setText(str(xyRanges[1]))
        self.lineEdit_yMin.setText(str(xyRanges[2]))
        self.lineEdit_yMax.setText(str(xyRanges[3]))
        self.spinBox_rows.setValue(size[0])
        self.spinBox_cols.setValue(size[1])

    def get(self):
        xMin=int(self.lineEdit_xMin.text())
        xMax=int(self.lineEdit_xMax.text())
        yMin=int(self.lineEdit_yMin.text())
        yMax=int(self.lineEdit_yMax.text())
        rows=self.spinBox_rows.value()
        cols=self.spinBox_cols.value()
        return [xMin,xMax,yMin,yMax],[rows,cols]
    
    @pyqtSlot()
    def on_okButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.accept=True

if __name__ == "__main__":
    import  sys
    app = QApplication(sys.argv)
    ui =GridSettingDialog()
    ui.show()
    sys.exit(app.exec_())