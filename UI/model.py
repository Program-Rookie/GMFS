# -*- coding: utf-8 -*-
class Model:
    def __init__(self,modelType):
        self.modelType=modelType
        self.modelType_Sphere=0#与ForwarCenterWidget中保持一致
        self.modelType_RectPrism=1

        self.I = 90  # 磁化方向倾角(度)
        self.D = 0  # 磁化方向偏角(度)
        self.M = 1 #磁化强度(A/m)
        self.K = 0.1  # 磁化率（SI）

        self.density = 1  # 密度（g/cm^3）

        if self.modelType==self.modelType_Sphere:
            self.m_geometry_center_x = 0
            self.m_geometry_center_y = 0
            self.m_geometry_center_z = 100
            self.m_geometry_radius = 50

        if self.modelType==self.modelType_RectPrism:
            self.m_geometry_center_x = 0
            self.m_geometry_center_y = 0
            self.m_geometry_center_z = 20
            self.m_geometry_xLen = 10
            self.m_geometry_yLen = 10
            self.m_geometry_zLen = 10

    def type(self):
        return self.modelType