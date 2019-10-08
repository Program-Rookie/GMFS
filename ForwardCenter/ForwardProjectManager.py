# -*- coding: utf-8 -*-
from UI.ForwardProject import *

class yForwardProjectManager:
    m_forwardProjs=[]

    def __del__(self):
        self.clearAll

    def clearAll(self):# 全部清除
        for p in self.m_forwardProjs:
            del p
        self.m_forwardProjs.clear()

    def createProject(self,projectType):# 创建项目0 重 1磁
        p=ForwardProject(projectType)
        self.m_forwardProjs.append(p)
        return p

    def deleteProject(self,p):# 删除项目
        self.m_forwardProjs.remove(p)

    def getCountOfProject(self):
        return self.m_forwardProjs.__len__()

