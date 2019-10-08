# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyCharm\project\UI\XZgraphDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/UI/dialogLogo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.XZgraphWgt = MatplotlibWidget(Dialog)
        self.XZgraphWgt.setObjectName("XZgraphWgt")
        self.verticalLayout.addWidget(self.XZgraphWgt)
        self.actionColorFilling = QtWidgets.QAction(Dialog)
        self.actionColorFilling.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/UI/Resources/colorFilling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColorFilling.setIcon(icon1)
        self.actionColorFilling.setObjectName("actionColorFilling")
        self.actionHillShading = QtWidgets.QAction(Dialog)
        self.actionHillShading.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/UI/Resources/HillShading.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHillShading.setIcon(icon2)
        self.actionHillShading.setObjectName("actionHillShading")
        self.actionColorLining = QtWidgets.QAction(Dialog)
        self.actionColorLining.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/UI/Resources/colorLining.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColorLining.setIcon(icon3)
        self.actionColorLining.setObjectName("actionColorLining")
        self.actionSaving = QtWidgets.QAction(Dialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/UI/Resources/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaving.setIcon(icon4)
        self.actionSaving.setObjectName("actionSaving")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.actionColorFilling.setText(_translate("Dialog", "颜色填充"))
        self.actionColorFilling.setToolTip(_translate("Dialog", "是否开启颜色填充"))
        self.actionHillShading.setText(_translate("Dialog", "山体阴影"))
        self.actionHillShading.setToolTip(_translate("Dialog", "是否开启山体阴影"))
        self.actionColorLining.setText(_translate("Dialog", "颜色轮廓"))
        self.actionColorLining.setToolTip(_translate("Dialog", "是否开启颜色轮廓"))
        self.actionSaving.setText(_translate("Dialog", "保存"))
        self.actionSaving.setToolTip(_translate("Dialog", "保存成grd文件"))

from UI.matplotlibWidget import MatplotlibWidget
import UI.UI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

