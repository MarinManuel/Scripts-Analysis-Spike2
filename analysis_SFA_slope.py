#This python script is a helper for the spike2 script analysis_SFA.s2s
#it takes one argument, a file name containing a spreadsheet of XY pairs
#it calculates a linear regression and returns the probability that the
#slope is different from 0
#the output is stored in a file with the same name as input file, but with
#extension .res

from scipy import stats
from numpy import loadtxt
import sys

nbargs = len(sys.argv)-1
if nbargs <> 1:
    sys.exit("ERROR: 1 argument required")

dataFile = sys.argv[1]
resultFile = dataFile.replace(".dat",".res")
data = loadtxt(dataFile,skiprows=1)
slope, intercept, r_value, p_value, std_err = stats.linregress(data[:,0],data[:,1])
f = open(resultFile,'w')
f.write(str(p_value))
f.close()
