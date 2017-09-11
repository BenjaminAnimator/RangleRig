import maya.cmds as mc
from RangleRig.toolkit import assetColourer
from RangleRig.toolkit import connectionCreator
from RangleRig.setUpModules.bodyParts import basicSpine
from RangleRig.setUpModules.bodyParts import plantigradeLeg
from RangleRig.setUpModules.bodyParts import basicArm
from RangleRig.setUpModules.bodyParts import clavicle
from RangleRig.setUpModules.bodyParts import basicHead


class humanSetUp:
    
    def __init__(self, name, *args):
        
        #Generate Setup Joints
        R_Leg = plantigradeLeg.plantigradeLegGen( name, 'Leg1' )
        L_Leg = plantigradeLeg.plantigradeLegGen( name, 'Leg2' )
        Spine = basicSpine.spineGen( name, 'Spine')
        L_Clav = clavicle.clavGen( name, 'Clav1')
        R_Clav = clavicle.clavGen(name, 'Clav2')
        L_Arm = basicArm.basicArmGen( name, 'Arm1')
        R_Arm = basicArm.basicArmGen(name, 'Arm2')
        Neck = basicHead.basicHeadGen(name, 'Neck')
        
        #Move Joints
        mc.xform(R_Leg.legJnts[0], relative = True, worldSpace = True, translation = [-1,0,0])
        mc.xform(L_Leg.legJnts[0], relative = True, worldSpace = True, translation = [1,0,0])
        
        mc.xform(L_Clav.clavJnts[0], relative = True, worldSpace = True, translation = [1,12.703,0] )
        mc.xform(R_Clav.clavJnts[0],relative = True, worldSpace = True, translation = [-1,12.703,0])
        mc.xform(R_Clav.clavJnts[1],relative = True, worldSpace = True, translation = [-2,0,0])
        
        mc.xform(L_Arm.armJnts[0], relative = False, worldSpace = True, translation = [2,12.703,0] )
        mc.xform(R_Arm.armJnts[0], relative = False, worldSpace = True, translation = [-2,12.703,0] )
        mc.xform(R_Arm.armJnts[1], relative = False, worldSpace = True, translation = [-4.735,12.703,-0.187] )
        mc.xform(R_Arm.armJnts[2], relative = False, worldSpace = True, translation = [-6.735,12.703,0] )
        
        mc.xform(Neck.neckJnts[0], relative = False, worldSpace = True, translation = [0.0, 13.391149833078918, -0.4379950587617747] )
        
        
        
        #Create Connections
        connectionCreator.setUpConnection(Spine.spineTopjnt, 'pCube1', 'rig')
        connectionCreator.setUpConnection(L_Leg.legTopjnt, Spine.spineTopjnt, 'constraintParent')
        connectionCreator.setUpConnection(R_Leg.legTopjnt, Spine.spineTopjnt, 'constraintParent')
        connectionCreator.setUpConnection(L_Clav.topClavjnt, Spine.spineJnts[1], 'direct')
        connectionCreator.setUpConnection(R_Clav.topClavjnt, Spine.spineJnts[1], 'direct')
        connectionCreator.setUpConnection(L_Arm.armTopjnt,L_Clav.endClavjnt, 'constraintParent')
        connectionCreator.setUpConnection(R_Arm.armTopjnt,R_Clav.endClavjnt,  'constraintPoint')
        
        connectionCreator.setUpConnection(Neck.neckTopjnt,Spine.spineJnts[1],  'direct')
        
        
        
        
        
        