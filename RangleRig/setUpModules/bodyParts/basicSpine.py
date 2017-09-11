'''
Spine Set Up
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer

class spineGen:
    
    def __init__(self,characterName, uniqueName):
        
        spineCoOrd = spineCoOrd = [(0,8.158,0), (0, 12.703323684583381,0)]
        
        self.spineJnts = []
        parts = ['base', 'end']
        count= 0
        
        for i in spineCoOrd:
            spine = mc.joint( position = i, name = 'setUp_' + uniqueName + str(count)+'_jnt' )
            self.spineJnts.append(spine)
            count += 1

        assetColourer.colourer(self.spineJnts, 6)
        mc.joint(self.spineJnts[0],edit=True, children=True, orientJoint='xyz', secondaryAxisOrient='zup')
        mc.select(clear = True)
        
        self.spineTopjnt= self.spineJnts[0]
        
        objDefine.definer('characterName', [self.spineTopjnt], characterName)
        objDefine.definer('setUpJnt', [self.spineTopjnt], 'Spine')
        objDefine.definer('UniqueID', [self.spineTopjnt], str(uniqueName))
        

        objDefine.definer('UniqueID', [self.spineJnts[1]], str(uniqueName))
