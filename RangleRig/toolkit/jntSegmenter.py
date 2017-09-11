"""
Tool For Segmenting Joints
"""
import maya.cmds as mc

def jointSegment(baseJoint, noSeg, prefix):
    """
    Adds joints between joints
    
    @param baseJoint:String, The base joint of the section you want to segment
    @param noSeg:Float, The number of segements
    @param prefix:String, The prefix for segmented joints
    @return: List of segmented joints
    """
    
    baseJoint = baseJoint
    endJoint = mc.listRelatives(baseJoint, type ='joint' )[0]
    jSegs = noSeg
    jointDist = mc.getAttr(endJoint + '.tx')
    jSegDist =  jointDist / jSegs
    rotOrder = mc.getAttr(baseJoint + '.rotateOrder' )
    jRad = mc.getAttr(baseJoint + '.radius' )
    count = jSegs
    allJsegs = []
    
    for i in range(jSegs):
        newJoint= mc.insertJoint(baseJoint)
        mc.setAttr(newJoint + '.tx', jSegDist)
        mc.setAttr(newJoint + '.rotateOrder', rotOrder)
        mc.setAttr(newJoint + '.radius', jRad)
        name = mc.rename(newJoint, prefix + 'Segment_' + str(count) + '_joint')
        allJsegs.append(name)
        count -= 1
        
        
    
    baseJoint = mc.rename(baseJoint, prefix +'Segment_' + str(count) + '_joint' )
    allJsegs.append(baseJoint)
    mc.delete(endJoint)  
    return allJsegs

   