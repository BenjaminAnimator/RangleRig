"""
Module for making Neck rigs
"""

import maya.cmds as mc
from RangleRig.toolkit import selectHirearchy
from RangleRig.toolkit import blndColours
from RangleRig.toolkit import controlGen
from RangleRig.toolkit import assetColourer
from RangleRig.toolkit import attrLocker
from RangleRig.toolkit import objDefine
from RangleRig.toolkit import jntSegmenter
from RangleRig.toolkit import createStretchy
from RangleRig.toolkit import setDvrKey
 
class neckGen():
    
    def __init__(self, neckJnt, jointNum ,characterName, rigGrp, settingsGrp, visGrp):
       
        self.setupJnt = neckJnt
        
        builderJnt =  mc.duplicate(neckJnt, name = 'seg_jnt', renameChildren = True )
        
        mc.setAttr(builderJnt[0] + '.setUpJnt', lock= False)
        mc.setAttr(builderJnt[0] + '.UniqueID', lock= False)
        mc.setAttr(builderJnt[0] + '.characterName', lock= False)
        mc.setAttr(builderJnt[0] + '.Connection_type', lock= False)
        mc.setAttr(builderJnt[0] + '.Connect_to', lock= False)
        
        mc.deleteAttr(builderJnt[0] + '.setUpJnt')
        mc.deleteAttr(builderJnt[0] + '.characterName')
        mc.deleteAttr(builderJnt[0] + '.UniqueID')
        mc.deleteAttr(builderJnt[0] + '.Connection_type')
        mc.deleteAttr(builderJnt[0] + '.Connect_to')
        
   
        self.neckBaseJnt = mc.duplicate(builderJnt, parentOnly = True, name = 'neckbase_ik_jnt')
        neckBaseFKJnt = mc.duplicate(builderJnt,  name = 'neckbase_fk_jnt', renameChildren =True)
        neckSegIk= jntSegmenter.jointSegment(builderJnt[0], jointNum, "neck_ik_seg")
        self.neckSegFk= jntSegmenter.jointSegment(neckBaseFKJnt[0], 2, "neck_fk_seg")
        self.neckFkEnd= self.neckSegFk[0]
        

        
        self.headJnt = mc.duplicate(neckSegIk[0], parentOnly = True, name = 'head_jnt')
        mc.parent(self.headJnt, world = True) 
        neckIK = mc.ikHandle(startJoint = neckSegIk[jointNum], endEffector = neckSegIk[0],
                        solver = 'ikSplineSolver', createCurve = True,
                         name  = 'neck_spline_ikhandle', numSpans = 3,
                         simplifyCurve = True)
        neckCurve = mc.rename(neckIK[2], 'neck_ik_curve')
        mc.rename(neckIK[1], 'neck_ik_effector')

       
        #Enable Twisting
        mc.setAttr(neckIK[0] + '.dTwistControlEnable', 1)
        mc.setAttr(neckIK[0] + '.dWorldUpType', 4 )
        mc.connectAttr(self.neckBaseJnt[0] +'.worldMatrix[0]', neckIK[0] + '.dWorldUpMatrix', force = True )
        mc.connectAttr(self.headJnt[0] +'.worldMatrix[0]', neckIK[0] + '.dWorldUpMatrixEnd', force = True )
        mc.setAttr(neckIK[0] + '.dWorldUpVectorY', 0)
        mc.setAttr(neckIK[0] + '.dWorldUpVectorEndY', 0)
        mc.setAttr(neckIK[0] + '.dWorldUpVectorZ', -1)
        mc.setAttr(neckIK[0] + '.dWorldUpVectorEndZ', -1)
        mc.setAttr(neckIK[0] + '.dWorldUpAxis', 4)
        mc.setAttr(neckIK[0] + '.dForwardAxis', 0)
  
        createStretchy.stretchyIK(neckSegIk,neckCurve,'neckIK')
        mc.skinCluster(self.headJnt[0],self.neckBaseJnt[0], neckCurve,
                 bindMethod = 0, maximumInfluences = 5,
                 obeyMaxInfluences = True,
                 dropoffRate = 4.0 )
        
        controlGen.generateCircle('neck_Fk_anim',self.neckSegFk[1], True, [1,0,0])
        self.fkNeckCon = mc.rename(self.neckSegFk[1], 'neck_FK_anim')
        self.headCon =controlGen.generateSquare('head_Ctrl',self.headJnt, False)
        assetColourer.colourer([self.headCon,self.fkNeckCon], 22)        
        mc.parent(self.headJnt, self.headCon)
        neck_loc = mc.xform(self.neckBaseJnt[0], query = True, worldSpace = True, translation = True )
        head_loc = mc.xform(self.headJnt, query = True, worldSpace = True, translation = True )
        
        #Presever Volume
        node_Sqrt = mc.shadingNode('multiplyDivide' ,name = 'neck_sqrt_multDiv', asUtility = True)
        mc.setAttr(node_Sqrt + '.operation', 3)
        mc.setAttr(node_Sqrt + '.input2X', 0)
        mc.connectAttr('neckIK_str_multDiv.outputX', node_Sqrt + '.input1X', force = True)
        
        print rigGrp + 'THIS ONE'
        
        node_worldDiv = mc.shadingNode('multiplyDivide' ,name = 'neck_worlDiv_multDiv', asUtility = True)
        mc.setAttr(node_worldDiv + '.operation', 2)
        mc.connectAttr(node_Sqrt +'.outputX', node_worldDiv + '.input2X', force = True)
        mc.connectAttr(rigGrp +'.globalScale', node_worldDiv + '.input1X', force = True)
        
        for i in neckSegIk:
            mc.connectAttr(node_worldDiv +'.outputX', i + '.scaleY', force = True)
            mc.connectAttr(node_worldDiv +'.outputX', i + '.scaleZ', force = True)
        
        #Flip Stopping
        mc.distanceDimension(endPoint= head_loc , startPoint= neck_loc)
        mc.rename('locator1', 'neckBase_Loc')
        mc.rename('locator2', 'neckEnd_Loc')
        neckDis = mc.rename('distanceDimension1', 'neck_Dist')
        node_M_D = mc.shadingNode('multiplyDivide' ,name = 'neckStr_multDiv', asUtility = True)
        mc.connectAttr(neckDis + '.distance', node_M_D + '.input1X')
        mc.connectAttr(rigGrp + '.scaleY', node_M_D + '.input2X')
        mc.setAttr(node_M_D + '.operation',2)
        mc.parent('neckBase_Loc', self.neckBaseJnt[0])
        mc.parent('neckEnd_Loc', self.headJnt)
        setDvrKey.setDvrK(self.neckBaseJnt[0] + '.scaleX' ,node_M_D +'.outputX',1,1)
        setDvrKey.setDvrK(self.neckBaseJnt[0] + '.scaleY' ,node_M_D +'.outputX',1,1)
        setDvrKey.setDvrK(self.neckBaseJnt[0] + '.scaleZ' ,node_M_D +'.outputX',1,1)
        setDvrKey.setDvrK(self.headJnt[0] + '.scaleX' ,node_M_D +'.outputX',1,1)
        setDvrKey.setDvrK(self.headJnt[0] + '.scaleY' ,node_M_D +'.outputX',1,1)
        setDvrKey.setDvrK(self.headJnt[0] + '.scaleZ' ,node_M_D +'.outputX',1,1)
        mc.setAttr(self.headCon +'.translateY', -0.933)
        setDvrKey.setDvrK(self.neckBaseJnt[0] + '.scaleX' ,node_M_D +'.outputX',1,0.01)
        setDvrKey.setDvrK(self.neckBaseJnt[0] + '.scaleY' ,node_M_D +'.outputX',1,0.01)
        setDvrKey.setDvrK(self.neckBaseJnt[0] + '.scaleZ' ,node_M_D +'.outputX',1,0.01)
        setDvrKey.setDvrK(self.headJnt[0] + '.scaleX' ,node_M_D +'.outputX',1,0.01)
        setDvrKey.setDvrK(self.headJnt[0] + '.scaleY' ,node_M_D +'.outputX',1,0.01)
        setDvrKey.setDvrK(self.headJnt[0] + '.scaleZ' ,node_M_D +'.outputX',1,0.01)
        mc.setAttr(self.headCon +'.translateY', 0)
        
        #Grouping
        self.headGrp = mc.group(self.headCon, name = 'head_anim_grp')
        self.nckGrp = mc.group(empty =True, name = 'Neck_grp')
        mc.group(empty =True, name = 'Neck_DNT_grp')
        mc.parent('Neck_DNT_grp', self.nckGrp)
        mc.parent(self.neckSegFk[-1], self.nckGrp)
        mc.parent(neckCurve, 'Neck_DNT_grp')
        mc.parent(neckDis, 'Neck_DNT_grp')
        mc.parent(neckIK[0], 'Neck_DNT_grp')
        mc.parent(neckSegIk[-1], 'Neck_DNT_grp')
        mc.setAttr( "Neck_DNT_grp.inheritsTransform", 0)
        
        #CleanUP
        self.neckSegFk.pop(1)
        
        #SetVis(Non Joint)
        mc.setAttr("Neck_DNT_grp.visibility", 1)
        mc.setAttr(neckCurve + ".visibility", 0)
        mc.setAttr(neckDis + ".visibility", 0)
        mc.setAttr(neckIK[0] + ".visibility", 0)
        mc.setAttr(self.neckBaseJnt[0] + ".visibility", 0)
        mc.setAttr('neckBase_Loc' + ".visibility", 0)
        mc.setAttr('neckEnd_Loc' + ".visibility", 0)
        
        #Set Vis (Joints)
        for i  in neckSegIk :
            mc.setAttr(i +'.drawStyle', 2)
        mc.setAttr(self.headJnt[0] +'.drawStyle', 2)
        mc.setAttr(self.neckFkEnd +'.drawStyle', 2)
        mc.setAttr(self.neckSegFk[0] +'.drawStyle', 2)
        mc.setAttr(self.neckSegFk[-1] +'.drawStyle', 2)
        mc.setAttr(self.fkNeckCon +'.drawStyle', 2)
        
        #Lock Attr
        attrLocker.lockCommon('Neck_DNT_grp', ['X','Y','Z'], ['X','Y','Z'],['X','Y','Z'], True, True)
        attrLocker.lockCommon(self.nckGrp, ['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        attrLocker.lockCommon(self.headCon, [], [], ['X','Y','Z'], False, True)
        attrLocker.lockCommon(self.fkNeckCon, ['X','Y', 'Z'], [], ['X','Y','Z'], False, True)
        attrLocker.lockCommon(self.headJnt[0], ['X','Y','Z'],['X','Y','Z'], ['X','Y','Z'], True, True)
        attrLocker.lockCommon(neckCurve, ['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        attrLocker.lockCommon(neckDis, ['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        attrLocker.lockCommon(neckIK[0], ['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        attrLocker.lockCommon('neckEnd_Loc', ['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        attrLocker.lockCommon('neckBase_Loc', ['X','Y','Z'], ['X','Y','Z'], ['X','Y','Z'], True, True)
        
        #Define Controls
        objDefine.definer('characterName', [self.headCon], characterName)
        objDefine.definer('controlArea', [self.headCon], 'head')
        objDefine.definer('controlType', [self.headCon], "head")
        
        objDefine.definer('characterName', [self.fkNeckCon], characterName)
        objDefine.definer('controlArea', [self.fkNeckCon], 'head')
        objDefine.definer('controlType', [self.fkNeckCon], "neck")
        
        objDefine.definer("Connection", [self.nckGrp], "rig")
        objDefine.definer("Connection", [self.neckBaseJnt[0]], "root")



       