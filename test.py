# -*- coding: utf-8 -*-
from CircleControl import CircleControl
import matplotlib.pyplot as plt

cirCon = CircleControl('dale')

cirCon.getCircleValues()
cirCon.getXYValues()

print(cirCon.xVals,cirCon.yVals)
plt.plot(cirCon.xVals,cirCon.yVals,'*k')
