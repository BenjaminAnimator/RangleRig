'''
 Clavicle Set Up
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer

class clavGen:
    
    def __init__(self,characterName, uniqueName):
        
        #clavCoOrd = [(0.7715187660205942, 12.620006138429257, -0.31258490820034934),(1.2819456677733205, 12.644605025260717, -0.31258490820034934,)]
        
        clavCoOrd = [(0, 0, 0),(1, 0, 0)]
        
        self.clavJnts = []
        count = 0
        
        for i in clavCoOrd:
            clav = mc.joint( position = i, name = 'setUp_' + uniqueName + str(count)+'_jnt' )
            self.clavJnts.append(clav)
            count += 1
        assetColourer.colourer(self.clavJnts, 6)
        mc.joint(self.clavJnts[0],edit=True, children=True, orientJoint='xyz', secondaryAxisOrient='zup')
        mc.select(clear = True)
        
        self.topClavjnt= self.clavJnts[0]
        self.endClavjnt= self.clavJnts[1]
        
        objDefine.definer('characterName', [self.topClavjnt], characterName)
        objDefine.definer('setUpJnt', [self.topClavjnt], 'Clav')
        objDefine.definer('UniqueID', [self.topClavjnt], str(uniqueName))
        objDefine.definer('UniqueID', [self.endClavjnt], str(uniqueName))
        