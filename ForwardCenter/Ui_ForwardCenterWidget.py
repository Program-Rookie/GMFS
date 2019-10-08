# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyCharm\project\ForwardCenter\ForwardCenterWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ForwardCenterWidget(object):
    def setupUi(self, ForwardCenterWidget):
        ForwardCenterWidget.setObjectName("ForwardCenterWidget")
        ForwardCenterWidget.resize(300, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(ForwardCenterWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBar = QtWidgets.QToolBar(ForwardCenterWidget)
        self.toolBar.setObjectName("toolBar")
        self.verticalLayout.addWidget(self.toolBar)
        self.treeWidget = QtWidgets.QTreeWidget(ForwardCenterWidget)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ForwardCenterWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ForwardCenter/info"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.labelInfo = QtWidgets.QLabel(ForwardCenterWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelInfo.sizePolicy().hasHeightForWidth())
        self.labelInfo.setSizePolicy(sizePolicy)
        self.labelInfo.setText("")
        self.labelInfo.setObjectName("labelInfo")
        self.horizontalLayout.addWidget(self.labelInfo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.actionNewProject = QtWidgets.QAction(ForwardCenterWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ForwardCenter/add"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewProject.setIcon(icon)
        self.actionNewProject.setObjectName("actionNewProject")
        self.actionDelete = QtWidgets.QAction(ForwardCenterWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ForwardCenter/delete"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSaveForwardData = QtWidgets.QAction(ForwardCenterWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ForwardCenter/Resources/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveForwardData.setIcon(icon2)
        self.actionSaveForwardData.setObjectName("actionSaveForwardData")
        self.toolBar.addAction(self.actionNewProject)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionSaveForwardData)

        self.retranslateUi(ForwardCenterWidget)
        QtCore.QMetaObject.connectSlotsByName(ForwardCenterWidget)

    def retranslateUi(self, ForwardCenterWidget):
        _translate = QtCore.QCoreApplication.translate
        ForwardCenterWidget.setWindowTitle(_translate("ForwardCenterWidget", "正演操作中心"))
        self.actionNewProject.setText(_translate("ForwardCenterWidget", "新建正演工程"))
        self.actionNewProject.setToolTip(_translate("ForwardCenterWidget", "新建正演工程"))
        self.actionDelete.setText(_translate("ForwardCenterWidget", "删除"))
        self.actionDelete.setToolTip(_translate("ForwardCenterWidget", "删除（快捷键delete）"))
        self.actionDelete.setShortcut(_translate("ForwardCenterWidget", "Del"))
        self.actionSaveForwardData.setText(_translate("ForwardCenterWidget", "保存"))
        self.actionSaveForwardData.setToolTip(_translate("ForwardCenterWidget", "保存正演数据"))

import ForwardCenter.ForwardCenter_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForwardCenterWidget = QtWidgets.QWidget()
    ui = Ui_ForwardCenterWidget()
    ui.setupUi(ForwardCenterWidget)
    ForwardCenterWidget.show()
    sys.exit(app.exec_())

