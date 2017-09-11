'''
Basic Arm Set Up
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer


class basicArmGen:
    
    def __init__(self,characterName, uniqueName):
        
        armCoOrd = [(1.2819456677733205, 12.644605025260717, -0.31258490820034934),
                               (4.01733866073109, 12.644605025260713, -0.5),
                               (6.01733866073109, 12.644605025260713, -0.31258490820034934)]
        
        self.armJnts = []
        count= 0
        
        for i in armCoOrd:
            arm = mc.joint( position = i, name = 'setUp_' + uniqueName + str(count)+'_jnt' )
            self.armJnts.append(arm)
            count += 1
        assetColourer.colourer(self.armJnts, 6)
        mc.joint(self.armJnts[0],edit=True, children=True, orientJoint='xyz', secondaryAxisOrient='zup')
        mc.select(clear = True)
        
        self.armTopjnt= self.armJnts[0]
        
        objDefine.definer('characterName', [self.armTopjnt], characterName)
        objDefine.definer('setUpJnt', [self.armTopjnt], 'Arm')
        objDefine.definer('UniqueID', [self.armTopjnt], str(uniqueName))
        

        
    





        
        
        

        

