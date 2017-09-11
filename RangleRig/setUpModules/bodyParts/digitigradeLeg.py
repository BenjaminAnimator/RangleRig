'''
digitigrade Leg Set Up - 'Dog/Cat Leg'
'''
import maya.cmds as mc

from RangleRig.toolkit import objDefine
from RangleRig.toolkit import assetColourer


class digitigradeLegGen:
    
    def __init__(self,characterName):
        
        legCoOrd = [(0, 6.3549179646938505, 0.0),
                    (0, 4.04919589915265, 0.7593162562699296),
                    (0, 1.6234758919952759, 0.25931625626992916),
                    (0, 0.14582711230190204, 0.36513830806033865),
                    (0, 0.0, 1.4228935312019737)]
        
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
        

        
    





        
        
        

        

