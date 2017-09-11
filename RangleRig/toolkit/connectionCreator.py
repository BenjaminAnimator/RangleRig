"""
Module for establishing connections between set up body parts 
"""
import maya.cmds as mc
from RangleRig.toolkit import objDefine

def setUpConnection(slave, masters, type ):
    
    """
    Add Attributes
    @param master: list, the parent object(s) 
    @param slave: string,the child object
    @param type:string, the type of connection "direct" or 'constraint' or 'rig' 
    """
    if type == 'rig':
        masters = 'rig'
    else:
        print 'none'
    conecteeLst = [slave]
    
    objDefine.definer( 'Connect_to' ,conecteeLst, masters)
    objDefine.definer('Connection_type',conecteeLst, type)
  
def connector(instanceDict,instancekey, animGrp):
    
    for key in instancekey:
        slaveSetupJnt = instanceDict[key].setupJnt
        queryConnectTo = mc.attributeQuery('Connect_to', node = slaveSetupJnt,  exists= True)
        if queryConnectTo == False:
            mc.error('No Connections Detected: Please add connections')
        else:
            connectTo = mc.getAttr(slaveSetupJnt+ ('.Connect_to'))
            queryConnectionType = mc.attributeQuery('Connection_type', node = slaveSetupJnt,  exists= True)
            if queryConnectionType == False:
                mc.error()
            else:
                connectionType = mc.getAttr(slaveSetupJnt+ ('.Connection_type'))
                

                #Connection Type: Rig
                if connectionType == 'rig':
                    print 'rig'
                    slaveInstDic =  instanceDict[key].__dict__
                    print slaveInstDic
                    
                    for i in slaveInstDic:
                        node = slaveInstDic[i]

                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    conType = mc.getAttr(x +'.Connection')
                                    if conType == 'root':
                                        mc.parent(x,animGrp)
                                else:
                                    print 'Dic error'
                    
                    #Find Root Node
                        else:
                            print node
                                                  
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                conType = mc.getAttr(node +'.Connection')
                                if conType == 'root':
                                    print node + 'passed' 
                                    mc.parent(node,animGrp)
                                else:
                                    print 'unknown'
                    
                
                
                
                #Connection Type: Direct
                elif connectionType == 'direct':
                    print 'Direct'


                    masterConnect = mc.getAttr(slaveSetupJnt + '.Connect_to')
                    masterID = mc.getAttr(masterConnect + '.UniqueID')
                    masterInst = instanceDict[masterID] 
                

                
               
                
                    slaveInstDic =  instanceDict[key].__dict__
                    masterInstDic =  masterInst.__dict__
                
                    #Find Root Node
                    for i in slaveInstDic:
                        node = slaveInstDic[i]
                        

                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    conType = mc.getAttr(x +'.Connection')
                                    if conType == 'root':
                                        RootNode = x
                                        
                                else:
                                    print 'Dic error'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                conType = mc.getAttr(node +'.Connection')
                                if conType == 'root':
                                     RootNode = node

                                else:
                                    print 'unknown'
                        
                        
                        
                     
                    #Find Connection Nodes
                    conNodes = []
                    for i in masterInstDic:
                        node = masterInstDic[i]
                       

                        
                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    ConNode = x
                                    conNodes.append(ConNode)
                                else:
                                    print 'DEBUG:No Connection Node'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                ConNode = node
                                conNodes.append(ConNode)
                            else:
                                print 'DEBUG:No Connection Node'
                                    
                        print conNodes            

                        for i in conNodes:
                            conType = mc.getAttr(i +'.Connection') 
                            if conType == connectTo:
                                parentCheck = mc.listRelatives(RootNode, allParents = True)
                                print "PARENT CHECK : %s" %(parentCheck)
                                                                
                                if parentCheck == None:                                    
                                    print 'connecting to %s' %(i)
                                    mc.parent(RootNode,i)
                                    
                                elif parentCheck[0] == i:
                                    print 'Already connected'
                            else:
                                print 'DEBUG:Not right Connection Node'
          
                                
                
                
                

                #Connection Type: constraintParent
                elif connectionType == 'constraintParent':
                    print 'other'


                    masterConnect = mc.getAttr(slaveSetupJnt + '.Connect_to')
                    masterID = mc.getAttr(masterConnect + '.UniqueID')
                    masterInst = instanceDict[masterID] 
                

                
               
                
                    slaveInstDic =  instanceDict[key].__dict__
                    masterInstDic =  masterInst.__dict__
                
                    #Find Root Node
                    for i in slaveInstDic:
                        node = slaveInstDic[i]
                        

                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    conType = mc.getAttr(x +'.Connection')
                                    if conType == 'root':
                                        RootNode = x
                                        
                                else:
                                    print 'Dic error'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                conType = mc.getAttr(node +'.Connection')
                                if conType == 'root':
                                     RootNode = node

                                else:
                                    print 'unknown'
                        
                        
                        
                     
                    #Find Connection Nodes
                    conNodes = []
                    for i in masterInstDic:
                        node = masterInstDic[i]
                       

                        
                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    ConNode = x
                                    conNodes.append(ConNode)
                                else:
                                    print 'DEBUG:No Connection Node'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                ConNode = node
                                conNodes.append(ConNode)
                            else:
                                print 'DEBUG:No Connection Node'
                                    
                        print conNodes            

                        for i in conNodes:
                            conType = mc.getAttr(i +'.Connection') 
                            if conType == connectTo:
                                print 'connecting to %s' %(i)
                                mc.parentConstraint(i,RootNode, maintainOffset = True)
                               
                            else:
                                print 'DEBUG:Not right Connection Node'
                             
                    mc.parent(RootNode, animGrp)

                #Connection Type: constraintPoint
                elif connectionType == 'constraintPoint':
                    print 'other'


                    masterConnect = mc.getAttr(slaveSetupJnt + '.Connect_to')
                    masterID = mc.getAttr(masterConnect + '.UniqueID')
                    masterInst = instanceDict[masterID] 
                

                
               
                
                    slaveInstDic =  instanceDict[key].__dict__
                    masterInstDic =  masterInst.__dict__
                
                    #Find Root Node
                    for i in slaveInstDic:
                        node = slaveInstDic[i]
                        

                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    conType = mc.getAttr(x +'.Connection')
                                    if conType == 'root':
                                        RootNode = x
                                        
                                else:
                                    print 'Dic error'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                conType = mc.getAttr(node +'.Connection')
                                if conType == 'root':
                                     RootNode = node

                                else:
                                    print 'unknown'
                        
                        
                        
                     
                    #Find Connection Nodes
                    conNodes = []
                    for i in masterInstDic:
                        node = masterInstDic[i]
                       

                        
                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    ConNode = x
                                    conNodes.append(ConNode)
                                else:
                                    print 'DEBUG:No Connection Node'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                ConNode = node
                                conNodes.append(ConNode)
                            else:
                                print 'DEBUG:No Connection Node'
                                    
                        print conNodes            

                        for i in conNodes:
                            conType = mc.getAttr(i +'.Connection') 
                            if conType == connectTo:
                                print 'connecting to %s' %(i)
                                mc.pointConstraint(i,RootNode, maintainOffset = True)
                               
                            else:
                                print 'DEBUG:Not right Connection Node'
                             
                    mc.parent(RootNode, animGrp)
                    
                    
                #Connection Type: constraintParent
                elif connectionType == 'constraintOrient':
                    print 'other'


                    masterConnect = mc.getAttr(slaveSetupJnt + '.Connect_to')
                    masterID = mc.getAttr(masterConnect + '.UniqueID')
                    masterInst = instanceDict[masterID] 
                

                
               
                
                    slaveInstDic =  instanceDict[key].__dict__
                    masterInstDic =  masterInst.__dict__
                
                    #Find Root Node
                    for i in slaveInstDic:
                        node = slaveInstDic[i]
                        

                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    conType = mc.getAttr(x +'.Connection')
                                    if conType == 'root':
                                        RootNode = x
                                        
                                else:
                                    print 'Dic error'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                conType = mc.getAttr(node +'.Connection')
                                if conType == 'root':
                                     RootNode = node

                                else:
                                    print 'unknown'
                        
                        
                        
                     
                    #Find Connection Nodes
                    conNodes = []
                    for i in masterInstDic:
                        node = masterInstDic[i]
                       

                        
                        if isinstance(node, list) == True:
                            for x in node:
                                conQuery = mc.attributeQuery('Connection', node = x, exists = True)
                                if conQuery == True:
                                    ConNode = x
                                    conNodes.append(ConNode)
                                else:
                                    print 'DEBUG:No Connection Node'
                    

                        else:
                                                                            
                            conQuery = mc.attributeQuery('Connection', node = node, exists = True)
                            if conQuery == True:
                                ConNode = node
                                conNodes.append(ConNode)
                            else:
                                print 'DEBUG:No Connection Node'
                                    
                        print conNodes            

                        for i in conNodes:
                            conType = mc.getAttr(i +'.Connection') 
                            if conType == connectTo:
                                print 'connecting to %s' %(i)
                                mc.orientConstraint(i,RootNode, maintainOffset = True)
                               
                            else:
                                print 'DEBUG:Not right Connection Node'
                             
                    mc.parent(RootNode, animGrp)                    

def connectorCleaner(instanceDict,instancekey, animGrp):
    print 'Connection CLEANER'
    for key in instancekey:
        
        InstDic =  instanceDict[key].__dict__
        print InstDic
        

        for i in InstDic:
            node = InstDic[i]
            print node
 
            
            if isinstance(node, list) == True:
                print ' is list'
                for x in node:
                    attrQuery = mc.attributeQuery('Connection', node = x, exists = True)
                    if attrQuery == True:
                        valQuery = mc.getAttr(x +'.Connection')
                        if valQuery == 'rig':
                            mc.parent(x, animGrp)
                        else:
                            print 'DEBUG: Not Rig value'
                    else:
                        print 'DEBUG: No Connection Attribute'
            
            else:
                print 'not list'
                attrQuery = mc.attributeQuery('Connection', node = node, exists = True)
                if attrQuery == True:
                    valQuery = mc.getAttr(node +'.Connection')
                    if valQuery == 'rig':
                        mc.parent(node, animGrp)
                    else:
                        print 'DEBUG: Not Rig value'
                else:
                    print 'DEBUG: No Connection Attribute'
                         



            