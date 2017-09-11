"""
Module For creating character hands
"""
import maya.cmds as mc

from RangleRig.toolkit import jntSegmenter
from RangleRig.toolkit import assetColourer
from RangleRig.toolkit import controlGen
from RangleRig.toolkit import attrLocker
from RangleRig.toolkit import objDefine
from RangleRig.toolkit import selectHirearchy

class handGen():
    
    def __init__(self, handJnt, pinkyRoot, ringRoot, midRoot, indexRoot, thumbRoot, characterName):
        
        locX = mc.getAttr(handJnt + ".translateX")

        if locX > 0:
            assetCol = 6
            prefix = "L_"

        
        elif locX < 0:
            assetCol = 13
            prefix = "R_"
        
        #Create list of finger hireachrys
        
        pinkyJnts = selectHirearchy.jntHirearch(pinkyRoot, True)
        ringJnts = selectHirearchy.jntHirearch(ringRoot, True)
        midJnts = selectHirearchy.jntHirearch(midRoot, True)
        indexJnts = selectHirearchy.jntHirearch(indexRoot, True)
        thumbJnts = selectHirearchy.jntHirearch(thumbRoot, True)
        handJnts = selectHirearchy.jntHirearch(handJnt, True)
        

        mc.setAttr(pinkyJnts[3] +'.drawStyle', 2)
        mc.setAttr(ringJnts[3] +'.drawStyle', 2)
        mc.setAttr(midJnts[3] +'.drawStyle', 2)
        mc.setAttr(indexJnts[3] +'.drawStyle', 2)
        mc.setAttr(thumbJnts[3] +'.drawStyle', 2)

        #Pop end joints
        pinkyJnts.pop(-1)
        ringJnts.pop(-1)
        midJnts.pop(-1)
        indexJnts.pop(-1)
        thumbJnts.pop(-1)
        
        handIK = mc.ikHandle( name= prefix+'hand_ik_handle', startJoint=handJnt, endEffector=handJnts[1], solver = "ikRPsolver" )
        mc.parent(handIK[0], handJnt)
        mc.parent(pinkyJnts[0], handJnt)
        mc.parent(ringJnts[0], handJnt)
        mc.parent(midJnts[0], handJnt)
        mc.parent(indexJnts[0], handJnt)
        mc.parent(thumbJnts[0], handJnt)
        self.handGrp =mc.group(handJnt, name = prefix+'Hand Group')
        mc.setAttr(handJnt +'.drawStyle', 2)
        mc.setAttr(handJnts[1] +'.drawStyle', 2)
        
        #Create Finger controls
        pinkyCon = []
        count = 0
        for i in pinkyJnts:
            assetColourer.colourer([i], assetCol)
            controlGen.generateCircle('Pinky Shape', i, True,[1,0,0])
            mc.select(i + '.cv[0:]')
            mc.scale(0.2,0.2,0.2, absolute =True)
            mc.setAttr(i +'.drawStyle', 2)
            rename = mc.rename(i,prefix+ 'pinky%s_anim'%count)
            attrLocker.lockCommon(rename, ['X','Y','Z'], [], ['X','Y','Z'], False, True)
            pinkyCon.append(rename)
            count +=1
        for i in pinkyCon[1:]:
            attrLocker.lockCommon(i, ['X','Y','Z'], [], ['X','Y','Z'], True, True)
        
        ringCon = []
        count = 0
        for i in ringJnts:
            assetColourer.colourer([i], assetCol)
            controlGen.generateCircle('Ring Shape', i, True,[1,0,0])
            mc.select(i + '.cv[0:]')
            mc.scale(0.2,0.2,0.2, absolute =True)
            mc.setAttr(i +'.drawStyle', 2)
            rename = mc.rename(i,prefix+ 'ring%s_anim'%count)
            attrLocker.lockCommon(rename, ['X','Y','Z'], [], ['X','Y','Z'], False, True)
            ringCon.append(rename)
            count +=1
        for i in ringCon[1:]:
            attrLocker.lockCommon(i, ['X','Y','Z'], [], ['X','Y','Z'], True, True)
            
            
        midCon = []
        count = 0                        
        for i in midJnts:
            assetColourer.colourer([i], assetCol)
            controlGen.generateCircle('Mid Shape', i, True,[1,0,0])
            mc.select(i + '.cv[0:]')
            mc.scale(0.2,0.2,0.2, absolute =True)
            mc.setAttr(i +'.drawStyle', 2)
            rename = mc.rename(i,prefix+ 'mid%s_anim'%count)
            attrLocker.lockCommon(rename, ['X','Y','Z'], [], ['X','Y','Z'], False, True)
            midCon.append(rename)
            count +=1
        
        for i in midCon[1:]:
            attrLocker.lockCommon(i, ['X','Y','Z'], [], ['X','Y','Z'], True, True)

        indexCon = []
        count = 0                       
        for i in indexJnts:
            assetColourer.colourer([i], assetCol)
            controlGen.generateCircle('Index Shape', i, True,[1,0,0])
            mc.select(i + '.cv[0:]')
            mc.scale(0.2,0.2,0.2, absolute =True)
            mc.setAttr(i +'.drawStyle', 2)
            rename = mc.rename(i,prefix+ 'index%s_anim'%count)
            attrLocker.lockCommon(rename, ['X','Y','Z'], [], ['X','Y','Z'], False, True)
            indexCon.append(rename)
            count +=1
            
        for i in indexCon[1:]:
            attrLocker.lockCommon(i, ['X','Y','Z'], [], ['X','Y','Z'], True, True)
            
            
        thumbCon = []
        count = 0                        
        for i in thumbJnts:
            assetColourer.colourer([i], assetCol)
            controlGen.generateCircle('Thumb Shape', i, True,[1,0,0])
            mc.select(i + '.cv[0:]')
            mc.scale(0.2,0.2,0.2, absolute =True)
            mc.setAttr(i +'.drawStyle', 2)
            rename = mc.rename(i,prefix+ 'thumb%s_anim'%count)
            attrLocker.lockCommon(rename, ['X','Y','Z'], [], ['X','Y','Z'], False, True)
            thumbCon.append(rename)
            count +=1
        
        for i in thumbCon[1:]:
            attrLocker.lockCommon(i, ['X','Y','Z'], [], ['X','Y','Z'], True, True)
        
        self.TopJnts=[pinkyCon[0], ringCon[0] ,midCon[0], indexCon[0], thumbCon[0]]
            
        objDefine.definer('characterName', pinkyCon , characterName)
        objDefine.definer('controlArea', pinkyCon  , prefix + "hand")
        objDefine.definer('controlType', pinkyCon  , "master")
        

        objDefine.definer('characterName', ringCon , characterName)
        objDefine.definer('controlArea', ringCon , prefix + "hand")
        objDefine.definer('controlType', ringCon , "master")


        objDefine.definer('characterName', midCon , characterName)
        objDefine.definer('controlArea', midCon , prefix + "hand")
        objDefine.definer('controlType', midCon , "master")
    

        objDefine.definer('characterName', indexCon , characterName)
        objDefine.definer('controlArea', indexCon , prefix + "hand")
        objDefine.definer('controlType', indexCon , "master")
                                          
                       
        
       
        
        