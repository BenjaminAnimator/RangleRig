'''
        --Assembler Module--

 - Detects Setup Body Parts
 - Rigs body Parts
 - Connects Body Parts
 
'''

import maya.cmds as mc

from RangleRig.rigModules import base
from RangleRig.rigModules import spineRig
from RangleRig.rigModules import legRig
from RangleRig.rigModules import clavicleRig
from RangleRig.rigModules import armRig
from RangleRig.rigModules import neckRig
from RangleRig.toolkit import connectionCreator


class assembleRig():

    def __init__(self, name):
       
        #Finds SetUp Joints
        setupList = []
        sel = mc.ls()
        for i in sel:
            mc.select(i)
            query = mc.attributeQuery('setUpJnt', node = i,  exists= True)
            if query == True:
                setupList.append(i)
        print setupList    
        
        #Create Rig Base Group
        rigBase = base.baseGen(name)
        rigGrp = rigBase.rigGrp
        settingGrp = rigBase.settingGrp
        visGrp = rigBase.visibilityGrp
        animGrp = rigBase.animGrp
    
        
        #Begins Rigging Body Parts
        bodyPartRigInstList = {}
        bodyPartRigInstKeys = []
        
        #Find and Rig Spines
        spineList =[]
        spineID = []
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Spine':
                ID  = mc.getAttr(i +'.UniqueID')
                spineList.append(i)  
                spineID.append(ID)  
                
            else:
                print 'NO SPINE'
        
        
        spineCount = len(spineList)
        
        if spineCount == 0:
            print 'NO SPINE'
        
        else:
            spineRigs = {}
            spineKeys = []
            count = 0
            for i in spineID:
                print 'Rigging %s this is spine %s of %s' %(i,count, spineCount -1)                     
                bodyPartRigInstList[i] = spineRig.spineGen(spineList[count],4,3, name, rigGrp, visGrp)
                bodyPartRigInstKeys.append(i)
                count =+ 1
                        
                
                  



            
        #Find and Rig Legs

        legList = []
        legID = []  
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Leg':
                ID  = mc.getAttr(i +'.UniqueID')
                legList.append(i)  
                legID.append(ID) 
                
            else:
                print 'NO LEGS'
       
        legCount = len(legList)
        
        if legCount == 0:
            print 'NO Leg'
        
        else:
            legRigs = {}
            legKeys = []

            count = 0
            for i in legID:
                print 'Rigging %s this is leg %s of %s' %(i,count, legCount -1)                     
                bodyPartRigInstList[i] = legRig.legGen(legList[count],name,rigGrp,settingGrp,visGrp)
                bodyPartRigInstKeys.append(i)
                count =+ 1
              

      
                

            
        
        #Find and Rig Clavicles
        clavList = []
        clavID = []  
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Clav':
                ID  = mc.getAttr(i +'.UniqueID')
                clavList.append(i)  
                clavID.append(ID) 
                
            else:
                print 'NO LEGS'
       
        clavCount = len(clavList)
        
        if clavCount == 0:
            print 'NO Clav'
        
        else:
            clavRigs = {}
            clavKeys = []

            count = 0
            for i in clavID:
                print 'Rigging %s this is clav %s of %s' %(i,count, clavCount -1)                     
                bodyPartRigInstList[i] = clavicleRig.clavGen(clavList[count],name,rigGrp,visGrp)
                bodyPartRigInstKeys.append(i)
                count =+ 1

              
        
        
        
        
        #Find and Rig Arms
        armList = []
        armID = []  
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Arm':
                ID  = mc.getAttr(i +'.UniqueID')
                armList.append(i)  
                armID.append(ID) 
                
            else:
                print 'NO ARMS'
       
        armCount = len(armList)
        
        if armCount == 0:
            print 'NO ARMS'
        
        else:
            armRigs = {}
            armKeys = []

            count = 0
            for i in armID:
                print 'Rigging %s this is clav %s of %s' %(i,count, armCount -1)                     
                bodyPartRigInstList[i] = armRig.armGen(armList[count],name,rigGrp, settingGrp ,visGrp)
                bodyPartRigInstKeys.append(i)
                count =+ 1
                
                
        
                #Find and Rig Arms
        neckList = []
        neckID = []  
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Neck':
                ID  = mc.getAttr(i +'.UniqueID')
                neckList.append(i)  
                neckID.append(ID) 
                
            else:
                print 'NO ARMS'
       
        neckCount = len(neckList)
        
        if armCount == 0:
            print 'NO NECKS'
        
        else:
            neckRigs = {}
            neckKeys = []

            count = 0
            for i in neckID:
                print 'Rigging %s this is neck %s of %s' %(i,count, armCount -1)                     
                bodyPartRigInstList[i] = neckRig.neckGen(neckList[count], 3,name ,rigGrp, settingGrp ,visGrp)
                bodyPartRigInstKeys.append(i)
                count =+ 1
        '''
        ArmCount = 0  
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Arm':
                armRig.armGen(i , name, rigGrp, settingGrp, visGrp)
                ArmCount += 1
                
            else:
                print 'NO ARMS'
                
        #Find and Rig Heads
        NeckCount = 0  
        for i in setupList:
            mc.select(i)
            query = mc.getAttr(i + '.setUpJnt')
            if query == 'Neck':
                neckRig.neckGen(i , 3 ,name, rigGrp, settingGrp, visGrp)
                NeckCount += 1
                
            else:
                print 'NO NECKS'


'''
        #Run Connector
        
        print bodyPartRigInstList
           
        connectionCreator.connector(bodyPartRigInstList,bodyPartRigInstKeys,animGrp)
        connectionCreator.connectorCleaner(bodyPartRigInstList,bodyPartRigInstKeys,animGrp)
        
        #Clean Up
        setUpGrp = mc.group(name = "SetUp Group", empty = True)
        mc.setAttr(setUpGrp + '.visibility', 0)
       
        for i in setupList:
            mc.parent(i, setUpGrp)


        