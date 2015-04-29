import numpy as np
import pandas as pd
# df=query4.txt (cleaned)
df = pd.read_csv('nedpaper.csv', index_col=0)
# dfmc from Monte Carlo linear fit - mcfit.py
dfmc=pd.read_csv('fitresults.txt', index_col=0)
# Some constants
r2d = 57.295779513082321
# Conversion from Glat,Glon to ???
theta=(90.-df.Glat)/r2d
phi=df.Glon/r2d
# Parameters from MC linear fit z=a0+b0*D
b0=np.mean(dfmc.BMC)
a0=np.mean(dfmc.AMC)
get_ipython().magic(u'pylab ')

#dhip=np.sqrt(dfopt.Dx**2+dfopt.Dy**2+dfopt.Dz**2)
#thangle=np.arccos(dfopt.Dz/dhip)
#phangle=np.arctan2(dfopt.Dy,dfopt.Dx)