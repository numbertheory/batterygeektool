#!/usr/bin/env python
# coding=UTF-8
 
import math, subprocess, os
 
p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"], stdout=subprocess.PIPE)
output = p.communicate()[0]
 
o_max = [l for l in output.splitlines() if 'MaxCapacity' in l][0]
o_cur = [l for l in output.splitlines() if 'CurrentCapacity' in l][0]
 
b_max = float(o_max.rpartition('=')[-1])
b_cur = float(o_cur.rpartition('=')[-1])
 
charge = b_cur / b_max

print int(charge*100)

level = int(charge*10)

os.system('cp batt0' + str(level) + '0.png x.png')