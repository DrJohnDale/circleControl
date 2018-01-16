# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer

import mainwindow
from CircleControl import CircleControl
from pygaussmarkov.CircleSolver import CircleSolver


class mainCircleControl(QMainWindow, mainwindow.Ui_mainwindow):
    def __init__(self,parent=None):
        super(mainCircleControl,self).__init__(parent)
        self.setupUi(self)
        self.circ = CircleControl('dale')
        self.circ.getCircleValues()
        self.setValues()
        self.timerUpdate()
        self.xc.textChanged.connect(lambda strIn:self.circ.xc.put(float(strIn)))
        self.yc.textChanged.connect(lambda strIn:self.circ.yc.put(float(strIn)))
        self.rad.textChanged.connect(lambda strIn:self.circ.r.put(float(strIn)))
        self.ps.textChanged.connect(lambda strIn:self.circ.phaseStep.put(float(strIn)))
        self.noise.textChanged.connect(lambda strIn:self.circ.noise.put(float(strIn)))
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerUpdate)
        self.timer.start(500)
        
    def timerUpdate(self):
        self.plotData()
        self.readCircleParameters()
        
    def plotData(self):
        self.circ.getXYValues()
        self.plot.canvas.ax.clear()
        self.plot.canvas.ax.plot(self.circ.xVals,self.circ.yVals,'*k')
        if self.applyFit.isChecked():
            fitter = CircleSolver(np.array(self.circ.xVals),np.array(self.circ.yVals),np.array([self.circ.noiseVal]),np.array([self.circ.noiseVal]),recordHistory=False)
            startParam = fitter.determinStatingVariables()
            out,err = fitter.solve(startParam)
            resString = 'Number of iterations = ' + str(fitter.noInterations) + '\n' +\
            'Solution = ' + str(out)+'\n'+\
            'Uncertainties = ' + str(err)+'\n'+\
            'Final ChiSq = ' +  str(fitter.finalChi_)
            self.fitResults.setText(resString)
            cFit = plt.Circle((out[0],out[1]),out[2],color='r',clip_on=False,fill=False)
            self.plot.canvas.ax.add_artist(cFit)
        else:
            self.fitResults.setText('')
            
        self.plot.canvas.draw()
            
            
    def readCircleParameters(self):
        self.circ.getCircleValues()
        if self.circ.valuesChanged:
            self.setValues()
            
    def setValues(self):
        self.xc.setText(str(self.circ.xcVal))
        self.yc.setText(str(self.circ.ycVal))
        self.rad.setText(str(self.circ.rVal))
        self.noise.setText(str(self.circ.noiseVal))
        self.ps.setText(str(self.circ.phaseStepVal))
        
    def closeEvent(self, event):
        self.timer.stop()
    
def main():
    app = QApplication(sys.argv)
    form = mainCircleControl()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()