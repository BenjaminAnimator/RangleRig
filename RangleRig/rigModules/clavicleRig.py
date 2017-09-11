"Module for creating Clavical Rig"

import maya.cmds as mc
from RangleRig.toolkit import controlGen
from RangleRig.toolkit import assetColourer
from RangleRig.toolkit import attrLocker
from RangleRig.toolkit import objDefine
from RangleRig.toolkit import setDvrKey
from RangleRig.toolkit import selectHirearchy

class clavGen():
    
    def __init__(self, basejoint,characterName,rigGrp,visGrp):
        
        self.setupJnt = basejoint
        baseJntslst = selectHirearchy.jntHirearch(basejoint,False)
        endSetup = baseJntslst[0]
        
        ID  = mc.getAttr(basejoint +'.UniqueID')
        
        rigJnts =  mc.duplicate(basejoint,  name = ID+'_01_Jnt', renameChildren = True)
        jnt1 = mc.rename(rigJnts[0], ID + '_01_Jnt')
        jnt2 = mc.rename(rigJnts[1], ID + '_02_Jnt')
        
        #Clavicle Set Up
        locX = mc.getAttr(jnt1  + ".translateX")

        if locX > 0:
            assetCol = 6
            prefix = "L_"
            
        elif locX < 0:
            prefix = "R_"
            assetCol = 13
            
        else:
            assetCol = 22
            prefix = "M_"
        
        mc.setAttr(jnt1 + '.setUpJnt', lock= False)
        mc.setAttr(jnt1 + '.UniqueID', lock= False)
        mc.setAttr(jnt1 + '.Connect_to', lock= False)
        mc.setAttr(jnt1 + '.Connection_type', lock= False)
        mc.setAttr(jnt1 + '.characterName', lock= False)
        mc.deleteAttr(jnt1 + '.setUpJnt')
        mc.deleteAttr(jnt1 + '.characterName')
        mc.deleteAttr(jnt1 + '.UniqueID')
        mc.deleteAttr(jnt1 + '.Connect_to')
        mc.deleteAttr(jnt1 + '.Connection_type')
            
        clavJnts = mc.listRelatives(jnt1)
        baseJnt =  mc.rename(jnt1 , prefix +'clavBase_jnt')      
        self.childJnt = mc.rename(clavJnts[0], prefix +'clavBase_end')
        
        
        
        #Create Clavicle Ik
        clavIk = mc.ikHandle(startJoint = baseJnt, 
                    endEffector = self.childJnt,
                    name  = prefix +'clavicle_ikhandle')
        
        
        

        
        
        '''
        #ADVANCE CLAVS (WIP)
        
        mc.distanceDimension( startPoint =[-1,0,0] ,  endPoint =  [1,0,0])

        baseLoc = 'locator1'
        childLoc = 'locator2'
        
        baseLoc = mc.rename(baseLoc, '%sbaseClav_loc' %prefix)
        childLoc = mc.rename(childLoc, '%sendClav_loc' %prefix)
        
        mc.parent(baseLoc, baseJnt)
        mc.parent(childLoc, clavIk[0])
        
        mc.move(0,0,0, baseLoc, objectSpace = True)
        mc.move(0,0,0, childLoc, objectSpace = True)
        
        mc.rename('distanceDimension1', prefix +'clavDist_util')
        clavDist = prefix + "clavDist_utilShape"
        '''

        
        #Create Clavicle Controls
        self.clavCtrl= controlGen.generateSquare(prefix + "clavicle_anim", clavIk[0] ,False)
        assetColourer.colourer([self.clavCtrl], assetCol)
        

        
        #Constrain Ik handle to controler
        mc.parent(clavIk[0],self.clavCtrl) 
        
        #Grouping
        self.clavGrp = mc.group(empty = True, name = prefix + "Clav_grp")
        dntGroup= mc.group(empty = True, name = prefix + "DONOTTOUCH_Clav_grp")
        mc.parent(dntGroup, self.clavGrp)
        mc.parent(baseJnt,dntGroup)
        mc.parent(self.clavCtrl, self.clavGrp)
        
        
        #Clean Up (Non Joint)
        attrLocker.lockCommon(dntGroup,['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        mc.setAttr(clavIk[0] + '.visibility', 0)
        attrLocker.lockCommon(self.clavCtrl,[], [], ['X','Y','Z'], False, True)
        
        #Clean Up (Joints)
        mc.setAttr(self.childJnt +'.drawStyle', 2)
        mc.setAttr(baseJnt +'.drawStyle', 2)
        
        #Clav Vis
        mc.select(visGrp)
        mc.addAttr( shortName=ID + '_ClavVis', longName=ID + '_ClavVis', attributeType = 'enum', enumName = 'On:Off' , keyable = True, hidden = False )
        
        for i in [self.clavCtrl]:
            setDvrKey.setDvrK(visGrp +  '.' + ID + '_ClavVis', i + '.visibility', 0, 1)
            setDvrKey.setDvrK(visGrp +  '.' + ID + '_ClavVis', i + '.visibility', 1, 0)

            attrLocker.lockCommon(i,[],[],[],True,True)
        
        
        
        #Define Controls
        objDefine.definer('characterName', [self.clavCtrl], characterName)
        objDefine.definer('controlArea', [self.clavCtrl], prefix + "clav")
        objDefine.definer("Connection", [self.clavGrp], "root")
        objDefine.definer("Connection", [self.clavCtrl], endSetup )
        
        
        
        
        
        

        
               

    