from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mouvement"
        self.TypeForme="Rectangle"
        self.Texte="Aller aux coordonnées X et Y"
        self.Parametres=[['Label', 'aller a x:'], ['EmptyCercle'], ['Label', ' y :'], ['EmptyCercle']]
        self.Color=Couleurs.bleu_fonce
        self.Compile="GotoXY"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    
