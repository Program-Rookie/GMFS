# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyCharm\project\UI\GridSettingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GridSettingDialog(object):
    def setupUi(self, GridSettingDialog):
        GridSettingDialog.setObjectName("GridSettingDialog")
        GridSettingDialog.resize(250, 243)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/UI/dialogLogo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GridSettingDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(GridSettingDialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(GridSettingDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_yMin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_yMin.setObjectName("lineEdit_yMin")
        self.gridLayout.addWidget(self.lineEdit_yMin, 1, 1, 1, 1)
        self.lineEdit_xMin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_xMin.setObjectName("lineEdit_xMin")
        self.gridLayout.addWidget(self.lineEdit_xMin, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.lineEdit_xMax = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_xMax.setObjectName("lineEdit_xMax")
        self.gridLayout.addWidget(self.lineEdit_xMax, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.lineEdit_yMax = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_yMax.setObjectName("lineEdit_yMax")
        self.gridLayout.addWidget(self.lineEdit_yMax, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(GridSettingDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.spinBox_rows = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_rows.setObjectName("spinBox_rows")
        self.gridLayout_2.addWidget(self.spinBox_rows, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.spinBox_cols = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_cols.setObjectName("spinBox_cols")
        self.gridLayout_2.addWidget(self.spinBox_cols, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.okButton = QtWidgets.QPushButton(GridSettingDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/UI/apply"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okButton.setIcon(icon1)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(GridSettingDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/UI/cancel"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GridSettingDialog)
        self.cancelButton.clicked.connect(GridSettingDialog.reject)
        self.okButton.clicked.connect(GridSettingDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(GridSettingDialog)
        GridSettingDialog.setTabOrder(self.lineEdit_xMin, self.lineEdit_xMax)
        GridSettingDialog.setTabOrder(self.lineEdit_xMax, self.lineEdit_yMin)
        GridSettingDialog.setTabOrder(self.lineEdit_yMin, self.lineEdit_yMax)
        GridSettingDialog.setTabOrder(self.lineEdit_yMax, self.spinBox_rows)
        GridSettingDialog.setTabOrder(self.spinBox_rows, self.spinBox_cols)
        GridSettingDialog.setTabOrder(self.spinBox_cols, self.okButton)
        GridSettingDialog.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, GridSettingDialog):
        _translate = QtCore.QCoreApplication.translate
        GridSettingDialog.setWindowTitle(_translate("GridSettingDialog", "网格几何参数设置"))
        self.groupBox_2.setTitle(_translate("GridSettingDialog", "网格坐标范围"))
        self.label_4.setText(_translate("GridSettingDialog", "yMax"))
        self.label.setText(_translate("GridSettingDialog", "xMin"))
        self.label_2.setText(_translate("GridSettingDialog", "xMax"))
        self.label_3.setText(_translate("GridSettingDialog", "yMin"))
        self.groupBox.setTitle(_translate("GridSettingDialog", "网格大小"))
        self.label_5.setText(_translate("GridSettingDialog", "行数"))
        self.label_6.setText(_translate("GridSettingDialog", "列数"))
        self.okButton.setText(_translate("GridSettingDialog", "确定"))
        self.cancelButton.setText(_translate("GridSettingDialog", "取消"))

import UI.UI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GridSettingDialog = QtWidgets.QDialog()
    ui = Ui_GridSettingDialog()
    ui.setupUi(GridSettingDialog)
    GridSettingDialog.show()
    sys.exit(app.exec_())

