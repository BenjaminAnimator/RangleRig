'''
Plantigrade Leg Set Up - 'Human Leg'
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer


class plantigradeLegGen:
    
    def __init__(self,characterName, uniqueName):
        
        legCoOrd = [(0,8,0),
                    (0, 4.04169, 0.5),
                    (0, 0.8552566497927181, 0.0),
                    (0, 0, 1.0000000000000007),
                    (0, 0, 2.0000000000000018) ]
        
        self.legJnts = []
        count = 0
        for i in legCoOrd:
            leg = mc.joint( position = i, name = 'setUp_' + uniqueName + str(count)+'_jnt' )
            self.legJnts.append(leg)
            count += 1
        assetColourer.colourer(self.legJnts, 6)
        mc.joint(self.legJnts[0],edit=True, children=True, orientJoint='xyz', secondaryAxisOrient='zup')
        mc.select(clear = True)
        
        self.legTopjnt= self.legJnts[0]
        
        objDefine.definer('characterName', [self.legTopjnt], characterName)
        objDefine.definer('setUpJnt', [self.legTopjnt], 'Leg')
        objDefine.definer('UniqueID', [self.legTopjnt], str(uniqueName))
        
        

        
    





        
        
        

        

