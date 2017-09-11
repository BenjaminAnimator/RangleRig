"""
UI Module
"""
import maya.cmds as mc
import maya.mel as mel
from functools import partial
from _functools import partial
from RangleRig.setUpModules import symHumanSetUp
from RangleRig import Assembler


class SetupUI:
    def __init__(self):
        self.title = "Rangle Rig: Rig Creation UI"
        if(mc.window(self.title, exists = True)):
            mc.deleteUI(self.title)
        self.window = mc.window(self.title, widthHeight=(300, 50),
        resizeToFitChildren=1)
               
        
        topLayout = mc.columnLayout(adjustableColumn=True, columnAlign="center",rowSpacing=10)
        self.CharaterName = mc.textFieldGrp(label = 'Rig_Name')
        setUpLayout= mc.tabLayout()
        
        premadeLayout = mc.rowColumnLayout(parent = setUpLayout,  numberOfColumns = 2, columnSpacing = [100,100], rowSpacing =  [50,50])
        
        self.loadHumanBipedSETUP = mc.iconTextButton(style = 'iconAndTextHorizontal',label = 'SetUp Human Biped',command = self.setUpHuman, parent = premadeLayout)
        self.loadQuadrupedSETUP = mc.button(label = 'SetUp Basic Quadruped (CURRENTLY NOT AVALIBLE)', parent = premadeLayout, enable = False)
        
        
        
        additionsLayout = mc.gridLayout(parent = setUpLayout)
        
        mc.tabLayout(setUpLayout, edit = True, tabLabel =((premadeLayout, 'Premade Set Ups'),(additionsLayout,'Additional Parts / Custom Setup Rigs')))
        
        
        
        
        self.loadRigBiped= mc.button(label = 'Create Rig',command = self.createRig, parent = topLayout)
        
        
        mc.showWindow(self.window)
        
    def setUpHuman(self,*args):
        name = mc.textFieldGrp(self.CharaterName, query = True, text =True)
        print 'NAME !%s'%name
        if name == '':
            mc.error("Rig must be named")
        else:
            self.setUp = symHumanSetUp.humanSetUp(name)

            

        
    def createRig(self,*args):
        name = mc.textFieldGrp(self.CharaterName, query = True, text =True)
        if name == '':
            mc.error("Rig  must be named")
        else:
            Assembler.assembleRig(name)
GO = SetupUI()
        





