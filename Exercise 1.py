import numpy as np
import matplotlib.pyplot as plt
import sys

def func(x):
    return np.sin(x)+2*np.cos(3*x)+3*np.sin(5*x)

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

def ak(f,T,k,n):
    def fcos(x):
        return f(x)*np.cos(x*k*(2*np.pi)/T)
    return (2/T)*simpson(fcos,0,T,n)

#USING A0/2, NOT A0

def bk(f,T,k,n):
    def fsin(x):
        return f(x)*np.sin(x*k*(2*np.pi)/T)
    return (2/T)*simpson(fsin,0,T,n)

def fourier(f,T,k,n,x):
    i=1
    four=ak(f,T,0,n)/2
    while i<=k:
        foursin=bk(f,T,i,n)*np.sin(i*2*(np.pi/T)*x)
        fourcos=ak(f,T,i,n)*np.cos(i*2*(np.pi/T)*x)
        four=four+foursin+fourcos
        i+=1
    return four

# xs=np.linspace(-0.1,2*np.pi+0.1,1000)
# s1=[]
# s2=[]
# s3=[]
# s4=[]
# s5=[]
# s6=[]
# s7=[]
# s8=[]
# s9=[]
# s10=[]
# error=[]
# i=0
# funk=[]
# while i<len(xs):
#     funk.append(func(xs[i]))
#     s1.append(fourier(func,2*np.pi,0,32,xs[i]))
#     s2.append(fourier(func,2*np.pi,1,32,xs[i]))
#     s3.append(fourier(func,2*np.pi,2,32,xs[i]))
#     s4.append(fourier(func,2*np.pi,3,32,xs[i]))
#     s5.append(fourier(func,2*np.pi,4,32,xs[i]))
#     s6.append(fourier(func,2*np.pi,5,32,xs[i]))
#     s7.append(fourier(func,2*np.pi,6,32,xs[i]))
#     s8.append(fourier(func,2*np.pi,7,32,xs[i]))
#     s9.append(fourier(func,2*np.pi,8,32,xs[i]))
#     s10.append(fourier(func,2*np.pi,9,32,xs[i]))
#     error.append(funk[i]-s10[i])
#     i+=1


# alphas=np.linspace(0.3,1,10)
# plt.plot(xs,funk,linewidth=2,c='blue')
# plt.plot(xs,s1,linewidth=0.5,c='blue',alpha=alphas[0])
# plt.plot(xs,s2,linewidth=0.5,c='blue',alpha=alphas[1])
# plt.plot(xs,s3,linewidth=0.5,c='blue',alpha=alphas[2])
# plt.plot(xs,s4,linewidth=0.5,c='blue',alpha=alphas[3])
# plt.plot(xs,s5,linewidth=0.5,c='blue',alpha=alphas[4])
# plt.plot(xs,s6,linewidth=0.5,c='blue',alpha=alphas[5])
# plt.plot(xs,s7,linewidth=0.5,c='blue',alpha=alphas[6])
# plt.plot(xs,s8,linewidth=0.5,c='blue',alpha=alphas[7])
# plt.plot(xs,s9,linewidth=0.5,c='blue',alpha=alphas[8])
# plt.plot(xs,s10,linewidth=0.7,c='blue',alpha=alphas[9])
# plt.show()

aks=[]
bks=[]
i=1
length=10
index=np.linspace(1,length,length)
while i<=length:
    aks.append(ak(func,2*np.pi,i,32))
    bks.append(bk(func,2*np.pi,i,32))
    i+=1

plt.scatter(index,aks,label=r'$a_k$',c='green',alpha=0.5,marker='^')
plt.scatter(index,bks,label=r'$b_k$',c='purple',alpha=0.5,marker='v')
plt.xlim(0,length*1.05)
plt.xlabel('k')
plt.legend()
plt.savefig('ab4.pdf')
plt.show()

# def func1(x):
#     return np.sin(x)

# def func2(x):
#     return np.cos(x)+3*np.cos(2*x)-4*np.cos(3*x)

# def func3(x):
#     return np.sin(x)+3*np.sin(3*x)+5*np.sin(5*x)

# def func4(x):
#     return np.sin(x)+2*np.cos(3*x)+3*np.sin(5*x)

# f1=[]
# f2=[]
# f3=[]
# f4=[]
# i=0
# while i<len(xs):
#     f1.append(func1(xs[i]))
#     f2.append(func2(xs[i]))
#     f3.append(func3(xs[i]))
#     f4.append(func4(xs[i]))
#     i+=1

# plt.scatter(xs,f1,s=0.2,c=xs,cmap='autumn')
# plt.xlabel('x')
# plt.ylabel(r'$f(t)$')
# plt.title(r'$f(t)=\sin(\omega t)$')
# plt.savefig('f1.pdf')
# plt.show()

# plt.scatter(xs,f2,s=0.2,c=xs,cmap='autumn')
# plt.xlabel('x')
# plt.ylabel(r'$f(t)$')
# plt.title(r'$f(t)=\cos(\omega t)+3\cos(2 \omega t)-4\cos(3 \omega t)$')
# plt.savefig('f2.pdf')
# plt.show()

# plt.scatter(xs,f3,s=0.2,c=xs,cmap='autumn')
# plt.xlabel('x')
# plt.ylabel(r'$f(t)$')
# plt.title(r'$f(t)=\sin(\omega t)+3\sin(3 \omega t)+5\sin(5 \omega t)$')
# plt.savefig('f3.pdf')
# plt.show()

# plt.scatter(xs,f4,s=0.2,c=xs,cmap='autumn')
# plt.xlabel('x')
# plt.ylabel(r'$f(t)$')
# plt.title(r'$f(t)=\sin(\omega t)+2\cos(3 \omega t)+3\sin(5 \omega t)$')
# plt.savefig('f4.pdf')
# plt.show()