'''
head Set Up
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer

class basicHeadGen:
    
    def __init__(self,characterName, uniqueName):
        
        neckCoOrd =[(0.0, 0, 0),(0, 1,0)]
        
        
        self.neckJnts = []
        parts = ['base', 'end']
        count= 0
        
        for i in neckCoOrd:
            neck = mc.joint( position = i, name = 'setUp_' + uniqueName + str(count)+'_jnt' )
            self.neckJnts.append(neck)
            count += 1

        assetColourer.colourer(self.neckJnts, 6)
        mc.joint(self.neckJnts[0],edit=True, children=True, orientJoint='xyz', secondaryAxisOrient='zup')
        mc.select(clear = True)
        
        self.neckTopjnt= self.neckJnts[0]
        self.headJnt = self.neckJnts[1]
        
        objDefine.definer('characterName', [self.neckTopjnt], characterName)
        objDefine.definer('setUpJnt', [self.neckTopjnt], 'Neck')
        objDefine.definer('UniqueID', [self.neckTopjnt], str(uniqueName))
        
        objDefine.definer('characterName', [self.headJnt], characterName)
