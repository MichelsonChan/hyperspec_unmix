# ====== #
# DSP.py #
# ====== #

# ====== #
# import #
# ====== #
import os
import numpy as np
from numpy import linalg as LA
from numpy import genfromtxt
import matplotlib.pyplot as plt

# =================== #
# function definition #
# =================== #


# === #
# LOG #
# === #
def LOG( actionStr , arg1 , arg2 , arg3 ) :
	if actionStr == 'log matrix to file' :
		fileNameStr = arg1
		matrix      = arg2
		delimStr    = arg3
		# =============================== #
		# check if the provided file name #
		# already exists in the directory #
		# =============================== #
		if os.path.isfile( fileNameStr ) :
			os.remove( fileNameStr )
		fileObject  = open( fileNameStr , 'w' )
		M , N = matrix.shape
		i , j = 0 , 0
		for i in range( 0 , M ) :
			for j in range( 0 , N ) :
				fileObject.write( str( matrix[i][j] ) + delimStr )
			fileObject.write( '\n' )
		fileObject.close()
		return


# ==== #
# STOP #
# ==== #
def STOP() :
	if os.path.isfile('stop') :
		# a stopping request exists
		print "A stopping request is found ! System paused !"
		print "Press enter/return to continue ..."
		raw_inpiut()
	return


# ========== #
# READMATRIX #
# ========== #
def READMATRIX( fileName , delimStr ) :

# ===================================================== #
# fileName is the file located in current directory     #
# delimStr is the character(s) that separate the number #
# if USGS Library ASCII data is to be read,             #
# delimStr will be '     ' ( 5 white spaces )           #
# ===================================================== #
	return genfromtxt( fileName , delimiter=delimStr )


# ============ #
# READUSGSDATA #
# ============ #
def READUSGSDATA( fileName ) :

# =============================== #
# same as READMATRIX()            #
# customize for reading USGS data #
# =============================== #
	return genfromtxt( fileName , delimiter='     ' )


# ==== #
# PLOT #
# ==== #
def PLOT( y , x=None , yLabel=None , xLabel=None , title=None , axis=None , grid=None ) :
	
	#plt.ion() # enable interactive mode
	
        if yLabel != None :
                plt.ylabel( yLabel ) # a string 
	
        if xLabel != None :
                plt.xlabel( xLabel ) # a string
	
        if title  != None :
                plt.title( title )   # a string
	
        if axis   != None :
                plt.axis( axis )     # a 4-entry array
	
        if grid   != None :
                if( grid == 1 or grid == True or grid.lower() == "true" ) :
                                         #           ^
                                         #           |
                                         #           |
                                         # note: this grid.lower() must
                                         # be placed at last so that error
                                         # would not be resulted when 
                                         # grid is boolean or numeric 
                        plt.grid(True)
	
        if x      != None :
                plt.plot( x , y )
	
        else :
                plt.plot( y )
	
        plt.show()
	#print "continue ..."
	#plt.show()
	
	return


# === #
# SPA #
# === #
def SPA( Y , N ) :

# ===================== #
# Y is assumed to be of #
# numpy.matrix class    #
# ===================== #

	# ============== #
	# initialization #
	# ============== #
	ENDMEM      = np.zeros( [Y.shape[0],N] )
	PPI         = np.zeros( N )
	SPA_ProjMat = np.eye( Y.shape[0] )

 	for i in range(0,N) : # same as for(i=0;i<N;i++)

		normSquareArray = np.zeros( Y.shape[1] )

		for j in range(0,Y.shape[1]) :
			normSquareArray[j] = LA.norm(np.dot(SPA_ProjMat,Y[:,j:j+1]),2)
		# =================================== #
		# strongest endmember power detection #
		# and indication of such (pure)pixel  #
		# =================================== #
		maxV , PPI[i]   = normSquareArray.max() , normSquareArray.argmax()
		ENDMEM[:,i:i+1] = Y[:,PPI[i]:PPI[i]+1]
		# ======================== #
		# update projection matrix #
		# ======================== #
		ak          = np.dot(SPA_ProjMat,ENDMEM[:,i:i+1])
		eyeMat      = np.eye(Y.shape[0])
		ak_Mat      = np.dot(ak,ak.transpose())
		ak_pow      = LA.norm(ak,2)**2
		SPA_ProjMat = np.dot( ( eyeMat - ak_Mat / ak_pow  ) , SPA_ProjMat )

	return ENDMEM , PPI

