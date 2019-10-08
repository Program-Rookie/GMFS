# -*- coding: utf-8 -*-
#导入需要的库


from PyQt5.QtWidgets import QWidget,QVBoxLayout,QApplication,QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolBar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

# colorList=list()
# MaxColorSize=0
# for c in colors.cnames:
#     colorList.append(c)
#     MaxColorSize+=1
# print(MaxColorSize)
#封装绘图类
class MatplotlibWidget(QWidget):
    def __init__(self,parent=None):
        super(MatplotlibWidget,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout=QVBoxLayout(self)
        self.mpl=MyMplCanvas(self)#,width=5,height=4,dpi=100)
        # self.mpl.start_static_plot()#如果想在初始化时就显示静态图，请取消这行注释
        # self.mpl.start_dynamic_plot()#如果想在初始化时就显示静态图，请取消这行注释
        self.mpl_ntb=NavigationToolBar(self.mpl,self)#添加完整的工具栏

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
        
class MyMplCanvas(FigureCanvas):
    '''FigureCanvas的最终父类其实是Qwidget'''
    def __init__(self,parent=None):#,width=5,height=4,dpi=100):
        #设置中文显示
        plt.rcParams['font.family']=['SimHei']#用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
        self.cb=None
        #新建一个绘图对象
        self.fig=Figure()#figsize=(width,height),dpi=dpi)
        #建立一个子图。如果要建立复合图，在这里修改
        self.axes=self.fig.add_subplot(111)

        # self.axes.hold(False)#每次绘图时都不保留上次的绘图结果

        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)
        '''定义FigureCanvas的尺寸策略，意思是设置FigureCanvas，使之尽可能向外填充空间'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    # '''绘制静态图，可以在这里定义或编辑 matplotlib.org/gallery'''
    # def start_static_plot(self):
    #     self.fig.suptitle('测试静态图')
    #     t=np.arange(0.0,3.0,0.01)
    #     s=np.sin(2*np.pi*t)
    #     self.axes.plot(t,s)
    #     self.axes.set_ylabel('静态图：Y轴')
    #     self.axes.set_xlabel('静态图：X轴')
    #     self.axes.grid(True)
    #
    # '''启动绘制动态图'''
    # def start_dynamic_plot(self,*args,**kwargs):
    #     timer=QtCore.QTimer(self)
    #     timer.timeout.connect(self.update_figure)#每隔一段时间就会触发一次update_figure()
    #     timer.start(1000)#触发的时间间隔为1s
    #
    # '''绘制动态图，可以在这里定义或编辑 matplotlib.org/gallery'''
    # def update_figure(self):
    #     self.fig.suptitle('测试动态图')
    #     l=[random.randint(0,10) for i in range(4)]
    #     self.axes.plot([0,1,2,3],l,'r')
    #     self.axes.set_ylabel('动态图：Y轴')
    #     self.axes.set_xlabel('动态图：X轴')
    #     self.axes.grid(True)
    #     self.draw()

    def start_modelXZGraph(self,models):
        self.axes.cla()
        # print(models[0].m_geometry_center_x)
        if models.__len__():
            for model in models:
                if model.type()==model.modelType_Sphere:
                    circle = plt.Circle((model.m_geometry_center_x, model.m_geometry_center_z),
                                        radius=model.m_geometry_radius,alpha=0.8,edgecolor='black')
                    self.axes.add_patch(circle)
                    self.axes.autoscale_view()

                if model.type()==model.modelType_RectPrism:
                    x1=model.m_geometry_center_x - model.m_geometry_xLen / 2
                    z1=model.m_geometry_center_z - model.m_geometry_zLen / 2
                    rect=plt.Rectangle((x1, z1), model.m_geometry_xLen, model.m_geometry_zLen,alpha=0.8,edgecolor='black')
                    self.axes.add_patch(rect)
                    self.axes.autoscale_view()

            self.axes.set_xlabel('X')
            self.axes.set_ylabel('Z')

            self.draw()  # 必须有
            # self.show()
            # print(self.axes.axis()[0])
            xLen = self.axes.axis()[1]-self.axes.axis()[0]
            x0 = (self.axes.axis()[1]+self.axes.axis()[0])/2
            zLen = self.axes.axis()[2] - self.axes.axis()[3]
            z0 = (self.axes.axis()[3] + self.axes.axis()[2]) / 2
            if xLen>zLen:
                self.axes.set_ylim(z0-xLen/2,z0+xLen/2)
            else:
                self.axes.set_xlim(x0 - zLen / 2, x0 + zLen / 2)

            self.axes.axis('equal')
            self.axes.invert_yaxis()  # y轴翻转

    def start_modelXYGraph(self,models):
        self.axes.cla()
        if models.__len__():
            for model in models:
                if model.type()==model.modelType_Sphere:
                    circle = plt.Circle((model.m_geometry_center_x, model.m_geometry_center_y),
                                        radius=model.m_geometry_radius,alpha=0.8,edgecolor='black')
                    self.axes.add_patch(circle)
                    self.axes.autoscale_view()
                if model.type()==model.modelType_RectPrism:
                    x1=model.m_geometry_center_x - model.m_geometry_xLen / 2
                    y1=model.m_geometry_center_y - model.m_geometry_yLen / 2
                    rect=plt.Rectangle((x1, y1), model.m_geometry_xLen, model.m_geometry_yLen,alpha=0.8,edgecolor='black')
                    self.axes.add_patch(rect)
                    self.axes.autoscale_view()

            self.axes.set_xlabel('X')
            self.axes.set_ylabel('Y')
            self.draw()  # 必须有

            xLen = self.axes.axis()[1] - self.axes.axis()[0]
            x0 = (self.axes.axis()[1] + self.axes.axis()[0]) / 2
            yLen = self.axes.axis()[2] - self.axes.axis()[3]
            y0 = (self.axes.axis()[3] + self.axes.axis()[2]) / 2
            if xLen > yLen:
                self.axes.set_ylim(y0 - xLen / 2, y0 + xLen / 2)
            else:
                self.axes.set_xlim(x0 - yLen / 2, x0 + yLen / 2)
            self.axes.axis('equal')

    def start_modelYZGraph(self,models):
        self.axes.cla()
        if models.__len__():
            for model in models:
                if model.type()==model.modelType_Sphere:
                    circle = plt.Circle((model.m_geometry_center_y, model.m_geometry_center_z),
                                        radius=model.m_geometry_radius,alpha=0.8,edgecolor='black')
                    self.axes.add_patch(circle)
                    self.axes.autoscale_view()

                if model.type()==model.modelType_RectPrism:
                    y1=model.m_geometry_center_y - model.m_geometry_yLen / 2
                    z1 = model.m_geometry_center_z - model.m_geometry_zLen / 2
                    rect=plt.Rectangle((y1, z1), model.m_geometry_yLen, model.m_geometry_zLen,alpha=0.8,edgecolor='black')
                    self.axes.add_patch(rect)
                    self.axes.autoscale_view()

            self.axes.set_xlabel('Y')
            self.axes.set_ylabel('Z')

            self.draw()  # 必须有

            yLen = self.axes.axis()[1] - self.axes.axis()[0]
            y0 = (self.axes.axis()[1] + self.axes.axis()[0]) / 2
            zLen = self.axes.axis()[2] - self.axes.axis()[3]
            z0 = (self.axes.axis()[3] + self.axes.axis()[2]) / 2
            if yLen > zLen:
                self.axes.set_ylim(z0 - yLen / 2, z0 + yLen / 2)
            else:
                self.axes.set_xlim(y0 - zLen / 2, y0 + zLen / 2)
            self.axes.axis('equal')
            self.axes.invert_yaxis()  # y轴翻转

    def start_model3DGraph(self,models):
        from mpl_toolkits.mplot3d import Axes3D
        self.axes.cla()
        self.axes = Axes3D(self.fig)
        if models.__len__():
            for model in models:
                if model.type()==model.modelType_Sphere:
                    u = np.linspace(0, 2 * np.pi, 200)
                    v = np.linspace(0, np.pi, 200)
                    x = model.m_geometry_radius * np.outer(np.cos(u), np.sin(v)) + model.m_geometry_center_x
                    y = model.m_geometry_radius * np.outer(np.sin(u), np.sin(v)) + model.m_geometry_center_y
                    z = model.m_geometry_radius * np.outer(np.ones(np.size(u)), np.cos(v)) + model.m_geometry_center_z

                    self.axes.plot_surface(x,y,z,alpha=0.8)
                if model.type()==model.modelType_RectPrism:
                    x = model.m_geometry_center_x - model.m_geometry_xLen / 2
                    dx=model.m_geometry_xLen
                    y = model.m_geometry_center_y - model.m_geometry_yLen / 2
                    dy=model.m_geometry_yLen
                    z = model.m_geometry_center_z - model.m_geometry_zLen / 2
                    dz=model.m_geometry_zLen

                    xx=np.linspace(x,x+dx,2)
                    yy=np.linspace(y,y+dy,2)
                    zz=np.linspace(z,z+dz,2)

                    X,Y=np.meshgrid(xx,yy)

                    self.axes.plot_surface(X,Y,z*X/X,alpha=0.8)
                    self.axes.plot_surface(X,Y,(z+dz)*X/X,alpha=0.8)
                    Y,Z=np.meshgrid(yy,zz)

                    self.axes.plot_surface(x,Y,Z,alpha=0.8)
                    self.axes.plot_surface(x+dx, Y, Z,alpha=0.8)

                    X,Z=np.meshgrid(xx,zz)

                    self.axes.plot_surface(X,y,Z,alpha=0.8)
                    self.axes.plot_surface(X,y+dy,Z,alpha=0.8)
            self.axes.set_xlabel('X')
            self.axes.set_ylabel('Y')
            self.axes.set_zlabel('Z')
            # print(self.axes.get_zlim())
            xLen = self.axes.axis()[1] - self.axes.axis()[0]
            x0 = (self.axes.axis()[1] + self.axes.axis()[0]) / 2
            yLen = self.axes.axis()[2] - self.axes.axis()[3]
            y0 = (self.axes.axis()[3] + self.axes.axis()[2]) / 2
            zLen = self.axes.get_zlim()[1]-self.axes.get_zlim()[0]
            z0=(self.axes.get_zlim()[1]+self.axes.get_zlim()[0])/2
            if xLen>yLen:
                len=xLen
            else:
                len=yLen
            if len<zLen:
                len=zLen
            self.axes.set_ylim(y0 - len / 2, y0 + len / 2)
            self.axes.set_xlim(x0 - len / 2, x0 + len / 2)
            self.axes.set_zlim(z0 - len / 2, z0 + len / 2)
            self.axes.invert_zaxis()  # z轴翻转
            # self.axes.zaxis('sequence')
            self.draw()  # 必须有
            # self.show()
            plt.axis('equal')



    def start_contourMap(self,info,forwardData):
        # self.fig.suptitle(u'等值线图')
        x=np.linspace(info.xMin,info.xMax,info.cols)
        y=np.linspace(info.yMin,info.yMax,info.rows)
        X, Y = np.meshgrid(x, y)

        self.axes.cla()
        cs=self.axes.contourf(X, Y, forwardData,cmap='hsv')
        if self.cb:
            # self.cb.remove()
            self.cb = self.fig.colorbar(cs,self.cb.ax)#在原来的色棒上修改
        else:
            self.cb=self.fig.colorbar(cs)

        C = self.axes.contour(X, Y, forwardData)
        self.axes.clabel(C, inline=True, fontsize=10,fmt='%.4f')

        self.axes.set_xlabel('X',fontsize=14)
        self.axes.set_ylabel('Y',fontsize=14)
        self.draw()  # 必须有


    def start_surface3D(self,info,txt,forwardData):#txt表示z轴label
        from mpl_toolkits.mplot3d import Axes3D
        # from mpl_toolkits.mplot3d import axes3d
        # self.fig.suptitle(u'三维曲面图')
        x = np.linspace(info.xMin, info.xMax, info.cols)
        y = np.linspace(info.yMin, info.yMax, info.rows)
        X, Y = np.meshgrid(x, y)
        self.axes=Axes3D(self.fig)
        # self.axes=self.fig.gca(projection='3d')
        self.axes.cla()
        self.axes.plot_surface(X,Y,forwardData,cmap='jet')
        # self.axes.contourf(X,Y,forwardData,zdir='z',offset=0)
        # self.axes.set_zlim(0)
        self.axes.set_xlabel('X',fontsize=14)
        self.axes.set_ylabel('Y',fontsize=14)
        self.axes.set_zlabel(txt,fontsize=14)
        self.axes.grid(True)
        # self.axes.view_init(30,45)
        # self.axes.up
        # plt.show()
        self.draw()#必须有

    # def start_surface3D(self):#做实验
    #     from mpl_toolkits.mplot3d import Axes3D
    #     # self.fig.suptitle(u'三维曲面图')
    #     x = np.linspace(-10, 10, 20)
    #     y=np.linspace(-10,10,20)
    #     X, Y = np.meshgrid(x, y)
    #     forwardData=X**2+Y**2
    #     self.axes = Axes3D(self.fig)
    #     self.axes.plot_surface(X, Y, forwardData)#, rstride=1, cstride=1)

    # def start_contourMap(self):#做实验
    #     self.fig.suptitle(u'等值线图')
    #     x=np.linspace(-10,10,20)
    #     y=np.linspace(-10,10,20)
    #     X, Y = np.meshgrid(x, y)
    #     forwardData=X**2+Y**2
    #     cs=self.axes.contourf(X, Y, forwardData)#,20#, alpha=0.5#, cmap=plt.cm.hot)
    #     C = self.axes.contour(X, Y, forwardData)#, 20, colors='black', linewidths=0.1)
    #     self.axes.clabel(C, inline=True, fontsize=10,fmt='%.4f')
    #     self.fig.colorbar(cs)
    #     self.draw()

    # def setCmap(self,cmap):
    #     self.axes

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    ui=MatplotlibWidget()
    # ui.mpl.start_static_plot()#测试静态图效果
    # ui.mpl.start_dynamic_plot()#测试动态图效果
    # ui.mpl.start_contourMap()
    ui.mpl.start_surface3D()
    ui.show()
    sys.exit(app.exec_())

