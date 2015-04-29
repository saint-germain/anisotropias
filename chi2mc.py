# Define chi2 function using fitresults and nedwithmethod
def chi2(x):
    dp2=nx*x[0]+ny*x[1]+nz*x[2]
    return np.sum(((h0-b0-dp2)/eps)**2.)  
import numpy as np
import pandas as pd
from scipy.optimize import minimize
# Output file
fout = open("optimization.txt","w")
fout.write("%s,%s,%s,%s\n" % ('Col','Dx','Dy','Dz'))
# df=query4.txt (cleaned)
df = pd.read_csv('nedpaper.csv', index_col=0)
# dfmc from Monte Carlo linear fit - mcfit.py
dfmc=pd.read_csv('fitresults.txt', index_col=0)
# Some constants
r2d = 57.295779513082321
c_kmsec = 299792.458
# No. of iterations
niter=10000
# Conversion from Glat,Glon to ???
theta=(90.-df.Glat)/r2d
phi=df.Glon/r2d
# z,D errors
sigx=df.dis_d
sigy=df.zz_d
# Build unit vector in the direction of each galaxy
nx=np.sin(theta)*np.cos(phi)
ny=np.sin(theta)*np.sin(phi)
nz=np.cos(theta)
# Parameters from MC linear fit z=a0+b0*D
b0=np.mean(dfmc.BMC)
a0=np.mean(dfmc.AMC)
# Set epsilon = quadrature error
# eps=np.sqrt(sigy**2+(b0*sigx)**2)
# Set epsilon = error propagation result for h0
eps=np.sqrt((sigy/df.dis)**2+(sigx*df.zz/(df.dis**2))**2)
# Correct for velocity (redshift) global bias (heliocentric velocity?)
znew=df.zz
#-a0
# Use v instead of z?
# vnew=znew*c_kmsec
# h0=vnew/df.dis

# h0=z/d, so it's not really H0
h0=znew/df.dis
# Initial guess for dx,dy,dz
x0 = np.array([1., 1., 1.])
# Optimization scheme for chi2
res = minimize(chi2, x0, method='nelder-mead',options={'xtol': 1e-8, 'disp': True})
# Help subsequent optimization calls with initial guess (before 2nd Monte Carlo)
x0=res.x
# 2nd Monte Carlo - for (niter) optimization calls
for k in range (1,niter):
    zzran = np.random.normal(df.zz,df.zz_d)
#    -a0
    disran=np.random.normal(df.dis,df.dis_d)
    x=disran
    y=zzran
    h0=y/x
    # Set epsilon = error propagation result for h0 - MC values
#    eps=np.sqrt((sigy/x)**2+(sigx*y/(x**2))**2)
    # Set epsilon = 1. - No errors
#    eps=1.
    sigx,sigy=(0.06*df.dis),(0.02*df.zz)
    eps=np.sqrt((sigy/df.dis)**2+(sigx*df.zz/(df.dis**2))**2)
    res = minimize(chi2, x0, method='nelder-mead',options={'xtol': 1e-8})
# 'disp': True
    fout.write("%d, %s, %s, %s\n" % (k,res.x[0],res.x[1],res.x[2]))
    print k,res.fun
fout.close()
# Clean results for dx,dy,dz outliers, create new array = dfnew
dfopt=pd.read_csv('optimization.txt', index_col=0)
dfnew=dfopt[np.absolute((dfopt.Dx-np.mean(dfopt.Dx))/dfopt.Dx) < 0.5]
dfnew=dfnew[np.absolute((dfnew.Dy-np.mean(dfnew.Dy))/dfnew.Dy) < 0.5]
dfnew=dfnew[np.absolute((dfnew.Dz-np.mean(dfnew.Dz))/dfnew.Dz) < 0.5]
dfnew.to_csv('out.csv')
# Compare to paper dx,dy,dz, obtain arccos(n(dot)d), for n,d = unitary vectors
DSx=3.3
DSy=-2.4
DSz=-1.4
desvx=np.std(dfopt.Dx)*100/np.mean(dfopt.Dx)
desvy=np.std(dfopt.Dy)*100/np.mean(dfopt.Dy)
desvz=np.std(dfopt.Dz)*100/np.mean(dfopt.Dz)
dhip=np.sqrt(dfopt.Dx**2+dfopt.Dy**2+dfopt.Dz**2)
angles=r2d*np.arccos((dfopt.Dx*DSx+dfopt.Dy*DSy+dfopt.Dz*DSz)/(dhip*np.sqrt(DSx**2+DSy**2+DSz**2)))
thangle=np.arccos(dfopt.Dz/dhip)
phangle=np.arctan2(dfopt.Dy,dfopt.Dx)
#angle1=r2d*np.arccos((res.x[0]*DSx+res.x[1]*DSy+res.x[2]*DSz)/(np.sqrt(res.x[0]**2+res.x[1]**2+res.x[2]**2)*np.sqrt(DSx**2+DSy**2+DSz**2)))

