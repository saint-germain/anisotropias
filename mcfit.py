import numpy as np
import pandas as pd
from scipy import constants
df = pd.read_csv('nedpaper.csv', index_col=0)
niter=1000000
fout = open("fitresults.txt","w")
x=df.dis
sigx=df.dis_d
y=df.zz
sigy=df.zz_d
#*constants.c
num=len(x)
sy=y.sum(axis=0)
sx=x.sum(axis=0)
xx=x*x
sxx=xx.sum(axis=0)
xy=x*y
sxy=xy.sum(axis=0)
delta=delta=num*sxx-(sx**2)
a=(sy*sxx-sx*sxy)/delta
b=(num*sxy-sx*sy)/delta
eps=np.sqrt(sigy**2+(b*sigx)**2)
w=1/(eps**2)
wy=y*w
wx=x*w
wx2=x*wx
wxy=wx*y
sw=w.sum(axis=0)
swy=wy.sum(axis=0)
swx=wx.sum(axis=0)
swx2=wx2.sum(axis=0)
swxy=wxy.sum(axis=0)
delta=sw*swx2-(swx**2)
a1=(swy*swx2-swx*swxy)/delta
b1=(sw*swxy-swx*swy)/delta
epsmc=np.sqrt(sigy**2+(b1*sigx)**2)
w=1/(epsmc**2)
fout.write("%s,%s,%s\n" % ('Col','AMC','BMC'))

for k in range (1,niter):
    zzran = np.random.normal(df.zz,df.zz_d)
    disran=np.random.normal(df.dis,df.dis_d)
    x=disran
    y=zzran
    wy=y*w
    wx=x*w
    wx2=x*wx
    wxy=wx*y
    sw=w.sum(axis=0)
    swy=wy.sum(axis=0)
    swx=wx.sum(axis=0)
    swx2=wx2.sum(axis=0)
    swxy=wxy.sum(axis=0)
    delta=sw*swx2-(swx**2)
    amc=(swy*swx2-swx*swxy)/delta
    bmc=(sw*swxy-swx*swy)/delta
#    print k,amc,bmc
    fout.write("%d, %s, %s\n" % (k,amc,bmc))
fout.close()
dfmc=pd.read_csv('fitresults.txt', index_col=0)
