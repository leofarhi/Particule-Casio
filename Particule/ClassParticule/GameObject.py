from ClassParticule.Object import Object
from ClassParticule.Components.Transform import Transform
from ClassParticule.Tag import Tag
from ClassParticule.Layer import Layer
from Particule import *
import os,sys
from Particule import *
class GameObject(Object):
    def __init__(self,Particule,name="",scene="",**kwargs):
        Object.__init__(self,Particule,name,**kwargs)
        self.activeInHierarchy = True
        self.activeSelf = True
        self.isStatic = False
        self.layer = Layer.Default
        self.scene = scene
        self.sceneCullingMask = ""
        self.tag = Tag.Untagged
        self.transform = Transform(self)
        self.ListOfComponent=[self.transform]
        self.Order = 0

        self.OpenIsHierarchy = 0

        if self.scene!="" and self.scene in self.Particule.Scene.scenes:
            indexScene = self.Particule.Scene.scenes.index(self.scene)
            if not self.ID in self.Particule.Scene.UUID_Objects[indexScene]:
                self.Particule.Scene.UUID_Objects[indexScene].update({self.ID:self})


    def SaveDataDict(self):
        self.OpenIsHierarchy = self.Particule.Hierarchy.t.item(self.ID)['open']
        TempDico = {"name": self.name,
                    ""
                    "activeInHierarchy": self.activeInHierarchy,
                    "activeSelf": self.activeSelf,
                    "isStatic": self.isStatic,
                    "layer": self.layer.value,
                    "scene": self.scene,
                    "sceneCullingMask": self.sceneCullingMask,
                    "tag": self.tag.value,
                    "transform": self.transform.ID,
                    "Order": self.Order,
                    "ListOfComponent": [i.ID for i in self.ListOfComponent],

                    "OpenIsHierarchy": self.OpenIsHierarchy
                    }
        return TempDico

    def Copy(self):
        DicoCompo = {}
        for i in self.ListOfComponent:
            DicoCompo.update(i.Copy())
        DicoSave = self.SaveDataDict()
        DicoSave["TypeObject"]="GameObject"
        DicoSave["ListOfComponent"] = DicoCompo
        Data = {self.ID:DicoSave}
        for Tchild in self.transform.childs:
            Data.update(Tchild.gameObject.Copy())
        return Data

    def ChangeActifSelf(self):
        for component in self.ListOfComponent:
            component.ChangeActifSelf()

    def UpdateOnGUI(self):
        if self.scene!="" and self.scene in self.Particule.Scene.scenes:
            indexScene = self.Particule.Scene.scenes.index(self.scene)
            if not self.ID in self.Particule.Scene.UUID_Objects[indexScene]:
                self.Particule.Scene.UUID_Objects[indexScene].update({self.ID:self})
        if self.transform.parent == None:
            self.activeInHierarchy = True
        else:
            parent = self.transform.parent.gameObject
            self.activeInHierarchy = (parent.activeSelf and parent.activeInHierarchy)
            if self.activeSelf and self.activeInHierarchy:
                tag = 'Active'
            else :
                tag = 'Desactive'
            try:
                self.Particule.Hierarchy.t.item(str(self.ID),  tags=(tag))
            except:
                pass
        for component in self.ListOfComponent:
            component.UpdateOnGUI()
            if component.myFrame != None:
                if component.myFrame.winfo_ismapped() == 1:
                    component.WhenComponentIsShow()
                else:
                    component.WhenComponentIsHide()
    def AddComponent(self,ClassComponent):
        temp = ClassComponent(self)#getattr(sys.modules['Particule'], ClassComponent.__name__)(self)
        self.ListOfComponent.append(temp)
        self.Particule.Inspector.UpdateItemSelected()
        self.Particule.Inspector.focus_set()
        return temp

    def AddComponentByName(self,name):
        for compo in self.Particule.AllComponent:
            if name == (compo.__name__).split(".")[-1]:
                self.AddComponent(compo)


    def Destroy(self):
        Object.Destroy(self)
        if self.scene != "" and self.scene in self.Particule.Scene.scenes:
            indexScene = self.Particule.Scene.scenes.index(self.scene)
            if self.ID in self.Particule.Scene.UUID_Objects[indexScene]:
                del (self.Particule.Scene.UUID_Objects[indexScene])[self.ID]
        while len(self.ListOfComponent)>0:
            self.ListOfComponent[0].Destroy()
    def BroadcastMessage(self):
        pass
    def CompareTag(self):
        pass
    def GetComponent(self,TYPE):
        for i in self.ListOfComponent:
            if type(i)==TYPE:
                return i
        return None
    def GetComponentInChildren(self):
        pass
    def GetComponentInParent(self):
        pass
    def GetComponents(self):
        pass
    def GetComponentsInChildren(self):
        pass
    def GetComponentsInParent(self):
        pass
    def SendMessage(self):
        pass
    def SendMessageUpwards(self):
        pass
    def SetActive(self):
        pass
    def TryGetComponent(self):
        pass
    def CreatePrimitive(self):
        pass
    def Find(self):
        pass
    def FindGameObjectsWithTag(self):
        pass
    def FindWithTag(self):
        pass
