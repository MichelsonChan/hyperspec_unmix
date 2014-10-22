# ====== #
# NMF.py #
# ====== #

# ====== #
# import #
# ====== #
import os
import numpy as np
from numpy import linalg as LA
import scipy.optimize.nnls


# =================== #
# function definition #
# =================== #


# ======================================= #
# Non-Negative Least Squares (Alternating)#
# ======================================= #
def NNLS( Y , A , S , iteraNum , firstUpdateMatrixFlag ) :
	# ======================================== #
	# if    firstUpdateMatrixFlag == 0         #
	# then  A will be updated first by using S #
	# elif  firstUpdateMatrixFlag == 1         #
	# then  S will be updated first by using A #
	# ======================================== #
	if firstUpdateMatrixFlag == 1 :
		# ========================== #
		# need to update S first     #
		# check dimension of Y and A #
		# ========================== #
		if Y.shape[0] != A.shape[0] :
			print "Error @ NMF.NNLS() : dimension of Y and A mismatch !!!"
			print "Press any key to stop ..."
			raw_input()
			err
			return -1
		# ====================================== #
		# initialize modelOrder and A , S matrix #
		# ====================================== #
		modelOrder = A.shape[1]
		# A takes the input matrix as initial matrix
		# or reuse the updated matrix in the last iteration
		S = np.zeros( [ modelOrder , Y.shape[1] ] )
		itera = 0
		for itera in range( 0 , iteraNum ) :
			print "iteration : %d/%d" % ( itera+1 , iteraNum )
			# ~~~~~~~~~~~~~ #
			# Update S Part #
			# ~~~~~~~~~~~~~ #
			# ~~~~~~~~~~~~~~~~~~~~ #
			# mathematical model : #
			# Y = A * S            #
			# ~~~~~~~~~~~~~~~~~~~~ #
			# ------------------------------------- #
			# in min( || Y - A * S ||2 )            #
			#    sub to S geq 0                     #
			# for each column of S , perform NNLS   #
			# by using A matrix and jth column of Y #
			# jth column is indicated by S_j        #
			# ------------------------------------- #
			for j in range( 0 , Y.shape[1] ) :
				# ----------------------------- #
				# prepare a Y column vector Y_j #
				# ----------------------------- #
				Y_j = np.zeros( [ 1 , Y.shape[0] ] )[0]
				#             conversion to array for scipy requires 
				#             a row matrix such that the shape is
				#             taken as a transpose
				#             Y_j = np.zeros( [ Y.shape[0] , 1 ] )
				for k in range( 0 , Y.shape[0] ) :
					Y_j[k] = Y[ k , j ]
				# --------- #
				# NNLS part #
				# --------- #
				S_j = scipy.optimize.nnls( A , Y_j )[0]
				# ----------------------------------- #
				# update the obatined optimized       #
				# value of the jth column to S matrix #
				# ----------------------------------- #
				for k in range( 0 , S_j.size ) :
					S[ k , j ] = S_j[k]
			# ~~~~~~~~~~~~~ #
			# Update A Part #
			# ~~~~~~~~~~~~~ #
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
			# mathematical model :          #
			# Yt = St * At                  #
			# where Xt means transpose of X # 
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
			Yt = Y.transpose()
			At = A.transpose()
			St = S.transpose()
			# --------------------------------------- #
			# in min( || Yt - St * At ||2 )           #
			#    sub to At geq 0                      #
			# for each column of At , perform NNLS    #
			# by using St matrix and ith column of Yt #
			# ith column is indicated by Yt_j         #
			# --------------------------------------- #
			for j in range( 0 , Yt.shape[1] ) :
				# ------------------------------- #
				# prepare a Yt column vector Yt_j #
				# ------------------------------- #
				Yt_j = np.zeros( [ 1 , Yt.shape[0] ] )[0]
				#             conversion to array for scipy requires 
				#             a row matrix such that the shape is 
				#             taken as a transpose
				#             Yt_j = np.zeros( [ Yt.shape[0] , 1 ] )
				for k in range( 0 , Yt.shape[0] ) :
					Yt_j[k] = Yt[ k , j ]
				# --------- #
				# NNLS part #
				# --------- #
				At_j = scipy.optimize.nnls( St , Yt_j )[0]
				# ------------------------------------ #
				# update the obtained optimized        #
				# value of the jth column to At matrix #
				# ------------------------------------ #
				for k in range( 0 , At_j.size ) :
					At[ k , j ] = At_j[k]
			# --------------------------------------------- #
			# update A after the above transposed NNLS      #
			# no need to update S matrix as it is unchanged #
			# --------------------------------------------- #
			A = At.transpose()
		# ===================== #
		# End of NNLS iteration #
		# ===================== #
		return A , S
	elif firstUpdateMatrixFlag == 0 :
		# ========================== #
		# need to update A first     #
		# check dimension of Y and S #
		# ========================== #
		if Y.shape[1] != S.shape[1] :
			print "Error @ DSP.NNLS() : dimension of Y and S mismatch !!!"
			print "Press any key to stop ..."
			raw_input()
			err
			return -1
		# ====================================== #
		# initialize modelOrder and A , S matrix #
		# ====================================== #
		modelOrder = S.shape[0]
		A = np.zeros( [ Y.shape[0] , modelOrder ] )
		# S takes the input matrix as initial matrix
		# or reuse the updated matrix in the last iteration
		itera = 0
		for itera in range( 0 , iteraNum ) :
			print "iteration : %d/%d" % ( itera+1 , iteraNum )
			# ~~~~~~~~~~~~~ #
			# Update A Part #
			# ~~~~~~~~~~~~~ #
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
			# mathematical model :          #
			# Yt = St * At                  #
			# where Xt means transpose of X # 
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
			Yt = Y.transpose()
			At = A.transpose()
			St = S.transpose()
			# --------------------------------------- #
			# in min( || Yt - St * At ||2 )           #
			#    sub to At geq 0                      #
			# for each column of At , perform NNLS    #
			# by using St matrix and ith column of Yt #
			# ith column is indicated by Yt_j         #
			# --------------------------------------- #
			for j in range( 0 , Yt.shape[1] ) :
				# ------------------------------- #
				# prepare a Yt column vector Yt_j #
				# ------------------------------- #
				Yt_j = np.zeros( [ 1 , Yt.shape[0] ] )[0]
				#             conversion to array for scipy requires 
				#             a row matrix such that the shape is 
				#             taken as a transpose
				#             Yt_j = np.zeros( [ Yt.shape[0] , 1 ] )
				for k in range( 0 , Yt.shape[0] ) :
					Yt_j[k] = Yt[ k , j ]
				# --------- #
				# NNLS part #
				# --------- #
				At_j = scipy.optimize.nnls( St , Yt_j )[0]
				# ------------------------------------ #
				# update the obtained optimized        #
				# value of the jth column to At matrix #
				# ------------------------------------ #
				for k in range( 0 , At_j.size ) :
					At[ k , j ] = At_j[k]
			# --------------------------------------------- #
			# update A after the above transposed NNLS      #
			# no need to update S matrix as it is unchanged #
			# --------------------------------------------- #
			A = At.transpose()
			# ~~~~~~~~~~~~~ #
			# Update S Part #
			# ~~~~~~~~~~~~~ #
			# ~~~~~~~~~~~~~~~~~~~~ #
			# mathematical model : #
			# Y = A * S            #
			# ~~~~~~~~~~~~~~~~~~~~ #
			# ------------------------------------- #
			# in min( || Y - A * S ||2 )            #
			#    sub to S geq 0                     #
			# for each column of S , perform NNLS   #
			# by using A matrix and jth column of Y #
			# jth column is indicated by S_j        #
			# ------------------------------------- #
			for j in range( 0 , Y.shape[1] ) :
				# ----------------------------- #
				# prepare a Y column vector Y_j #
				# ----------------------------- #
				Y_j = np.zeros( [ 1 , Y.shape[0] ] )[0]
				#             conversion to array for scipy requires 
				#             a row matrix such that the shape is
				#             taken as a transpose
				#             Y_j = np.zeros( [ Y.shape[0] , 1 ] )
				for k in range( 0 , Y.shape[0] ) :
					Y_j[k] = Y[ k , j ]
				# --------- #
				# NNLS part #
				# --------- #
				S_j = scipy.optimize.nnls( A , Y_j )[0]
				# ----------------------------------- #
				# update the obatined optimized       #
				# value of the jth column to S matrix #
				# ----------------------------------- #
				for k in range( 0 , S_j.size ) :
					S[ k , j ] = S_j[k]
		# ===================== #
		# End of NNLS iteration #
		# ===================== #
		return A , S





# ============================= #
# Lee Seung Mulplicative Update #
# ============================= #
def LSMU( V , W0 , H0 , iteraNum ) :
	# ========== #
	# NMF Model: #
	# V = W * H  #
	# ========== #
	# ===================== #
	# check dimension match #
	# ===================== #
	vM , vN = V.shape
	wM , wN = W0.shape
	hM , hN = H0.shape

	if wN != hM :
		print "Error @ NMF.LSMU() : dimension mismatch !"
		print "wN != hM !!!!!"
		print "Press any key to stop ..."
		raw_input()
		err
		return -1

	if vM != wM :
		print "Error @ NMF.LSMU() : dimension mismatch !"
                print "vM != wM !!!!!"
		print "Press any key to stop ..."
                raw_input()
		err
		return -1

	if vN != hN :
		print "Error @ NMF.LSMU() : dimension mismatch !"
	        print "vN != hN !!!!!"
		print "Press any key to stop ..."
                raw_input()
		err
		return -1

	#W = W0.copy()
	#H = H0.copy()
	W = W0
	H = H0
	
	# ===================== #
	# multiplicative update #
	# ===================== #
	for i in range(0,iteraNum) :
		W = np.multiply( W , ( np.dot(V,H.transpose()) / np.dot(W,np.dot(H,H.transpose())) ) )
		H = np.multiply( H , ( np.dot(W.transpose(),V) / np.dot(W.transpose(),np.dot(W,H)) ) )
	return W , H

# ====================================== #
# Hierarchical Alternating Least Squares #
# ====================================== #

# -------------- #
# HALS core part #
# -------------- #
def HALS_CORE( X , W , H , modelOrder ) :

	for i in range( 0 , modelOrder ) :
		print "\t\tstatus: %d / %d" %( i , modelOrder )

		# ============================== #
		# generate the index array       #
		# the following approach is used #
		# to skip the current index      #
		# ============================== #
		if i == 0 :
			sumIdxArray = range( 1 , modelOrder )
		elif i == modelOrder-1 :
			sumIdxArray = range( 0 , modelOrder-1 )
		else :
			#sumIdxArray = range( 0 , i-1 ) + range( i+1 , modelOrder )
			sumIdxArray = range( 0 , i ) + range( i+1 , modelOrder )
		
		# =========== #
		# HALS update #
		# =========== #
		h_sum = 0
		for j in sumIdxArray :
			h = np.dot( H[j:j+1,:] , H[i:i+1,:].transpose() )
			h_sum = h_sum + np.dot( W[:,j:j+1] , h )
		w = ( np.dot(X,H[i:i+1,:].transpose()) - h_sum ) / (LA.norm(H[i:i+1,:],2)**2)
		for k in range( 0 , len(w) ) :
			if w[k] > 0 :
				W[k,i] = w[k]
			else :
				W[k,i] = 0
	return W

# ------------------- #
# HALS interface part #
# ------------------- #
def HALS( Y , A0 , S0 , iteraNum , A2S_iteraRatioVector ) :
	
	# ======================== #
	# check dimension mismatch #
	# ======================== #
	yM , yN = Y.shape
	aM , aN = A0.shape
	sM , sN = S0.shape
	
	modelOrder = aN
	
	if aN != sM :
		print "Error @ NMF.HALS() : dimension mismatch !"
		print "aN != sM !!!"
		print "Press any key to stop ..."
		raw_input()
		err
		return -1

	if yM != aM :
		print "Error @ NMF.HALS() : dimension mismatch !"
		print "yM != aM !!!"
		print "Press any key to stop ..."
		raw_input()
		err
		return -1

	if yN != sN :
		print "Error @ NMF.HALS() : dimension mismatch !"
		print "yN != sN !!!"
		print "Press any key to stop ..."
		raw_input()
		err
		return -1

	for i in range( 0 , iteraNum ) :
		print "iteration: %d / %d" %( i , iteraNum )
		# =============== #
		# update A matrix #
		# =============== #
		print "update A matrix"
		for k in range( 0 , A2S_iteraRatioVector[0] ) :
			A = HALS_CORE( Y , A0 , S0 , modelOrder )
		# =============== #                            	
       		# update S matrix #
       		# =============== #
		print "update S matrix"
       		for k in range( 0 , A2S_iteraRatioVector[1] ) :
       			S = HALS_CORE( Y.transpose() , S0.transpose() , A0.transpose() , modelOrder )
			S = S.transpose()
	return A , S
