# -*- coding: utf-8 -*-
# .belongToProj项目
# .belongToModel模型
# .belongToForwardDataNode分量
"""
Module implementing ForwardCenterWidget.
"""

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QApplication, QMessageBox, QAction, QTreeWidgetItem, QMenu, QActionGroup,\
    QWidget, QToolButton
from PyQt5.QtGui import QIcon,QKeySequence

from ForwardCenter.Ui_ForwardCenterWidget import Ui_ForwardCenterWidget
# from enum import Enum,unique
from UI.GeoMagFieldSettingDialog import yQGeoMagFieldSettingDialog  # 磁场参数
from UI.SphereModelSettingDialog import SphereModelSettingDialog  # 球体参数
from UI.RectPrismModelSettingDialog import RectPrismModelSettingDialog  # 长方体参数
from UI.GridSettingDialog import GridSettingDialog  # 网格参数
from UI.ForwardProject import *  # 单个正演项目
from ForwardCenter.ForwardProjectManager import *  # 总正演项目管理
from UI.model import Model  # 模型（球体/长方体）
from UI.XZgraphDialog import XZgraphDialog  # XZ平面投影图
from UI.XYgraphDialog import XYgraphDialog  # XY平面投影图
from UI.YZgraphDialog import YZgraphDialog  # YZ平面投影图
from UI.graph3DDialog import graph3DDialog  # 三维曲面图
from UI.GridContourMapDialog import GridContourMapDialog  # 等值线图
from UI.surface3DDialog import surface3DDialog  # 三维曲面图
# from enum import Enum,unique
#



class ForwardCenterWidget(QWidget, Ui_ForwardCenterWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ForwardCenterWidget, self).__init__(parent)
        self.setupUi(self)
        self.actionSaveForwardData.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.setupPopupMenus()
        self.setupTreeWidget()#隐藏treeWidget标签

        self.actionDelete.triggered.connect(self.onDeleteTreeItem)
        self.actionDelete.setShortcut(QKeySequence.Delete)
        self.actionSaveForwardData.triggered.connect(self.onSaveForwardData)
        self.actionSaveForwardData.setVisible(False)

        self.ItemType_TreeRoot = QTreeWidgetItem.UserType
        # print(QTreeWidgetItem.UserType)#1
        self.ItemType_Unknow = -1
        self.ItemType_ForwardProjectRoot = 2
        self.ItemType_GridInfo_Root = 3  # 网格信息
        self.ItemType_GridInfo = 4
        self.ItemType_GeoMag_Root = 5  # 地磁参数
        self.ItemType_GeoMag_Info = 6
        self.ItemType_Model_Root = 7  # 理论模型
        self.ItemType_Model_Sphere = 8
        self.ItemType_Model_RectPrism = 9
        self.ItemType_ForwardGridData_Root = 10  # 正演数据
        self.ItemType_ForwardGridData = 11

        self.modelType_Sphere=0
        self.modelType_RectPrism=1

    def createNewForwardProject(self,type):
        # type 0 磁 1 重
        ins=yForwardProjectManager()
        if type==0:
            proj=ins.createProject(ForwardProject.projectType_Mag)
            txt='正演项目(磁)'
            iconName=":/ForwardCenter/magnetic"
        elif type==1:
            proj=ins.createProject(ForwardProject.projectType_Grv)
            txt='正演项目(重)'
            iconName=':/ForwardCenter/gravity'
        else:
            return

        #print(ins.m_forwardProjs.__len__())#做实验OK

        projectRoot=QTreeWidgetItem(self.treeWidget,self.ItemType_ForwardProjectRoot)
        projectRoot.setIcon(0,QIcon(iconName))
        projectRoot.setText(0,txt)
        projectRoot.belongToProj=proj#设置各个模块所属的项目

        #网格信息

        gridInfoRoot=QTreeWidgetItem(projectRoot,self.ItemType_GridInfo_Root)
        gridInfoRoot.setText(0,'网格信息')
        gridInfoRoot.setIcon(0,QIcon(":/ForwardCenter/gridInfoSetting"))
        gridInfoRoot.belongToProj = proj

        #网格参数具体信息
        setting=proj.gridSetting()#
        xTxt='x:%d~%d'%(setting.xMin,setting.xMax)#是要用%d吗？
        yTxt='y:%d~%d'%(setting.yMin,setting.yMax)
        sizeTxt='%d(行)~%d(列)'%(setting.rows,setting.cols)
        

        projectInfo_XRange=QTreeWidgetItem(gridInfoRoot,self.ItemType_GridInfo)
        projectInfo_XRange.setText(0, xTxt)
        projectInfo_XRange.setIcon(0,QIcon(":/ForwardCenter/gridXRange"))




        projectInfo_YRange = QTreeWidgetItem(gridInfoRoot,self.ItemType_GridInfo)
        projectInfo_YRange.setText(0, yTxt)
        projectInfo_YRange.setIcon(0, QIcon(":/ForwardCenter/gridYRange"))


        projectInfo_Size = QTreeWidgetItem(gridInfoRoot,self.ItemType_GridInfo)
        projectInfo_Size.setText(0, sizeTxt)
        projectInfo_Size.setIcon(0, QIcon(":/ForwardCenter/gridSize"))

        

        #地磁参数信息

        if type==0:
            geoMag = proj.geoMagInfo()  # 地磁参数信息
            geoMagRoot=QTreeWidgetItem(projectRoot,self.ItemType_GeoMag_Root)
            geoMagRoot.setText(0,'地磁参数')
            geoMagRoot.setIcon(0,QIcon(":/ForwardCenter/Resources/geoMagSetting.png"))
            geoMagRoot.belongToProj = proj#设置各个模块所属的项目


            #print(geoMag.T0)#做实验ok
            #弹出对话框设置地磁参数
            dlg=yQGeoMagFieldSettingDialog()
            #print(dlg.T0.text())#做实验ok
            dlg.set(geoMag.T0,geoMag.I0,geoMag.D0)
            dlg.exec_()
            if dlg.accept:
                geoMag.T0,geoMag.I0,geoMag.D0=dlg.get()
                #print(geoMag.T0)#做实验ok
            t0Txt='磁场强度:%d(nT)'%geoMag.T0
            i0Txt='地磁倾角:%d(度)'%geoMag.I0
            d0Txt='地磁偏角:%d(度)'%geoMag.D0

            T0 = QTreeWidgetItem(geoMagRoot,self.ItemType_GeoMag_Info)
            T0.setIcon(0,QIcon(":/ForwardCenter/bullet"))
            T0.setText(0,t0Txt)

            I0 = QTreeWidgetItem(geoMagRoot,self.ItemType_GeoMag_Info)
            I0.setIcon(0, QIcon(":/ForwardCenter/bullet2"))
            I0.setText(0, i0Txt)

            D0 = QTreeWidgetItem(geoMagRoot,self.ItemType_GeoMag_Info)
            D0.setIcon(0, QIcon(":/ForwardCenter/bullet3"))
            D0.setText(0, d0Txt)

        #理论模型
        modelsRoot=QTreeWidgetItem(projectRoot,self.ItemType_Model_Root)
        modelsRoot.setText(0,'模型')
        modelsRoot.setIcon(0,QIcon(":/ForwardCenter/model"))
        modelsRoot.belongToProj = proj#设置各个模块所属的项目

        #正演数据（磁或重）
        forwardDataRoot=QTreeWidgetItem(projectRoot,self.ItemType_ForwardGridData_Root)
        forwardDataRoot.setText(0,'正演数据')
        forwardDataRoot.setIcon(0,QIcon(":/ForwardCenter/forwardData"))
        forwardDataRoot.belongToProj = proj#设置各个模块所属的项目

        #暂时留着
        '''
        SetDataToTreeItem(proj,gridInfoRoot)
        SetDataToTreeItem(proj,modelsRoot)
        SetDataToTreeItem(proj,forwardDataRoot)

        if geoMagRoot:
            SetDataToTreeItem(proj, geoMagRoot)
        '''
        self.treeWidget.expandAll()

    def setupTreeWidget(self):
        tree=self.treeWidget
        tree.setColumnCount(1)
        tree.header().setVisible(False)

    def onCreateMagForwardProject(self):
        self.createNewForwardProject(0)

    def onCreateGrvForwardProject(self):
        self.createNewForwardProject(1)

    def setupPopupMenus(self):
        #给工具栏上的按钮添加弹出菜单
        menuAddProject=QMenu(self)
        addMagProj=menuAddProject.addAction(QIcon(":/ForwardCenter/magnetic"), "磁正演项目")
        addGrvProj=menuAddProject.addAction(QIcon(":/ForwardCenter/gravity"), "重力正演项目")

        self.actionNewProject.setMenu(menuAddProject)#添加项目
        tb=self.toolBar.widgetForAction(self.actionNewProject)
        tb.setPopupMode(QToolButton.InstantPopup)#立即弹出

        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.showMyMenu)

        addMagProj.triggered.connect(self.onCreateMagForwardProject)#
        addGrvProj.triggered.connect(self.onCreateGrvForwardProject)#

        self.m_GridSettingMenu=QMenu(self)
        # self.action=QAction(QIcon(":/ForwardCenter/cog"),'设置')
        action=QAction(QIcon(":/ForwardCenter/cog"),'设置',self)
        self.m_GridSettingMenu.addAction(action)
        action.triggered.connect(self.onGridSetting)

        self.m_GeoMagSettingMenu = QMenu(self)
        action = QAction(QIcon(":/ForwardCenter/cog"), '设置',self)

        self.m_GeoMagSettingMenu.addAction(action)
        action.triggered.connect(self.onGeoMagSetting)

        #创建模型菜单
        self.m_ModelMenu=QMenu(self)
        self.subMenu=self.m_ModelMenu.addMenu(QIcon(":/ForwardCenter/addModel"),'添加模型')
        subAction1 = QAction(QIcon(':/ForwardCenter/sphere'),'球体',self)
        subAction2 = QAction(QIcon(':/ForwardCenter/cube'), '长方体',self)
        subAction1.triggered.connect(self.onAddModel_Sphere)  #
        subAction2.triggered.connect(self.onAddModel_RectPrism)  #
        self.subMenu.addActions([subAction1,subAction2])

        importModelAction=QAction(QIcon(":ForwardCenter/import"),'导入模型',self)
        self.m_ModelMenu.addAction(importModelAction)
        importModelAction.triggered.connect(self.onImportModel)

        saveModelAction=QAction(QIcon(":ForwardCenter/export"),'保存模型',self)
        self.m_ModelMenu.addAction(saveModelAction)
        saveModelAction.triggered.connect(self.onSaveModel)

        visializeMenu=self.m_ModelMenu.addMenu(QIcon(":ForwardCenter/visualization"),'模型可视化')########改
        subAction1 = QAction(QIcon(":ForwardCenter/bullet"),'XZ平面投影图',self)######加图标
        subAction2 = QAction(QIcon(":ForwardCenter/bullet1"),'XY平面投影图',self)######加图标
        subAction3=QAction(QIcon(":ForwardCenter/bullet2"),'YZ平面投影图',self)######加图标
        subAction4 = QAction(QIcon(":ForwardCenter/bullet3"),'模型三维图',self)######加图标
        subAction1.triggered.connect(self.onXZgraph)
        subAction2.triggered.connect(self.onXYgraph)
        subAction3.triggered.connect(self.onYZgraph)
        subAction4.triggered.connect(self.on3Dgraph)
        visializeMenu.addActions([subAction1,subAction2,subAction3,subAction4])

        forwardgridDataGroup = QActionGroup(self)
        forwardgridDataGroup.triggered.connect(self.onAddForwardGridData)

        #磁力正演菜单
        icon=QIcon(":/ForwardCenter/bullet")

        self.m_ForwardMenu_Mag=QMenu(self)
        subMenu=self.m_ForwardMenu_Mag.addMenu(QIcon(":/ForwardCenter/magnetic"),'添加磁正演量')
        subAction1 = QAction(icon,'△T',self)
        subAction2 = QAction(icon, 'Hax',self)
        subAction3 = QAction(icon, 'Hay',self)
        subAction4 = QAction(icon, 'Za',self)

        subMenu.addActions([subAction1,subAction2,subAction3,subAction4])
        subAction1.setData(DataComponentType().DT)
        subAction2.setData(DataComponentType().Hax)
        subAction3.setData(DataComponentType().Hay)
        subAction4.setData(DataComponentType().Za)
        # print(subAction1.data())
        #subAction1.setData(int(eDataComponentType.DT))
        #subAction2.setData(int(eDataComponentType.Hax))
        #subAction3.setData(int(eDataComponentType.Hay))
        #subAction4.setData(int(eDataComponentType.Za))

        forwardgridDataGroup.addAction(subAction1)
        forwardgridDataGroup.addAction(subAction2)
        forwardgridDataGroup.addAction(subAction3)
        forwardgridDataGroup.addAction(subAction4)

        #重力正演菜单
        self.m_ForwardMenu_Grv=QMenu(self)
        subMenu = self.m_ForwardMenu_Grv.addMenu(QIcon(":/ForwardCenter/magnetic"), '添加重力正演量')
        subAction1 = QAction(icon, '△g',self)
        #subAction2 = QAction(icon, 'Gxz',self)
        #subAction3 = QAction(icon, 'Gyz',self)
        #subAction4 = QAction(icon, 'Gzz',self)

        subMenu.addAction(subAction1)
                           #subAction2, subAction3, subAction4)
        subAction1.setData(DataComponentType().Dg)
        #subAction1.setData(int(eDataComponentType.Dg))
        #subAction2.setData(int(eDataComponentType.Gxz))
        #subAction3.setData(int(eDataComponentType.Gyz))
        #subAction4.setData(int(eDataComponentType.Gzz))
        forwardgridDataGroup.addAction(subAction1)
        #, subAction2, subAction3, subAction4)

        #显示正演数据
        self.m_DisplayForwardDataMenu=QMenu(self)
        action1=QAction(QIcon(":/ForwardCenter/bullet2"),'等值线图',self)
        action2=QAction(QIcon(":/ForwardCenter/bullet3"),'三维曲面图',self)
        self.m_DisplayForwardDataMenu.addActions([action1,action2])
        action1.triggered.connect(self.onDisplayForwardGridData_Contour)#
        action2.triggered.connect(self.onDisplayForwardGridData_3DSurface)#


    def contextMenuEvent(self, event):#右键弹出菜单
        tree=self.treeWidget
        selectedItem=tree.currentItem()
        if not selectedItem:
            return
        event.accept()
        pos=event.pos()
        #判断是否在TreeWidget内
        rect_Tree=tree.geometry()
        if rect_Tree.contains(pos)==False:
            return
        pt=event.globalPos()#???
        type=selectedItem.type()
        if type==self.ItemType_GridInfo_Root:#网格信息
            self.m_GridSettingMenu.popup(pt)
            return
        elif type==self.ItemType_GeoMag_Root:#地磁参数
            self.m_GeoMagSettingMenu.popup(pt)
            return
        elif type==self.ItemType_Model_Root:#模型
            self.m_ModelMenu.popup(pt)
            return
        elif type==self.ItemType_ForwardGridData_Root:#正演数据
            item=self.treeWidget.currentItem()
            p=item.parent()
            #print(p.data(0,Qt.UserRole))#none
            if p.text(0)=='正演项目(重)':
                self.m_ForwardMenu_Grv.popup(pt)
            else:
                self.m_ForwardMenu_Mag.popup(pt)
            return
        elif type==self.ItemType_ForwardGridData:#正演数据
            self.m_DisplayForwardDataMenu.popup(pt)
            return

    def setEnableOfActionOnDataTreeItem(self,enable):
        #self.actionSave.setEnable(True)
        #self.actionDelete.setEnable(True)
        pass

    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_treeWidget_currentItemChanged(self, current, previous):
        """
        Slot documentation goes here.

        @param current DESCRIPTION
        @type QTreeWidgetItem
        @param previous DESCRIPTION
        @type QTreeWidgetItem
        """
        if not current:
            return
        type=current.type()

        isProj=self.ItemType_ForwardProjectRoot==type
        # isGridInfoRoot=self.ItemType_GridInfo_Root==type
        # isGeoMagRoot=self.ItemType_GeoMag_Root==type

        isModel=self.ItemType_Model_Sphere==type or self.ItemType_Model_RectPrism==type
        isForwardGridData=self.ItemType_ForwardGridData==type

        self.actionSaveForwardData.setEnabled(isForwardGridData)
        self.actionSaveForwardData.setVisible(isForwardGridData)
        self.actionDelete.setEnabled(isModel or isForwardGridData or isProj)

        #获取数据中的基本信息，显示在面板下面的label文字栏上
        if isModel:
            parentItem=current.parent()
            if not parentItem:
                return
            proj=parentItem.belongToProj
            model=current.belongToModel
            if model.modelType==model.modelType_Sphere:
                x=model.m_geometry_center_x
                y=model.m_geometry_center_y
                z=model.m_geometry_center_z
                r=model.m_geometry_radius
                infoStr='球体中心（%d,%d,%d）半径:%d'%(x,y,z,r)
            elif model.modelType==model.modelType_RectPrism:
                x = model.m_geometry_center_x
                y = model.m_geometry_center_y
                z = model.m_geometry_center_z
                L=model.m_geometry_xLen
                W=model.m_geometry_yLen
                H=model.m_geometry_zLen
                infoStr='中心(%d,%d,%d),大小(%d×%d×%d)'%(x,y,z,L,W,H)

            if proj.type()==ForwardProject.projectType_Mag:
                infoStr+='\n磁化率:%f(SI)'%model.K
            elif proj.type()==ForwardProject.projectType_Grv:
                infoStr+='\n密度:%f(g/cm^3)'%model.density
            self.labelInfo.setText(infoStr)
        elif isForwardGridData:
            parentItem=current.parent()
            if not parentItem:
                return
            proj=parentItem.belongToProj
            if not proj:
                return
            #还没写————————————————————————————————
            forwardData=current.belongToForwardDataNode.forwardData
            min=np.min(forwardData)
            max=np.max(forwardData)

            infoStr='%f~%f'%(min,max)
            self.labelInfo.setText(infoStr)
        else:
            self.labelInfo.setText(u'')

    def onDeleteTreeItem(self):
        currentItem=self.treeWidget.currentItem()
        if not currentItem:
            return
        type=currentItem.type()
        if self.ItemType_ForwardGridData==type:
            #正演数据
            # 1、从树上删除节点
            parentItem = currentItem.parent()
            if not parentItem:
                return
            parentItem.removeChild(currentItem)
            # 2、同时删除相关的数据显示对话框(如果存在的话)
            # 3、底层的数据结构中也要删除
            proj=parentItem.belongToProj
            compType=currentItem.belongToForwardDataNode.m_componentType
            proj.deleteForwardDataNode(compType)

        elif type == self.ItemType_Model_Sphere or type == self.ItemType_Model_RectPrism:
            # 模型
            # 1、从树上删除
            parentItem = currentItem.parent()
            proj = parentItem.belongToProj
            model = currentItem.belongToModel
            if not parentItem:
                return
            parentItem.removeChild(currentItem)
                    #若模型数删去后只有0个，则删去所有正演数据
            if parentItem.childCount()==0:
                projItem=parentItem.parent()
                if proj.m_projectType==ForwardProject.projectType_Mag:#磁
                    item=projItem.child(3)#正演数据
                    if item.childCount():
                        for i in range(0,item.childCount()):
                            self.treeWidget.setCurrentItem(item.child(i))
                            self.onDeleteTreeItem()  # 迭代本函数

                if proj.m_projectType==ForwardProject.projectType_Grv:#重
                    item=projItem.child(2)#正演数据
                    if item.childCount():
                        for i in range(0,item.childCount()):
                            self.treeWidget.setCurrentItem(item.child(i))
                            self.onDeleteTreeItem()#迭代本函数
            self.treeWidget.setCurrentItem(parentItem)
            # 将正演数据减去该模型的正演值，从底层数据结构中删除
            proj.deleteModel(model)
        elif type==self.ItemType_ForwardProjectRoot:#删除项目
            proj = currentItem.belongToProj
            index=self.treeWidget.indexOfTopLevelItem(currentItem)
            self.treeWidget.takeTopLevelItem(index)
            ins=yForwardProjectManager()
            ins.deleteProject(proj)

    @pyqtSlot(QTreeWidgetItem, int)
    def on_treeWidget_itemDoubleClicked(self, item, column):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QTreeWidgetItem
        @param column DESCRIPTION
        @type int
        """
        itemType = item.type()
        if itemType == self.ItemType_Model_Sphere:
            self.onSphereModelSetting()
        elif itemType == self.ItemType_Model_RectPrism:
            self.onRectPrismModelSetting()

    def onGridSetting(self):#网格参数设置
        item=self.treeWidget.currentItem()
        #print(not item)#做实验OK
        if not item:
            return
        proj=item.belongToProj
        if not proj:
            return
        info=proj.gridSetting()
        xyRanges = [info.xMin, info.xMax, info.yMin, info.yMax]
        size = [info.rows, info.cols]
        dlg=GridSettingDialog()
        dlg.set(xyRanges, size)
        dlg.exec_()
        #print(dlg.accept)#做实验OK
        if dlg.accept:
            xyRanges,size=dlg.get()#????
            #print(xyRanges,size)#做实验OK
            isChanged=xyRanges[0] != info.xMin or xyRanges[1] != info.xMax or xyRanges[2] != info.yMin or xyRanges[3] != info.yMax or size[0] != info.rows or  size[1] != info.cols
            if isChanged:
                proj.setGridSetting(xyRanges,size)#????
                info = proj.gridSetting()
                #重新设置tree上的文字
                xTxt = 'x:%d~%d'%(info.xMin,info.xMax)
                yTxt = 'y:%d~%d'%(info.yMin,info.yMax)
                sizeTxt = '%d(行)x%d(列)'%(info.rows,info.cols)

                item.child(0).setText(0,xTxt)
                item.child(1).setText(0,yTxt)
                item.child(2).setText(0,sizeTxt)
                # 重新正演计算
                if proj.m_forwardDataNodes.__len__():
                    for node in proj.m_forwardDataNodes:
                        proj.calculateForwardData(node)
            item.setExpanded(True)


    def onGeoMagSetting(self):

        item=self.treeWidget.currentItem()
        if not item:
            return
        proj=item.belongToProj
        if not proj:
            return
        geoMag=proj.geoMagInfo()
        T0 = geoMag.T0
        I0 = geoMag.I0
        D0 = geoMag.D0
        #print(T0,I0,D0)#做实验OK

        dlg=yQGeoMagFieldSettingDialog()
        dlg.set(T0,I0,D0)
        dlg.exec_()
        if dlg.accept:
            T0,I0,D0=dlg.get()
            isChanged= T0!= geoMag.T0 or I0!= geoMag.I0 or D0!=geoMag.D0
            #print(isChanged)#OK
            if isChanged:
                pass
                proj.setGeoMagInfo(T0,I0,D0)#????
                #重新设置tree上的文字
                t0Txt = '磁场强度: %d(nT)' % geoMag.T0
                i0Txt = '地磁倾角: %d(度)' % geoMag.I0
                d0Txt = '地磁偏角: %d(度)' % geoMag.D0
                item.child(0).setText(0,t0Txt)
                item.child(1).setText(0,i0Txt)
                item.child(2).setText(0,d0Txt)
                # 重新正演计算
                if proj.m_forwardDataNodes.__len__():
                    for node in proj.m_forwardDataNodes:
                        proj.calculateForwardData(node)
            item.setExpanded(True)
            #重新正演计算
            return True
        else:
            return False

    def onAddModel_Sphere(self):
        item=self.treeWidget.currentItem()
        if not item:
            return
        proj=item.belongToProj
        if not proj:
            return

        model=Model(self.modelType_Sphere)
        #print(model.m_geometry_center_x)#OK

        #设置item
        newItem=QTreeWidgetItem(item,self.ItemType_Model_Sphere)#type
        newItem.setText(0,'球体')
        newItem.setIcon(0,QIcon(":/ForwardCenter/sphere"))

        #设置item所属项目和模型
        newItem.belongToProj = proj
        newItem.belongToModel=model

        # print(proj.m_models.__len__())#ok

        self.treeWidget.setCurrentItem(newItem)
        add=self.onSphereModelSetting()#弹出球体模型设置dialog
        if not add:
            currentItem = self.treeWidget.currentItem()
            parentItem = currentItem.parent()
            parentItem.removeChild(currentItem)
        else:
            proj.addModel(model)#底层模型数据添加

    def onAddModel_RectPrism(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        proj = item.belongToProj
        if not proj:
            return
        model = Model(self.modelType_RectPrism)
        # print(model.m_geometry_center_x)#OK
        newItem = QTreeWidgetItem(item, self.ItemType_Model_RectPrism)#type
        newItem.setText(0, '长方体')
        newItem.setIcon(0, QIcon(":/ForwardCenter/cube"))

        newItem.belongToProj = proj
        newItem.belongToModel = model

        # print(proj.m_models.__len__())#OK

        self.treeWidget.setCurrentItem(newItem)
        add=self.onRectPrismModelSetting()#弹出长方体模型设置dialog
        if not add:
            currentItem = self.treeWidget.currentItem()
            parentItem = currentItem.parent()
            parentItem.removeChild(currentItem)
        else:
            proj.addModel(model)

    def onSphereModelSetting(self):
        item=self.treeWidget.currentItem()
        if not item:
            return
        parentItem=item.parent()
        if not parentItem:
            return

        proj=parentItem.belongToProj
        s=item.belongToModel

        isMag=proj.type()==ForwardProject.projectType_Mag
        center=[s.m_geometry_center_x,s.m_geometry_center_y,s.m_geometry_center_z]
        if isMag:
            property=s.K
        else:
            property=s.density
        #print(property)
        dlg=SphereModelSettingDialog(isMag)
        dlg.set(center,s.m_geometry_radius,property)
        dlg.exec_()
        if dlg.accept:
            center,newRadius,newProperty=dlg.get()
            isChanged=s.m_geometry_center_x!=center[0] or s.m_geometry_center_y!=center[1] \
                    or s.m_geometry_center_z!=center[2] or property!=newProperty or s.m_geometry_radius!=newRadius
            #print(isChanged)
            if isChanged:
                proj.updateSphereModelParmeter(s,center,newRadius,newProperty)
                #重新正演计算
                if proj.m_forwardDataNodes.__len__():
                    for node in proj.m_forwardDataNodes:
                        proj.calculateForwardData(node)
                self.on_treeWidget_currentItemChanged(item,None)
            return True
        else:
            return False

    def onRectPrismModelSetting(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return

        proj = parentItem.belongToProj
        s = item.belongToModel

        isMag = proj.type() == ForwardProject.projectType_Mag
        center = [s.m_geometry_center_x, s.m_geometry_center_y, s.m_geometry_center_z]
        size=[s.m_geometry_xLen,s.m_geometry_yLen,s.m_geometry_zLen]
        if isMag:
            property = s.K
        else:
            property = s.density
        dlg = RectPrismModelSettingDialog(isMag)
        dlg.set(center, size, property)
        dlg.exec_()
        if dlg.accept:
            center, size, newProperty = dlg.get()
            isChanged = s.m_geometry_center_x != center[0] or s.m_geometry_center_y != center[1] \
                        or s.m_geometry_center_z != center[2]\
                        or s.m_geometry_xLen!=size[0] or s.m_geometry_yLen!=size[1] or s.m_geometry_zLen!=size[2] or \
                        property != newProperty
            # print(isChanged)#OK
            if isChanged:
                proj.updateRectPrismModelParmeter(s, center, size, newProperty)
                # 重新正演计算
                if proj.m_forwardDataNodes.__len__():
                    for node in proj.m_forwardDataNodes:
                        proj.calculateForwardData(node)
                self.on_treeWidget_currentItemChanged(item, None)
            return True
        else:
            return False

    def onImportModel(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        filename=QFileDialog.getOpenFileName(self,'导入模型','',"Model Files(*.txt);;All Files(*.*)",
                                               'Model Files(*.txt)')
        if filename[0]!='':
            with open(filename[0],'r') as f:
                if int(f.readline())==proj.m_projectType:
                    modelCount=int(f.readline())
                    for i in np.arange(modelCount):
                        modelType=int(f.readline())
                        if modelType==self.modelType_Sphere:#球体
                            model = Model(self.modelType_Sphere)

                            # 设置item
                            newItem = QTreeWidgetItem(item, self.ItemType_Model_Sphere)  # type
                            newItem.setText(0, '球体')
                            newItem.setIcon(0, QIcon(":/ForwardCenter/sphere"))

                            # 设置item所属项目和模型
                            newItem.belongToProj = proj
                            newItem.belongToModel = model

                            model.m_geometry_center_x = int(f.readline())
                            model.m_geometry_center_y = int(f.readline())
                            model.m_geometry_center_z = int(f.readline())
                            model.m_geometry_radius = int(f.readline())
                            if proj.m_projectType == 1:  # 重力模型
                                model.density = float(f.readline())
                            elif proj.m_projectType == 0:#磁法模型
                                model.K=float(f.readline())

                            proj.addModel(model)  # 底层模型数据添加
                        elif modelType==self.modelType_RectPrism:#长方体
                            model = Model(self.modelType_RectPrism)

                            newItem = QTreeWidgetItem(item, self.ItemType_Model_RectPrism)  # type
                            newItem.setText(0, '长方体')
                            newItem.setIcon(0, QIcon(":/ForwardCenter/cube"))

                            newItem.belongToProj = proj
                            newItem.belongToModel = model

                            model.m_geometry_center_x = int(f.readline())
                            model.m_geometry_center_y = int(f.readline())
                            model.m_geometry_center_z = int(f.readline())
                            model.m_geometry_xLen = int(f.readline())
                            model.m_geometry_yLen = int(f.readline())
                            model.m_geometry_zLen = int(f.readline())
                            if proj.m_projectType == 1:  # 重力模型
                                model.density = float(f.readline())
                            elif proj.m_projectType == 0:  # 磁法模型
                                model.K = float(f.readline())
                            proj.addModel(model)
                else:
                    QMessageBox.information(self,'提示','该文件不符合对应的正演项目！')
                    return

    def onSaveModel(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        if item.childCount()==0:
            QMessageBox.information(self, '提示', '请至少添加一个模型！')
            return
        filename = QFileDialog.getSaveFileName(self, '导出模型', '',"Model Files(*.txt);;All Files(*.*)",
                                               'Model Files(*.txt)')
        if filename[0] != '':  # 若取消则filename[0]=''
            with open(filename[0], 'w') as f:
                f.write('%d\n'%proj.m_projectType)#项目类别
                f.write('%d\n' % item.childCount())#模型个数
                for i in np.arange(0, item.childCount()):
                    childItem=item.child(i)
                    model=childItem.belongToModel
                    if model.modelType==self.modelType_Sphere:
                        x=model.m_geometry_center_x
                        y=model.m_geometry_center_y
                        z=model.m_geometry_center_z
                        r=model.m_geometry_radius
                        if proj.m_projectType==1:#重力模型
                            property=model.density
                        elif proj.m_projectType==0:
                            property=model.K
                        f.write('%d\n%d\n%d\n%d\n%d\n%f\n'%(model.modelType,x,y,z,r,property))
                    elif model.modelType==self.modelType_RectPrism:
                        x=model.m_geometry_center_x
                        y=model.m_geometry_center_y
                        z=model.m_geometry_center_z
                        xLen=model.m_geometry_xLen
                        yLen = model.m_geometry_yLen
                        zLen = model.m_geometry_zLen
                        if proj.m_projectType==1:#重力模型
                            property=model.density
                        elif proj.m_projectType==0:
                            property=model.K
                        f.write('%d\n%d\n%d\n%d\n%d\n%d\n%d\n%f\n'%(model.modelType,x,y,z,xLen,yLen,zLen,property))

    def onXZgraph(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        if proj.m_models.__len__()==0:
            QMessageBox.information(self, '提示', '请至少添加一个模型！')
            return
        if proj.modelGraphs.__len__():
            for dlg in proj.modelGraphs:
                if dlg.type==None:#当dlg关闭时dlg.type=None
                    proj.modelGraphs.remove(dlg)
                if dlg.type==displayUI().modelXZgraph:
                    # QMessageBox.information(self, '提示', '模型XZ平面投影图已存在！')
                    return
        # 若还未存在，则创建
        dlg = XZgraphDialog()
        # info = proj.gridSetting()
        dlg.XZgraphWgt.mpl.start_modelXZGraph(proj.m_models)
        dlg.setWindowTitle('模型XZ平面投影图')
        dlg.setAttribute(Qt.WA_DeleteOnClose, True)  # Makes Qt delete this widget when
        # the widget has accepted the close event (see QWidget::closeEvent()).
        dlg.show()  # 非模态对话框
        # dlg.exec_()

        proj.modelGraphs.append(dlg)
        
    def onXYgraph(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        if proj.m_models.__len__() == 0:
            QMessageBox.information(self, '提示', '请至少添加一个模型！')
            return
        if proj.modelGraphs.__len__():
            for dlg in proj.modelGraphs:
                if dlg.type == None:  # 当dlg关闭时dlg.type=None
                    proj.modelGraphs.remove(dlg)
                if dlg.type == displayUI().modelXYgraph:
                    # QMessageBox.information(self, '提示', '模型XY平面投影图已存在！')
                    return
        # 若还未存在，则创建
        dlg = XYgraphDialog()
        # info = proj.gridSetting()
        dlg.XYgraphWgt.mpl.start_modelXYGraph(proj.m_models)
        dlg.setWindowTitle('模型XY平面投影图')
        dlg.setAttribute(Qt.WA_DeleteOnClose, True)  # Makes Qt delete this widget when
        # the widget has accepted the close event (see QWidget::closeEvent()).
        dlg.show()  # 非模态对话框
        # dlg.exec_()
        proj.modelGraphs.append(dlg)

    def onYZgraph(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        if proj.m_models.__len__() == 0:
            QMessageBox.information(self, '提示', '请至少添加一个模型！')
            return
        if proj.modelGraphs.__len__():
            for dlg in proj.modelGraphs:
                if dlg.type == None:  # 当dlg关闭时dlg.type=None
                    proj.modelGraphs.remove(dlg)
                if dlg.type == displayUI().modelYZgraph:
                    # QMessageBox.information(self, '提示', '模型YZ平面投影图已存在！')
                    return
        # 若还未存在，则创建
        dlg = YZgraphDialog()
        # info = proj.gridSetting()
        dlg.YZgraphWgt.mpl.start_modelYZGraph(proj.m_models)
        dlg.setWindowTitle('模型YZ平面投影图')
        dlg.setAttribute(Qt.WA_DeleteOnClose, True)  # Makes Qt delete this widget when
        # the widget has accepted the close event (see QWidget::closeEvent()).
        dlg.show()  # 非模态对话框
        # dlg.exec_()
        proj.modelGraphs.append(dlg)

    def on3Dgraph(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        if proj.m_models.__len__() == 0:
            QMessageBox.information(self, '提示', '请至少添加一个模型！')
            return
        if proj.modelGraphs.__len__():
            for dlg in proj.modelGraphs:
                if dlg.type == None:  # 当dlg关闭时dlg.type=None
                    proj.modelGraphs.remove(dlg)
                if dlg.type == displayUI().model3Dgraph:
                    # QMessageBox.information(self, '提示', '模型三维图已存在！')
                    return
        # 若还未存在，则创建
        dlg = graph3DDialog()
        # info = proj.gridSetting()
        dlg.graph3DWgt.mpl.start_model3DGraph(proj.m_models)
        dlg.setWindowTitle('模型三维图')
        dlg.setAttribute(Qt.WA_DeleteOnClose, True)  # Makes Qt delete this widget when
        # the widget has accepted the close event (see QWidget::closeEvent()).
        dlg.show()  # 非模态对话框
        # dlg.exec_()
        proj.modelGraphs.append(dlg)

    def onAddForwardGridData(self,action):
        if not action:
            return
        item=self.treeWidget.currentItem()
        if not item:
            return
        proj=item.belongToProj
        if not proj:
            return
        if proj.m_models.__len__()==0:
            QMessageBox.information(self, '提示', '请先添加模型！')
            return
        compType=action.data()
        newNode=proj.addForwardData(compType)
        if newNode==None:
            name=DataComponentType().nameOfComponentType(compType)
            # QMessageBox.information(self,'提示',name + '分量已经存在，无需再添加！')
            return
        self.addForwardDataIntoTree(item,proj,compType,newNode)

    def addForwardDataIntoTree(self,item,proj,compType,newNode):
        if compType==DataComponentType().DT:
            name='△T(nT)'
        elif compType==DataComponentType().Hax:
            name='Hax(nT)'
        elif compType==DataComponentType().Hay:
            name='Hay(nT)'
        elif compType==DataComponentType().Za:
            name='Za(nT)'
        elif compType==DataComponentType().Dg:
            name='△g(g.u)'

        #设置item
        newItem=QTreeWidgetItem(item,self.ItemType_ForwardGridData)
        newItem.setText(0,name)
        newItem.setIcon(0,QIcon(":/ForwardCenter/bullet"))

        # 设置item所属项目
        newItem.belongToProj=proj
        newItem.belongToForwardDataNode=newNode

        self.treeWidget.setCurrentItem(newItem)


    def onDisplayForwardGridData_Contour(self):
        item=self.treeWidget.currentItem()
        if not item:
            return
        parentItem=item.parent()
        if not parentItem:
            return
        proj=parentItem.belongToProj
        if not proj:
            return
        #compType=item.belongToForwardDataNode.m_componentType
        #print(compType)#做实验OK
        node=item.belongToForwardDataNode
        if not node:
            return
        if node.displayUI.__len__():
            for dlg in node.displayUI:
                if dlg.type==None:#当dlg关闭时dlg.type=None
                    node.displayUI.remove(dlg)
                if dlg.type==displayUI().contourMap:
                    # QMessageBox.information(self, '提示', item.text(0)+'分量等值线图已存在！')
                    return
        #若还未存在，则创建
        forwardData=node.forwardData
        info=proj.gridSetting()
        dlg=GridContourMapDialog()
        dlg.contourMapWgt.mpl.start_contourMap(info,forwardData)
        dlg.setWindowTitle(item.text(0)+'分量平面等值线图')
        dlg.setAttribute(Qt.WA_DeleteOnClose, True)#Makes Qt delete this widget when
        # the widget has accepted the close event (see QWidget::closeEvent()).
        dlg.show()#非模态对话框
        # dlg.exec_()
        node.displayUI.append(dlg)


    def onDisplayForwardGridData_3DSurface(self):
        item = self.treeWidget.currentItem()
        if not item:
            return
        parentItem = item.parent()
        if not parentItem:
            return
        proj = parentItem.belongToProj
        if not proj:
            return
        #compType=item.belongToForwardDataNode.m_componentType
        # print(compType)#做实验OK
        node = item.belongToForwardDataNode
        if not node:
            return
        # hasDisplayUI=proj.hasDisplayUI(node,displayUI().contourMap)
        # print(hasDisplayUI)
        if node.displayUI.__len__():
            for dlg in node.displayUI:
                if dlg.type == None:#当dlg关闭时dlg.type=None
                    node.displayUI.remove(dlg)
                if dlg.type==displayUI().surface3D:
                    # QMessageBox.information(self, '提示', item.text(0)+'分量三维曲面图已存在！')
                    return
        # 若还未存在，则创建
        forwardData = node.forwardData
        info = proj.gridSetting()
        dlg = surface3DDialog()
        dlg.surface3DWgt.mpl.start_surface3D(info,item.text(0), forwardData)
        # dlg.surface3DWgt.mpl.start_surface3D(info, item.text(0), forwardData)
        dlg.setWindowTitle(item.text(0) + '分量三维曲面图')
        dlg.setAttribute(Qt.WA_DeleteOnClose, True)  # Makes Qt delete this widget when
        # the widget has accepted the close event (see QWidget::closeEvent()).
        dlg.show()  # 非模态对话框
        # dlg.exec_()
        node.displayUI.append(dlg)

    def onSaveForwardData(self):
        item=self.treeWidget.currentItem()
        if not item:
            return
        parentItem=item.parent()
        if not parentItem:
            return
        proj=parentItem.belongToProj
        if not proj:
            return
        filename=QFileDialog.getSaveFileName(self,'保存正演数据','%s'%item.text(0),"Grid Files(*.grd);;All Files(*.*)",'Grid Files(*.grd)')
        if filename[0]!='':#若取消则filename[0]=''
            with open(filename[0],'w') as f:
                # f=open(filename[0],'w')
                # fp = fopen(file_name, 'wt+');
                f.write('DSAA\n')
                nx=proj.m_gridSetting.cols
                ny=proj.m_gridSetting.rows
                f.write('%d %d\n'%(nx,ny))
                xmin=proj.m_gridSetting.xMin
                xmax=proj.m_gridSetting.xMax
                f.write('%d %d\n'%(xmin,xmax))
                ymin = proj.m_gridSetting.yMin
                ymax = proj.m_gridSetting.yMax
                f.write('%d %d\n'%(ymin,ymax))
                # fprintf(fp, '%s\n', 'DSAA');
                # fprintf(fp, '%d %d\n', nx, ny);
                # fprintf(fp, '%d %d\n', xmin, xmax);
                # fprintf(fp, '%d %d\n', ymin, ymax);
                data=item.belongToForwardDataNode.forwardData
                f.write('%g %g\n'%(np.min(np.min(data)),np.max(np.max(data))))
                # fprintf(fp, '%g %g\n', min(min(data)), max(max(data)));
                for i in np.arange(0,ny):
                    for j in np.arange(0,nx):
                        f.write('%g '%data[i][j])
                # for i=1:ny
                    # for j=1:nx
                        # fprintf(fp, '%g ', data(i, j));
                f.write('\n')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ForwardCenterWidget()
    ui.show()
    sys.exit(app.exec_())
    

