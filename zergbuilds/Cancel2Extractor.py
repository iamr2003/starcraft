from RBUT import *
from zerg import *
import time,sys

oldStdout = sys.stdout
sys.stdout = open("Cancel2Extractor.log", "w")

T = 0.
m = []
t = []
simulator = zerg(0.5)
PriorityQueue = []
#def condition1():
   #return  simulator.population - simulator.PopOcupied >= Drone.PopReq
def condition2():
   return  simulator.mineral > 105.
Cancel2Extractor = Combo([ (1, NumberItem(Extractor, simulator, 2)), (2, NumberItem(Drone, simulator, 2)), (3,CancelItem(Extractor, simulator)),(4,CancelItem(Extractor, simulator)) ])
#PriorityQueue.append((1,ConditionItem(Drone, simulator, condition1)))
PriorityQueue.append((1,NumberItem(Drone, simulator, 4)))
PriorityQueue.append((2,ConditionItem(Cancel2Extractor, simulator, condition2)))
PriorityQueue.append((6,NumberItem(Overlord, simulator, 1)))
PriorityQueue.append((7,NumberItem(Spawning_Pool,simulator, 1)))
PriorityQueue.append((8,NumberItem(Drone, simulator, 5)))
PriorityQueue.append((9,NumberItem(Queen, simulator, 1)))
PriorityQueue.append((10,NumberItem(Overlord, simulator, 1)))
PQ = pipeline(PriorityQueue)

def run(simulator, m, t):
    m.append(simulator.mineral) 
    t.append(simulator.time)
    PQ.make()
    m.append(simulator.mineral) 
    t.append(simulator.time)
    m.append(simulator.mineral) 
    t.append(simulator.queue[0][0])

Hatchery.run()
simulator.Mining()
simulator.mainloop(200., run, simulator, m, t)
#Hatchery.StopHatch()

for log in simulator.log:
    print '%s: %s took %s' % (log[0].name, log[2], log[3])

import matplotlib
import matplotlib.pyplot as plt
from numpy import array
from plot import *

fig = plt.figure()
sp = fig.add_subplot(111)
#sp.set_xlim(0,200)
#sp.set_ylim(0,600)
plt.xlabel('Time (s)')
plt.ylabel('Mineral')
for item in simulator.log:
    plotlog(sp,item)
plt.plot(t, m)
plt.show()
sys.stdout = oldStdout
