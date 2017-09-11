

'''
FK -> IK MAtcher (Arms and Legs)
'''
def FktoIkMatcher(ikJnts, fkJnts): 
    
    ikJntRot = []
    axisRot =[]
    for i in ikJnts:
        axisRot =[]
        RotX = mc.getAttr(i + '.rotateX')
        RotY = mc.getAttr(i + '.rotateY')
        RotZ = mc.getAttr(i + '.rotateZ')
        axisRot.append(RotX)
        axisRot.append(RotY)
        axisRot.append(RotZ)
        ikJntRot.append(axisRot)
    print ikJntRot
    
    NoJnt = 0
    for i in fkJnts[:2]:
        axis = 0
        print ikJntRot[NoJnt][axis]
        mc.setAttr(i + '.rotateX',ikJntRot[NoJnt][axis])
        axis += 1 
        mc.setAttr(i + '.rotateY',ikJntRot[NoJnt][axis])
        axis += 1
        mc.setAttr(i + '.rotateZ',ikJntRot[NoJnt][axis])
        NoJnt +=1

'''
IK -> FK MAtcher (Arms)
''' 
def IktoFkMatcher(FkJnts,ikControls): 
    count =0
    for i in FkJnts[0:]: 
        pos = mc.xform(i, query = True, translation = True, worldSpace =True)
        mc.move(pos[0],pos[1],pos[2],ikControls[count], rotatePivotRelative =True, absolute =True)
        count +=1

