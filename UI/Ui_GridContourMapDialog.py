# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyCharm\project\UI\GridContourMapDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GridContourMapDialog(object):
    def setupUi(self, GridContourMapDialog):
        GridContourMapDialog.setObjectName("GridContourMapDialog")
        GridContourMapDialog.resize(400, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/UI/dialogLogo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GridContourMapDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(GridContourMapDialog)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.contourMapWgt = MatplotlibWidget(GridContourMapDialog)
        self.contourMapWgt.setObjectName("contourMapWgt")
        self.gridLayout.addWidget(self.contourMapWgt, 0, 0, 1, 2)
        self.actionColorFilling = QtWidgets.QAction(GridContourMapDialog)
        self.actionColorFilling.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/UI/Resources/colorFilling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColorFilling.setIcon(icon1)
        self.actionColorFilling.setObjectName("actionColorFilling")
        self.actionHillShading = QtWidgets.QAction(GridContourMapDialog)
        self.actionHillShading.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/UI/Resources/HillShading.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHillShading.setIcon(icon2)
        self.actionHillShading.setObjectName("actionHillShading")
        self.actionColorLining = QtWidgets.QAction(GridContourMapDialog)
        self.actionColorLining.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/UI/Resources/colorLining.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColorLining.setIcon(icon3)
        self.actionColorLining.setObjectName("actionColorLining")
        self.actionSaving = QtWidgets.QAction(GridContourMapDialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/UI/Resources/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaving.setIcon(icon4)
        self.actionSaving.setObjectName("actionSaving")

        self.retranslateUi(GridContourMapDialog)
        QtCore.QMetaObject.connectSlotsByName(GridContourMapDialog)

    def retranslateUi(self, GridContourMapDialog):
        _translate = QtCore.QCoreApplication.translate
        self.actionColorFilling.setText(_translate("GridContourMapDialog", "颜色填充"))
        self.actionColorFilling.setToolTip(_translate("GridContourMapDialog", "是否开启颜色填充"))
        self.actionHillShading.setText(_translate("GridContourMapDialog", "山体阴影"))
        self.actionHillShading.setToolTip(_translate("GridContourMapDialog", "是否开启山体阴影"))
        self.actionColorLining.setText(_translate("GridContourMapDialog", "颜色轮廓"))
        self.actionColorLining.setToolTip(_translate("GridContourMapDialog", "是否开启颜色轮廓"))
        self.actionSaving.setText(_translate("GridContourMapDialog", "保存"))
        self.actionSaving.setToolTip(_translate("GridContourMapDialog", "保存等值线图"))

from UI.matplotlibWidget import MatplotlibWidget
import UI.UI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GridContourMapDialog = QtWidgets.QDialog()
    ui = Ui_GridContourMapDialog()
    ui.setupUi(GridContourMapDialog)
    GridContourMapDialog.show()
    sys.exit(app.exec_())

