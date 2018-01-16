# -*- coding: utf-8 -*-
from epics import PV

class CircleControl:
    def __init__(self,user):
        self.x = PV(user+':xPosArr.VAL')
        self.y = PV(user+':yPosArr.VAL')
        self.xc = PV(user+':xCentre.VAL')
        self.yc = PV(user+':yCentre.VAL')
        self.r = PV(user+':radius.VAL')
        self.noise = PV(user+':noise.VAL')
        self.phaseStep = PV(user+':phaseStep.VAL')
        
        self.xcVal = 0
        self.ycVal = 0
        self.rVal = 0
        self.noiseVal = 0
        self.phaseStepVal = 0
        
    def getXYValues(self):
        self.xVals = self.x.value
        self.yVals = self.y.value
        
    def getCircleValues(self):
        xcVal = self.xc.value
        ycVal = self.yc.value
        rVal = self.r.value
        noiseVal = self.noise.value
        phaseStepVal = self.phaseStep.value
        
        if self.xcVal!=xcVal or self.ycVal!=ycVal or self.rVal!=rVal or self.noiseVal!=noiseVal or self.phaseStepVal!=phaseStepVal:
            self.valuesChanged = True
        else:
            self.valuesChanged = False
        
        self.xcVal = xcVal
        self.ycVal = ycVal
        self.rVal = rVal
        self.noiseVal = noiseVal
        self.phaseStepVal = phaseStepVal