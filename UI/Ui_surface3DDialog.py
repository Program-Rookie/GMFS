# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyCharm\project\UI\surface3DDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_surface3DDialog(object):
    def setupUi(self, surface3DDialog):
        surface3DDialog.setObjectName("surface3DDialog")
        surface3DDialog.resize(400, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/UI/dialogLogo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        surface3DDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(surface3DDialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.surface3DWgt = MatplotlibWidget(surface3DDialog)
        self.surface3DWgt.setObjectName("surface3DWgt")
        self.verticalLayout.addWidget(self.surface3DWgt)
        self.actionColorFilling = QtWidgets.QAction(surface3DDialog)
        self.actionColorFilling.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/UI/Resources/colorFilling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColorFilling.setIcon(icon1)
        self.actionColorFilling.setObjectName("actionColorFilling")
        self.actionHillShading = QtWidgets.QAction(surface3DDialog)
        self.actionHillShading.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/UI/Resources/HillShading.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHillShading.setIcon(icon2)
        self.actionHillShading.setObjectName("actionHillShading")
        self.actionColorLining = QtWidgets.QAction(surface3DDialog)
        self.actionColorLining.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/UI/Resources/colorLining.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColorLining.setIcon(icon3)
        self.actionColorLining.setObjectName("actionColorLining")
        self.actionSaving = QtWidgets.QAction(surface3DDialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/UI/Resources/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaving.setIcon(icon4)
        self.actionSaving.setObjectName("actionSaving")

        self.retranslateUi(surface3DDialog)
        QtCore.QMetaObject.connectSlotsByName(surface3DDialog)

    def retranslateUi(self, surface3DDialog):
        _translate = QtCore.QCoreApplication.translate
        self.actionColorFilling.setText(_translate("surface3DDialog", "颜色填充"))
        self.actionColorFilling.setToolTip(_translate("surface3DDialog", "是否开启颜色填充"))
        self.actionHillShading.setText(_translate("surface3DDialog", "山体阴影"))
        self.actionHillShading.setToolTip(_translate("surface3DDialog", "是否开启山体阴影"))
        self.actionColorLining.setText(_translate("surface3DDialog", "颜色轮廓"))
        self.actionColorLining.setToolTip(_translate("surface3DDialog", "是否开启颜色轮廓"))
        self.actionSaving.setText(_translate("surface3DDialog", "保存"))
        self.actionSaving.setToolTip(_translate("surface3DDialog", "保存等值线图"))

from UI.matplotlibWidget import MatplotlibWidget
import UI.UI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surface3DDialog = QtWidgets.QDialog()
    ui = Ui_surface3DDialog()
    ui.setupUi(surface3DDialog)
    surface3DDialog.show()
    sys.exit(app.exec_())

