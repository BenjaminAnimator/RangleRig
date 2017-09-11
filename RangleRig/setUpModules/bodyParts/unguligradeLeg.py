'''
unguligrade Leg Set Up - 'Horse/Deer Leg'
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer


class unguligradeLegGen:
    
    def __init__(self,characterName):
        
        legCoOrd = [(0, 5.538720420251183, 0.0),
                    (0, 3.58990392546668, 0.757100818063537),
                    (0, 1.8016928910288283, 0.25710081806353646),
                    (0, 0.6464675994213542, 0.5953310844051976),
                    (0, 0.0, 0.9149597004695516)]
        
        self.legJnts = []
        
        for i in legCoOrd:
            leg = mc.joint( position = i)
            self.legJnts.append(leg)
        assetColourer.colourer(self.legJnts, 6)
        mc.joint(self.legJnts[0],edit=True, children=True, orientJoint='xyz', secondaryAxisOrient='zup')
        mc.select(clear = True)
        
        self.legTopjnt= self.legJnts[0]
        
        objDefine.definer('characterName', [self.legTopjnt], characterName)
        objDefine.definer('setUpJnt', [self.legTopjnt], 'Leg')
        

        
    





        
        
        

        

