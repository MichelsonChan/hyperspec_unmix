import os
import numpy as np
from numpy import linalg as LA
import scipy
import NMF
import DSP

os.system('clear')

Y = np.matrix([[1,3,77,6],[3,0,8,9],[1,4,4,3],[7,7,2,5],[5,3,9,8]])
A = np.matrix( np.random.ranf( [ Y.shape[0] , 2 ] ) )
S = np.matrix( np.random.ranf( [ 2 , Y.shape[1] ] ) )

# ===================================================== #
# display the convergence of residual error of NNLS NMF #
# ===================================================== #

numOfInstance = 20
iteraNum = np.array( range( 0 , numOfInstance ) )
Yresidual = iteraNum.copy()
Yresidual[0] = LA.norm( Y - np.dot(A,S) , 'fro' )

for i in range( 0 , numOfInstance ) :
	A , S = NMF.NNLS( Y , 0 , S , 1 , 0 )
	Yresidual[i] = LA.norm( Y - np.dot(A,S) , 'fro' )

DSP.PLOT( np.log10( Yresidual ) , x=iteraNum , xLabel='Iteration Number' , yLabel='Residual Error' , title='|| Y - A*S ||' , grid=True )

