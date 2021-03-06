from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame
from ClassSystem.Notebook import Notebook
from tkinter import ttk
from ClassParticule.Texture import Texture
import platform

class SearchWindow(EditorWindow):
    def __init__(self, RootWindow,Object,TypeSearch):
        self.Object = Object
        #bt = RootWindow.Particule.Inspector.Bouton_AddComponent
        #geo = str(bt.winfo_width()) + "x250"
        #geo += "+" + str(bt.winfo_rootx()) + "+" + str(bt.winfo_rooty() + bt.winfo_height())
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name": "Search", "geometry": "250x250"},
                              Resize=False, ScrollbarShow=False)
        self.pack(fill=tkinter.BOTH, expand=True)
        self.focus_set()



        self.var_barreRecherche = StringVar()
        self.SearchBar =  Entry(self, textvariable=self.var_barreRecherche)
        self.SearchBar.pack(fill=X)
        self.SearchBar.bind('<KeyRelease>', self.rechercheBind)

        onglets = ttk.Notebook(self)
        onglets.pack(fill=BOTH, expand=True)

        self.FolderFrame = ttk.Frame(onglets)
        self.SceneFrame = ttk.Frame(onglets)
        self.FolderFrame.pack(fill=BOTH, expand=True)
        #self.SceneFrame.pack(fill=BOTH, expand=True)

        onglets.add(self.FolderFrame, text='All')#'Folder')
        #onglets.add(self.SceneFrame, text='Scene')

        scrollbarFolder = Scrollbar(self.FolderFrame)
        scrollbarFolder.pack(side=RIGHT, fill=Y)

        self.mylistFolder = Listbox(self.FolderFrame, yscrollcommand=scrollbarFolder.set)
        self.mylistFolder.bind('<<ListboxSelect>>', self.Selected)

        self.LstObjFound=[]
        for UUID,Obj in list(self.Particule.All_UUID.items()):
            if type(Obj)==TypeSearch or issubclass(type(Obj),TypeSearch):
                if TypeSearch == Texture:
                    if Obj.fileVariable!=None and Obj.fileVariable.IsHide:continue
                self.LstObjFound.append((UUID,Obj))
                self.mylistFolder.insert(END, str(Obj))


        self.mylistFolder.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbarFolder.config(command=self.mylistFolder.yview)
        if platform.system().lower() == "linux":
            self.RootWindow.protocol("WM_DELETE_WINDOW", self.OnLostFocus)

        """
        #####################

        scrollbarScene = Scrollbar(self.SceneFrame)
        scrollbarScene.pack(side=RIGHT, fill=Y)

        self.mylistScene = Listbox(self.SceneFrame, yscrollcommand=scrollbarScene.set)
        for line in range(100):
            self.mylistScene.insert(END, "This is line Scene " + str(line))

        self.mylistScene.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbarScene.config(command=self.mylistScene.yview)
        """

    def Selected(self,event):
        w = event.widget
        index = int(w.curselection()[0])
        self.Object.Data = (self.LstObjFound[index])[1]
        self.Object.changeOther()
        self.Particule.Inspector.UpdateItemSelected()

    def ClearListe(self):
        self.mylistFolder.delete(0, END)
        #self.mylistScene.delete(0, END)

    def rechercheBind(self,_):
        self.ClearListe()
        for elem in self.LstObjFound:
            name = elem[1].name
            if not self.var_barreRecherche.get().lower() in name.lower():
                continue
            self.mylistFolder.insert(END, str(elem[1]))


    def OnLostFocus(self,_=None):
        if platform.system().lower() == "linux":
            self.Particule.UpdateOnFocus()
        self.RootWindow.destroy()

