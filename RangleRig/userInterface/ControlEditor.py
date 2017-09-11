import maya.cmds as mc
import maya.mel as mel
from functools import partial
from _functools import partial


class ControlEdUI:
    def __init__(self):
        self.title = "Rangle Rig: Control Editor UI"
        if(mc.window(self.title, exists = True)):
            mc.deleteUI(self.title)
        self.window = mc.window(self.title, widthHeight=(400, 600),
        resizeToFitChildren=1)
        rootLayout = mc.columnLayout(adjustableColumn = True)
        
        #Rig Finder
        mc.button(label = "Find Rigs", command = self.findRigs, parent = rootLayout )
        self.rigList = mc.optionMenu(label = 'Chosen Rig', changeCommand = self.setCharacter)
        mc.menuItem('None', parent = self.rigList)
        self.listRigs = []
        
        #Control Finder
        mc.button(label = "Find Controls", command = self.findControls, parent = rootLayout )
        self.controlList = mc.optionMenu(label = 'Chosen Control', changeCommand = self.setControl)
        mc.menuItem('None', parent = self.controlList)
        self.listcontrols = []
        
        #Control Translation Tweak
        self.transXField =  mc.floatSliderGrp(field = True, label = 'Translate X', precision = 3, 
                                              changeCommand = self.Translation, minValue = -1, maxValue = 1, value = 0)
        self.transYField =  mc.floatSliderGrp(field = True, label = 'Translate Y', precision = 3, 
                                              changeCommand = self.Translation, minValue = -1, maxValue = 1, value = 0)
        self.transZField =  mc.floatSliderGrp(field = True, label = 'Translate Z', precision = 3, 
                                              changeCommand = self.Translation, minValue = -1, maxValue = 1, value = 0)
 
        #Control Rotation Tweak
        self.rotXField =  mc.floatSliderGrp(field = True, label = 'Rotation X', precision = 3, 
                                              changeCommand = self.Rotation, minValue = -90, maxValue = 90, value = 0)
        self.rotYField =  mc.floatSliderGrp(field = True, label = 'Rotation Y', precision = 3, 
                                              changeCommand = self.Rotation, minValue = -90, maxValue = 90, value = 0)
        self.rotZField =  mc.floatSliderGrp(field = True, label = 'Rotation Z', precision = 3, 
                                              changeCommand = self.Rotation, minValue = -90, maxValue = 90, value = 0)
        #Control Scale Tweak
        self.UniformCheck = mc.checkBoxGrp(label = 'Uniform Scale', onCommand = self.onScale, offCommand = self.offScale)
        self.scaleUniField =  mc.floatSliderGrp(field = True, label = 'Scale Uniform', precision = 3, 
                                              changeCommand = self.Scale, minValue = 0.01, maxValue = 2, value = 1)
        self.scaleXField =  mc.floatSliderGrp(field = True, label = 'Scale X', precision = 3, 
                                              changeCommand = self.Scale, minValue = 0.01, maxValue = 2, value = 1)
        self.scaleYField =  mc.floatSliderGrp(field = True, label = 'Scale Y', precision = 3, 
                                              changeCommand = self.Scale, minValue = 0.01, maxValue = 2, value = 1)
        self.scaleZField =  mc.floatSliderGrp(field = True, label = 'Scale Z', precision = 3, 
                                              changeCommand = self.Scale, minValue = 0.01, maxValue = 2, value = 1)
                     
        
        mc.showWindow(self.window)
    
    '''
    Rig Finder Function
    '''
    def findRigs(self, *args):
        
        charList = []
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            query = mc.attributeQuery('sceneObjectType', node = i,  exists= True)
            if query == True:
                queryVal = mc.getAttr(i+'.sceneObjectType')
                if queryVal == 'rig':
                    self.charName = mc.getAttr(i + '.characterName' )
                    charList.append(self.charName)
        print charList    
        for i in charList:          
            if i in self.listRigs:
                mc.error("Rig already in list")
            else:
                menuItem = mc.menuItem(i, parent = self.rigList)
                rig = mc.menuItem(menuItem, query = True, label= True)
                self.listRigs.append(rig)
                print self.listRigs[0]
                
    def setCharacter(self,*args):
        self.actChar =  mc.optionMenu(self.rigList,query = True, value =True)
        print self.actChar
    
    '''
    Control Finder Functions
    '''
    def findControls(self, *args):
        menuItems = mc.optionMenu(self.controlList, q=True, itemListLong=True) # itemListLong returns the children
        if menuItems:
            mc.deleteUI(menuItems)
        conList = []
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            query = mc.attributeQuery('characterName', node = i,  exists= True)
            if query == True:
                queryVal = mc.getAttr(i+'.characterName')
                if queryVal == self.actChar:
                    queryConArea =  mc.attributeQuery('controlArea', node = i,  exists= True)
                    if queryConArea == True:
                        conList.append(i)
        print conList    
        for i in conList:          
            if i in self.listcontrols:
                mc.error("Control already in list")
            else:
                menuItem = mc.menuItem(i, parent = self.controlList)
                con = mc.menuItem(menuItem, query = True, label= True)
                self.listcontrols.append(con)
                print self.listcontrols[0]
                
    def setControl(self,*args):
        self.actCon =  mc.optionMenu(self.controlList,query = True, value =True)
        print self.actCon    
    
    
    
    
    
    def onScale(self,*args):    
        mc.floatSliderGrp(self.scaleXField,edit = True, enable = False)
        mc.floatSliderGrp(self.scaleYField, edit = True, enable = False )
        mc.floatSliderGrp(self.scaleZField, edit = True, enable = False)
        mc.floatSliderGrp(self.scaleUniField, edit = True, enable = True)
    
    def offScale(self,*args):    
        mc.floatSliderGrp(self.scaleXField,edit = True, enable = True)
        mc.floatSliderGrp(self.scaleYField, edit = True, enable = True )
        mc.floatSliderGrp(self.scaleZField, edit = True, enable = True)
        mc.floatSliderGrp(self.scaleUniField, edit = True, enable = False)        
        


    
    
    def Scale(self, *args):
        query = mc.checkBoxGrp(self.UniformCheck, query = True, value1= True)
        sclValX = mc.floatSliderGrp(self.scaleXField, query = True, value = True)
        sclValY = mc.floatSliderGrp(self.scaleYField, query = True, value = True)
        sclValZ = mc.floatSliderGrp(self.scaleZField, query = True, value = True)
        sclValUni = mc.floatSliderGrp(self.scaleUniField, query = True, value = True)
        active = [self.actCon]
        
        if query == True:
            for i in active:
                mc.select(i + '.cv[0:]')
                mc.scale(sclValUni,sclValUni,sclValUni, absolute =True)
                mc.floatSliderGrp(self.scaleUniField, edit =True, value = 1)

        elif query == False:
            for i in active:
                mc.select(i + '.cv[0:]')
                mc.scale(sclValX,sclValY,sclValZ, absolute =True)
                mc.floatSliderGrp(self.scaleXField, edit =True, value = 1)
                mc.floatSliderGrp(self.scaleYField, edit =True, value = 1)
                mc.floatSliderGrp(self.scaleZField, edit =True, value = 1)
            
    def Translation(self, *args):
        
        transValX = mc.floatSliderGrp(self.transXField, query = True, value = True)
        transValY = mc.floatSliderGrp(self.transYField, query = True, value = True)
        transValZ = mc.floatSliderGrp(self.transZField, query = True, value = True)
        active = [self.actCon]
        for i in active:
            mc.select(i + '.cv[0:]')
            mc.xform( translation = [transValX,transValY,transValZ], worldSpace = True, relative =True)
            mc.floatSliderGrp(self.transXField, edit = True, value = 0)
            mc.floatSliderGrp(self.transYField, edit = True, value = 0)
            mc.floatSliderGrp(self.transZField, edit = True, value = 0)
            
            
    def Rotation(self, *args):
        
        rotValX = mc.floatSliderGrp(self.rotXField, query = True, value = True)
        rotValY = mc.floatSliderGrp(self.rotYField, query = True, value = True)
        rotValZ = mc.floatSliderGrp(self.rotZField, query = True, value = True)
        active = [self.actCon]
        for i in active:
            mc.select(i + '.cv[0:]')
            mc.rotate(rotValX,rotValY,rotValZ, objectSpace = True, relative =True)
            mc.floatSliderGrp(self.rotXField, edit = True, value = 0)
            mc.floatSliderGrp(self.rotYField, edit = True, value = 0)
            mc.floatSliderGrp(self.rotZField, edit = True, value = 0)

GO = ControlEdUI()