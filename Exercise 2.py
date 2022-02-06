import numpy as np
import matplotlib.pyplot as plt
import sys

def func(x):
    if 0<=x<=np.pi:
        return 1
    if np.pi<x<=2*np.pi:
        return -1

def simpson(f, a, b, n):
    if n%2 != 0:
        sys.exit('n must be even')
    h=(b-a)/n
    s=0.0
    x=a+h
    for i in range(1,int(n/2+1)):
        s+=4*f(x)
        x+=2*h

    x=a+2*h
    for i in range(1,int(n/2)):
        s+=2*f(x)
        x+=2*h
    return (h/3)*(f(a)+f(b)+s)

def ak(f,a,T,k,n):
    def fcos(x):
        return f(x)*np.cos(x*k*(2*np.pi)/T)
    return (2/T)*simpson(fcos,a,T+a,n)

#USING A0/2, NOT A0

def bk(f,a,T,k,n):
    def fsin(x):
        return f(x)*np.sin(x*k*(2*np.pi)/T)
    return (2/T)*simpson(fsin,a,T+a,n)

def fourier(f,a,T,k,n,x):
    i=1
    four=ak(f,a,T,0,n)/2
    while i<=k:
        foursin=bk(f,a,T,i,n)*np.sin(i*2*(np.pi/T)*x)
        fourcos=ak(f,a,T,i,n)*np.cos(i*2*(np.pi/T)*x)
        four=four+foursin+fourcos
        i+=1
    return four

# xs=np.linspace(-0.1,2*np.pi+0.1,1000)
# s1=[]
# s2=[]
# s3=[]
# s5=[]
# s10=[]
# s20=[]
# s30=[]
# i=0
# exp=[]
# while i<len(xs):
#     exp.append(func(xs[i]))
#     s1.append(fourier(func,0,2*np.pi,1,32,xs[i]))
#     s2.append(fourier(func,0,2*np.pi,2,32,xs[i]))
#     s3.append(fourier(func,0,2*np.pi,3,32,xs[i]))
#     s5.append(fourier(func,0,2*np.pi,5,32,xs[i]))
#     s10.append(fourier(func,0,2*np.pi,10,128,xs[i]))
#     s20.append(fourier(func,0,2*np.pi,20,128,xs[i]))
#     s30.append(fourier(func,0,2*np.pi,30,128,xs[i]))
#     i+=1

# alphas=np.linspace(0.9,1,7)
# widths=np.linspace(0.55,0.6,7)
# plt.plot(xs,exp,linewidth=2,c='black',label=r'$f(\theta)$')
# plt.plot(xs,s1,linewidth=widths[0],alpha=alphas[0],label='1 term',c='red')
# plt.plot(xs,s2,linewidth=widths[1],alpha=alphas[1],label='2 terms',c='orange')
# plt.plot(xs,s3,linewidth=widths[2],alpha=alphas[2],label='3 terms',c='yellow')
# plt.plot(xs,s5,linewidth=widths[3],alpha=alphas[3],label='5 terms',c='green')
# plt.plot(xs,s10,linewidth=widths[4],alpha=alphas[4],label='10 terms',c='blue')
# plt.plot(xs,s20,linewidth=widths[5],alpha=alphas[5],label='20 terms',c='indigo')
# plt.plot(xs,s30,linewidth=widths[6],alpha=alphas[6],label='30 terms',c='violet')
# plt.legend(fontsize='small',loc=(0.625,0.45))
# plt.xlabel(r'$\theta$')
# plt.ylabel(r'$f(\theta)$')
# # plt.savefig('square.pdf')
# plt.show()

aks=[]
bks=[]
test=[]
i=1
length=10
index=np.linspace(1,length,length)
while i<=length:
    aks.append(ak(func,0,2*np.pi,i,2048))
    bks.append(bk(func,0,2*np.pi,i,2048))
    test.append(4/(np.pi*i))
    i+=1

plt.scatter(index,aks,label=r'$a_k$',c='green',alpha=0.5,marker='^')
plt.scatter(index,bks,label=r'$b_k$',c='purple',alpha=0.5,marker='v')
plt.plot(index,test,alpha=0.5,c='purple',label=r'$\frac{4}{\pi k}$')
plt.xlim(0,length*1.05)
plt.xlabel('k')
plt.legend()
plt.savefig('yokey.pdf')
plt.show()