""" This script provides a toy example of the NBS """

import numpy as np
import cviewer.libs.pyconto.groupstatistics.nbs as nbs
from pylab import imshow, show, title

# import test data
# you need to be in the correct path when executing the script
# or enter absolute path
import scipy.io as io
Xmat = io.loadmat('input.mat')
X = Xmat['X']
Y = Xmat['Y']
n = X.shape[0]

# Run the NBS with the following parameter options: 
# Set an appropriate threshold. It is difficult to provide a rule of thumb 
# to guide the choice of this threshold. Trial-and-error is always an option
# with the number of permutations generated per trial set low. 
THRESH=2

# Generate 5000 permutations. Many more permutations are required in practice
# to yield a reliable estimate. 
K=5000

# Set TAIL to left, and thus test the alternative hypothesis that mean of 
# population X < mean of population Y
TAIL='left'

# Run the NBS
PVAL, ADJ, NULL = nbs.compute_nbs(X,Y,THRESH,K,TAIL)

print "pval (should be between 0.03 and 0.04): ", PVAL
print "null", NULL

imshow(ADJ, interpolation='nearest')
title('Edges identified by the NBS')
show()
