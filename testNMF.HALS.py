import os
import numpy as np
from numpy import linalg as LA

import NMF

os.system('clear')

Y = np.matrix([[1,2,3,4,5],[2,3,12,5,1],[5,43,5,8,9],[5,6,7,94,0],[3,2,5,7,0],[9,9,8,7,1],[3,76,0,4,7]],float)

print "Y:"
print Y
print ""

modelNum = 3

A0 = np.random.ranf([Y.shape[0],modelNum])
#A0 = np.matrix([[1,3,5],[2,4,6],[3,5,7],[4,6,8],[5,7,9],[6,8,10],[7,9,11]],float)
S0 = np.random.ranf([modelNum,Y.shape[1]])
#S0 = np.matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

#A , S = NMF.HALS( Y , A0 , S0 , 1000 , [1,1] )
A , S = NMF.HALS( Y , A0 , S0 , 1000 , [1,1] )

print "A shape:"
print A.shape
print "A:"
print A
print ""

print "S shape:"
print S.shape
print "S:"
print S
print ""

print "A*S"
Y_new = np.dot(A,S)
print Y_new
print ""

print "Y"
print Y
print ""

print "Y - A*S"
print Y - Y_new
print ""

print "norm( Y-A*S , 'fro' )"
print LA.norm( Y - Y_new , 'fro' )
print ""

