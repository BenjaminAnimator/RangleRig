'''
UIClasses
'''
from RangleRig import assemble
from RangleRig.setUpModules import symHumanSetUp

class buildSetup():   
    def __init__(self,text):
         name = text
         setUp = symHumanSetUp.humanSetUp(name)
         self.Topjnts = setUp.assembleRequirement
         

class createRig():
    def __init__(self):
        assemble.builder(name)