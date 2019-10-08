# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\selflearning\project2019\UI\Grid3DSurfaceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_yQGrid3DSurfaceDialog(object):
    def setupUi(self, yQGrid3DSurfaceDialog):
        yQGrid3DSurfaceDialog.setObjectName("yQGrid3DSurfaceDialog")
        yQGrid3DSurfaceDialog.resize(520, 384)
        self.verticalLayout = QtWidgets.QVBoxLayout(yQGrid3DSurfaceDialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(yQGrid3DSurfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QtGui.QPixmap(":/UI/Resources/colorTable.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_clrTbl_presets = yColorTablePresetsComboBox(yQGrid3DSurfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_clrTbl_presets.sizePolicy().hasHeightForWidth())
        self.comboBox_clrTbl_presets.setSizePolicy(sizePolicy)
        self.comboBox_clrTbl_presets.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_clrTbl_presets.setObjectName("comboBox_clrTbl_presets")
        self.horizontalLayout.addWidget(self.comboBox_clrTbl_presets)
        self.slider = QtWidgets.QSlider(yQGrid3DSurfaceDialog)
        self.slider.setProperty("value", 50)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.horizontalLayout.addWidget(self.slider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(yQGrid3DSurfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.HLayout_Surface_ClrTableSpectrum = QtWidgets.QHBoxLayout()
        self.HLayout_Surface_ClrTableSpectrum.setSpacing(6)
        self.HLayout_Surface_ClrTableSpectrum.setObjectName("HLayout_Surface_ClrTableSpectrum")
        self.clrTblSpectrumWidget = yColorTableSpectrumWidget(yQGrid3DSurfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clrTblSpectrumWidget.sizePolicy().hasHeightForWidth())
        self.clrTblSpectrumWidget.setSizePolicy(sizePolicy)
        self.clrTblSpectrumWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.clrTblSpectrumWidget.setObjectName("clrTblSpectrumWidget")
        self.HLayout_Surface_ClrTableSpectrum.addWidget(self.clrTblSpectrumWidget)
        self.verticalLayout.addLayout(self.HLayout_Surface_ClrTableSpectrum)

        self.retranslateUi(yQGrid3DSurfaceDialog)
        QtCore.QMetaObject.connectSlotsByName(yQGrid3DSurfaceDialog)

    def retranslateUi(self, yQGrid3DSurfaceDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("yQGrid3DSurfaceDialog", "（鼠标左键：选取查看数据点；鼠标滚轮：缩放场景；鼠标右键：旋转场景）"))

from yColorTableSpectrumWidget import yColorTableSpectrumWidget
from ycolortablepresetscombobox import yColorTablePresetsComboBox
import ChartsVisualization_rc
import Grid3DSurfaceDialog_rc
import UI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    yQGrid3DSurfaceDialog = QtWidgets.QDialog()
    ui = Ui_yQGrid3DSurfaceDialog()
    ui.setupUi(yQGrid3DSurfaceDialog)
    yQGrid3DSurfaceDialog.show()
    sys.exit(app.exec_())

