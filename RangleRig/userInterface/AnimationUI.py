import maya.cmds as mc
import maya.mel as mel
from functools import partial
from _functools import partial


class AnimUI:
    def __init__(self):
        self.title = "Rangle Rig: Animation UI"
        if(mc.window(self.title, exists = True)):
            mc.deleteUI(self.title)
        self.window = mc.window(self.title, widthHeight=(400, 600),
        resizeToFitChildren=1)
        rootLayout = mc.columnLayout(adjustableColumn = True)

        
        
        
        mc.button(label = "Find Rigs", command = self.findRigs, parent = rootLayout )
        self.rigList = mc.optionMenu(label = 'Chosen Rig', changeCommand = self.setCharacter)
        mc.menuItem('None', parent = self.rigList)
        
        #Spine Controls
        spineLayout = mc.rowColumnLayout(numberOfColumns=1 )
        self.spineKeyButton = mc.button(label = "Spine Key", command = self.SpineKey )
        self.spinIkFkKey = mc.optionMenu(label = 'Fk/Ik Key' )
        mc.menuItem('FK', parent = self.spinIkFkKey )
        mc.menuItem('IK', parent = self.spinIkFkKey )
        mc.menuItem('Both', parent = self.spinIkFkKey )
        self.spinIkFkVis = mc.optionMenu(label = 'Fk/Ik Vis', changeCommand = self.SpineVis )
        mc.menuItem('FK', parent = self.spinIkFkVis )
        mc.menuItem('IK', parent = self.spinIkFkVis )
        mc.menuItem('Both', parent = self.spinIkFkVis )
        mc.menuItem('None', parent = self.spinIkFkVis )
        
        #Left Leg Controls
        L_LegLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(L_LegLayout, topLevel =True)
        self.L_legKeyButton = mc.button(label = " Left Leg Key All", command = self.L_LegKey )
        self.L_legIkFkKey = mc.optionMenu(label = 'Fk/Ik Key' )
        mc.menuItem('FK', parent = self.L_legIkFkKey )
        mc.menuItem('IK', parent = self.L_legIkFkKey )
        mc.menuItem('Both', parent = self.L_legIkFkKey )
        self.L_legIkFkVis = mc.optionMenu(label = 'Fk/Ik Vis', changeCommand = self.L_LegVis )
        mc.menuItem('FK', parent = self.L_legIkFkVis )
        mc.menuItem('IK', parent = self.L_legIkFkVis )
        mc.menuItem('Both', parent = self.L_legIkFkVis )
        mc.menuItem('None', parent = self.L_legIkFkVis )
        self.L_legIkFkActiv = mc.optionMenu(label = 'Active Fk/Ik', changeCommand = self.L_LegActive )
        mc.menuItem('FK', parent = self.L_legIkFkActiv )
        mc.menuItem('IK', parent = self.L_legIkFkActiv )
        #self.matchL_leg= mc.button(label = 'Match:')
        #self.matchToL_leg = mc.optionMenu()
        #mc.menuItem('Fk -> Ik', parent = self.matchToL_leg )
        #mc.menuItem('Ik -> Fk', parent = self.matchToL_leg )

        
        #Right Leg Controls
        R_LegLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(R_LegLayout, topLevel =True)
        self.R_legKeyButton = mc.button(label = "Right Leg Key All", command = self.R_LegKey )
        self.R_legIkFkKey = mc.optionMenu(label = 'Fk/Ik Key' )
        mc.menuItem('FK', parent = self.R_legIkFkKey )
        mc.menuItem('IK', parent = self.R_legIkFkKey )
        mc.menuItem('Both', parent = self.R_legIkFkKey )
        self.R_legIkFkVis = mc.optionMenu(label = 'Fk/Ik Vis', changeCommand = self.R_LegVis )
        mc.menuItem('FK', parent = self.R_legIkFkVis )
        mc.menuItem('IK', parent = self.R_legIkFkVis )
        mc.menuItem('Both', parent = self.R_legIkFkVis )
        mc.menuItem('None', parent = self.R_legIkFkVis )
        self.R_legIkFkActiv = mc.optionMenu(label = 'Active Fk/Ik', changeCommand = self.R_LegActive )
        mc.menuItem('FK', parent = self.R_legIkFkActiv )
        mc.menuItem('IK', parent = self.R_legIkFkActiv )
        #self.matchR_leg= mc.button(label = 'Match:')
        #self.matchToR_leg = mc.optionMenu()
        #mc.menuItem('Fk -> Ik', parent = self.matchToR_leg )
        #mc.menuItem('Ik -> Fk', parent = self.matchToR_leg )
        
        #Left Arm Controls
        L_ArmLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(L_ArmLayout, topLevel =True)
        self.L_armKeyButton = mc.button(label = " Left Arm Key All", command = self.L_ArmKey )
        self.L_armIkFkKey = mc.optionMenu(label = 'Fk/Ik Key' )
        mc.menuItem('FK', parent = self.L_armIkFkKey )
        mc.menuItem('IK', parent = self.L_armIkFkKey )
        mc.menuItem('Both', parent = self.L_armIkFkKey )
        self.L_armIkFkVis = mc.optionMenu(label = 'Fk/Ik Vis', changeCommand = self.L_ArmVis )
        mc.menuItem('FK', parent = self.L_armIkFkVis )
        mc.menuItem('IK', parent = self.L_armIkFkVis )
        mc.menuItem('Both', parent = self.L_armIkFkVis )
        mc.menuItem('None', parent = self.L_armIkFkVis )
        self.L_armIkFkActiv = mc.optionMenu(label = 'Active Fk/Ik', changeCommand = self.L_ArmActive )
        mc.menuItem('FK', parent = self.L_armIkFkActiv )
        mc.menuItem('IK', parent = self.L_armIkFkActiv )
        #self.matchL_arm= mc.button(label = 'Match:')
        #self.matchToL_arm = mc.optionMenu()
        #mc.menuItem('Fk -> Ik', parent = self.matchToL_arm )
        #mc.menuItem('Ik -> Fk', parent = self.matchToL_arm )        
        
        
        #Right Arm Controls
        R_ArmLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(R_ArmLayout, topLevel =True)
        self.R_armKeyButton = mc.button(label = " Right Arm Key All", command = self.R_ArmKey )
        self.R_armIkFkKey = mc.optionMenu(label = 'Fk/Ik Key' )
        mc.menuItem('FK', parent = self.R_armIkFkKey )
        mc.menuItem('IK', parent = self.R_armIkFkKey )
        mc.menuItem('Both', parent = self.R_armIkFkKey )
        self.R_armIkFkVis = mc.optionMenu(label = 'Fk/Ik Vis', changeCommand = self.R_ArmVis )
        mc.menuItem('FK', parent = self.R_armIkFkVis )
        mc.menuItem('IK', parent = self.R_armIkFkVis )
        mc.menuItem('Both', parent = self.R_armIkFkVis )
        mc.menuItem('None', parent = self.R_armIkFkVis )
        self.R_armIkFkActiv = mc.optionMenu(label = 'Active Fk/Ik', changeCommand = self.R_ArmActive )
        mc.menuItem('FK', parent = self.R_armIkFkActiv )
        mc.menuItem('IK', parent = self.R_armIkFkActiv )                 
        #self.matchR_arm= mc.button(label = 'Match:')
        #self.matchToR_arm = mc.optionMenu()
        #mc.menuItem('Fk -> Ik', parent = self.matchToR_arm )
        #mc.menuItem('Ik -> Fk', parent = self.matchToR_arm )         
       
        #Left Clav Controls
        L_ClavLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(L_ArmLayout, topLevel =True)
        self.L_clavKeyButton = mc.button(label = " Left Clavicle Key", command = self.L_ClavKey )
        self.L_clavVis = mc.optionMenu(label = 'Visibility', changeCommand = self.L_ClavVis )
        mc.menuItem('On', parent =  self.L_clavVis )
        mc.menuItem('Off', parent =  self.L_clavVis )


        #Right Clav Controls
        R_ClavLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(R_ArmLayout, topLevel =True)
        self.R_clavKeyButton = mc.button(label = " Right Clavicle Key", command = self.R_ClavKey )
        self.R_clavVis = mc.optionMenu(label = 'Visibility', changeCommand = self.R_ClavVis )
        mc.menuItem('On', parent =  self.R_clavVis )
        mc.menuItem('Off', parent =  self.R_clavVis )
        
        #Head Controls
        headLayout = mc.rowColumnLayout(numberOfRows=1 )
        mc.setParent(headLayout, topLevel =True)
        self.headKeyButton = mc.button(label = " Head Key", command = self.HeadKey )
        self.headKey = mc.optionMenu(label = 'Head/Neck Key' )
        mc.menuItem('head', parent = self.headKey )
        mc.menuItem('neck', parent = self.headKey )
        mc.menuItem('Both', parent = self.headKey )
        self.headVis = mc.optionMenu(label = 'Head Vis', changeCommand = self.HeadVis )
        mc.menuItem('Head', parent = self.headVis )
        mc.menuItem('Head and Neck', parent = self.headVis )
        mc.menuItem('None', parent = self.headVis)
        self.headTrans = mc.optionMenu(label = 'Head Trans', changeCommand = self.HeadTrans )
        mc.menuItem('World', parent = self.headTrans )
        mc.menuItem('Chest', parent = self.headTrans )
        mc.menuItem('Neck', parent = self.headTrans)  
        self.headOri = mc.optionMenu(label = 'Head Ori', changeCommand = self.HeadOri )
        mc.menuItem('World', parent = self.headOri )
        mc.menuItem('Chest', parent = self.headOri )
        mc.menuItem('Neck', parent = self.headOri)          
        self.listRigs = []
        mc.showWindow(self.window)

               
        


    '''
    Finding Rigs in Scene
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
    Spine Functions
    '''    
    def SpineKey(self,*args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'spine':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                print typeVal
                                keyableType = mc.optionMenu(self.spinIkFkKey,query = True, value =True)
                                if typeVal == keyableType:
                                    mc.setKeyframe(i)
                                elif keyableType == 'Both':
                                    mc.setKeyframe(i)
                                    
    def SpineVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.spinIkFkVis,query = True, value =True)
                                    if visType =='FK':
                                        set = 0
                                    elif visType =='IK':
                                        set = 1
                                    elif visType =='Both':
                                        set = 2
                                    elif visType =='None':
                                        set = 3
                                    mc.setAttr(i + '.Torso',set)
    
    '''
    L_leg Functions
    '''                            
    def L_LegKey(self,*args):
        
        #Used to set key frames on  FK, IK or Both controls on Left Leg
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'L_leg':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                print typeVal
                                keyableType = mc.optionMenu(self.L_legIkFkKey,query = True, value =True)
                                if typeVal == keyableType:
                                    mc.setKeyframe(i)
                                elif keyableType == 'Both':
                                    mc.setKeyframe(i)                
        
    def L_LegVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.L_legIkFkVis,query = True, value =True)
                                    if visType =='FK':
                                        set = 0
                                    elif visType =='IK':
                                        set = 1
                                    elif visType =='Both':
                                        set = 2
                                    elif visType =='None':
                                        set = 3
                                    mc.setAttr(i + '.L_leg',set)
                                    
    def L_LegActive(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'settings':
                                    setType = mc.optionMenu(self.L_legIkFkActiv,query = True, value =True)
                                    if setType =='FK':
                                        set = 0
                                    elif setType =='IK':
                                        set = 1

                                    mc.setAttr(i + '.L_leg_Fk_IK',set)
                                    
    def L_LegMatch(self,*args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'L_Leg':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )



    '''
    R_leg Functions
    '''                            
    def R_LegKey(self,*args):
        
        #Used to set key frames on  FK, IK or Both controls on Left Leg
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'R_leg':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                print typeVal
                                keyableType = mc.optionMenu(self.R_legIkFkKey,query = True, value =True)
                                if typeVal == keyableType:
                                    mc.setKeyframe(i)
                                elif keyableType == 'Both':
                                    mc.setKeyframe(i)                
        
    def R_LegVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.R_legIkFkVis,query = True, value =True)
                                    if visType =='FK':
                                        set = 0
                                    elif visType =='IK':
                                        set = 1
                                    elif visType =='Both':
                                        set = 2
                                    elif visType =='None':
                                        set = 3
                                    mc.setAttr(i + '.R_leg',set)
                                    
    def R_LegActive(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'settings':
                                    setType = mc.optionMenu(self.R_legIkFkActiv,query = True, value =True)
                                    if setType =='FK':
                                        set = 0
                                    elif setType =='IK':
                                        set = 1

                                    mc.setAttr(i + '.R_leg_Fk_IK',set)

    
    '''
    L_arm Functions
    '''                            
    def L_ArmKey(self,*args):
        
        #Used to set key frames on  FK, IK or Both controls on Left Leg
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'L_arm':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                print typeVal
                                keyableType = mc.optionMenu(self.L_armIkFkKey,query = True, value =True)
                                if typeVal == keyableType:
                                    mc.setKeyframe(i)
                                elif keyableType == 'Both':
                                    mc.setKeyframe(i)                
        
    def L_ArmVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.L_armIkFkVis,query = True, value =True)
                                    if visType =='FK':
                                        set = 0
                                    elif visType =='IK':
                                        set = 1
                                    elif visType =='Both':
                                        set = 2
                                    elif visType =='None':
                                        set = 3
                                    mc.setAttr(i + '.L_arm',set)
                                    
    def L_ArmActive(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'settings':
                                    setType = mc.optionMenu(self.L_armIkFkActiv,query = True, value =True)
                                    if setType =='FK':
                                        set = 0
                                    elif setType =='IK':
                                        set = 1

                                    mc.setAttr(i + '.L_arm_Fk_IK',set)


    '''
    R_arm Functions
    '''                            
    def R_ArmKey(self,*args):
        
        #Used to set key frames on  FK, IK or Both controls on Left Leg
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'R_arm':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                print typeVal
                                keyableType = mc.optionMenu(self.R_armIkFkKey,query = True, value =True)
                                if typeVal == keyableType:
                                    mc.setKeyframe(i)
                                elif keyableType == 'Both':
                                    mc.setKeyframe(i)                
        
    def R_ArmVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.R_armIkFkVis,query = True, value =True)
                                    if visType =='FK':
                                        set = 0
                                    elif visType =='IK':
                                        set = 1
                                    elif visType =='Both':
                                        set = 2
                                    elif visType =='None':
                                        set = 3
                                    mc.setAttr(i + '.R_arm',set)
                                    
    def R_ArmActive(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'settings':
                                    setType = mc.optionMenu(self.R_armIkFkActiv,query = True, value =True)
                                    if setType =='FK':
                                        set = 0
                                    elif setType =='IK':
                                        set = 1

                                    mc.setAttr(i + '.R_arm_Fk_IK',set)


    '''
    L_clav Functions
    '''                            
    def L_ClavKey(self,*args):
        
        #Used to set key frames on Left Clav
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'L_clav':
                            mc.setKeyframe(i)
                
        
    def L_ClavVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.L_clavVis,query = True, value =True)
                                    if visType =='On':
                                        set = 0
                                    elif visType =='Off':
                                        set = 1
                                    mc.setAttr(i + '.L_Clav',set)


    '''
    R_clav Functions
    '''                            
    def R_ClavKey(self,*args):
        
        #Used to set key frames on Left Clav
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'R_clav':
                            mc.setKeyframe(i)
                
    
    def R_ClavVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.R_clavVis,query = True, value =True)
                                    if visType =='On':
                                        set = 0
                                    elif visType =='Off':
                                        set = 1
                                    mc.setAttr(i + '.R_Clav',set)

    '''
    Head And Neck Functions
    '''

    def HeadKey(self,*args):   
        #Used to set key frames on  FK, IK or Both controls on Left Leg
        
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'head':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                print typeVal
                                keyableType = mc.optionMenu(self.headKey,query = True, value =True)
                                if typeVal == keyableType:
                                    mc.setKeyframe(i)
                                elif keyableType == 'Both':
                                    mc.setKeyframe(i)
                                    
    def HeadVis(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'visibility':
                                    visType = mc.optionMenu(self.headVis,query = True, value =True)
                                    if visType =='Head':
                                        set = 0
                                    elif visType =='Head and Neck':
                                        set = 1
                                    elif visType =='None':
                                        set = 2
                                    mc.setAttr(i + '.Head',set)
                                    
    def HeadTrans(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'settings':
                                    setType = mc.optionMenu(self.headTrans,query = True, value =True)
                                    if setType =='World':
                                        set = 0
                                    elif setType =='Chest':
                                        set = 1
                                    elif setType =='Neck':
                                        set = 2

                                    mc.setAttr(i + '.HeadTrans',set)        

    def HeadOri(self, *args):
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            nameQuery= mc.attributeQuery('characterName', node = i,  exists= True)
            if nameQuery == True:
                nameVal = mc.getAttr(i + '.characterName' )
                if nameVal == self.actChar:
                    partQuery =mc.attributeQuery('controlArea', node = i,  exists= True)
                    if partQuery == True:
                        partVal = mc.getAttr(i + '.controlArea' )
                        if partVal == 'master':
                            typeQuery =mc.attributeQuery('controlType', node = i,  exists= True)
                            if typeQuery == True:
                                typeVal = mc.getAttr(i + '.controlType' )
                                if typeVal == 'settings':
                                    setType = mc.optionMenu(self.headOri,query = True, value =True)
                                    if setType =='World':
                                        set = 0
                                    elif setType =='Chest':
                                        set = 1
                                    elif setType =='Neck':
                                        set = 2

                                    mc.setAttr(i + '.HeadOri',set)
go = AnimUI()