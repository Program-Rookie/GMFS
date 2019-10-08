# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget, QAction, QMessageBox, QWidget
from PyQt5.QtGui import QIcon

from Ui_MainWindow import Ui_MainWindow
from ForwardCenter.ForwardCenterWidget import ForwardCenterWidget
from aboutDlg import AboutDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.centralWidget.setStyleSheet('background-color:white;')
        forwardCenterDockWidget=QDockWidget('正演操作中心')
        forwardCenterDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea)
        forwardCenterDockWidget.setWidget(ForwardCenterWidget())

        self.addDockWidget(Qt.LeftDockWidgetArea,forwardCenterDockWidget)
        actionForwardCenter=forwardCenterDockWidget.toggleViewAction()#Returns a checkable action that can be used to show or close this dock widget.
                                                                      #The action's text is set to the dock widget's window title.
        actionForwardCenter.setIcon(QIcon(':/icons/forwardCenter'))
        self.toolBar.addAction(actionForwardCenter)

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """

        QMessageBox.aboutQt(self)

    @pyqtSlot()
    def on_actionHelp_triggered(self):
        """
        Slot documentation goes here.
        """
        dlg=AboutDialog()
        dlg.exec_()

        # dlg=AboutDlg()
        # dlg.exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
