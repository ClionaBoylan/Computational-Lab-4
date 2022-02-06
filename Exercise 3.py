import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import scipy.signal

def func(x):
    return np.sin(6*np.pi*x)

h=5.0/144.0
# h=0.04
h=0.04
N=128
N=32
i=0
ts=[]
omegas=[]
while i<N:
    ts.append(i*h)
    omegas.append((2*np.pi*(i+1))/(N*h))
    i+=1

smoothtime=np.linspace(0,N*h,1000)
smoothfunc=[]
i=0
while i<len(smoothtime):
    smoothfunc.append(func(smoothtime[i]))
    i+=1


fs=[]
i=0
while i<N:
    fs.append(func(ts[i]))
    i+=1

def fnreal(n):
    result=0.0
    i=0
    while i<N:
        result+=fs[i]*np.cos((2*np.pi*i*n)/N)
        i+=1
    return result

def fnimag(n):
    result=0.0
    i=0
    while i<N:
        result+=-fs[i]*np.sin((2*np.pi*i*n)/N)
        i+=1
    return result

def fm(m):
    result=0.0
    i=0
    while i<N:
        result+=complex(fnreal(i),fnimag(i))*(complex(np.cos((2*np.pi*m*i)/N),np.sin((2*np.pi*m*i)/N)))
        i+=1
    return result/N

funcs=[]
i=0
while i<N:
    funcs.append(func(i*h))
    i+=1

print('Sampling Rate:',(1/h))
print()
print('Fundamental Frequency:',omegas[0])

# plt.scatter(ts,funcs,s=10,c='red',label='Sampled Points',zorder=2)
# plt.plot(ts,funcs,linewidth=2,c='black',zorder=1)
# plt.ylabel(r'$f(t)$')
# plt.xlabel('t')
# plt.legend(fontsize='x-small')
# # plt.savefig('Sampled.pdf')
# plt.show()

index=[]
fnreals=[]
fnimags=[]
i=0
while i<N:
    fnreals.append(fnreal(i))
    fnimags.append(fnimag(i))
    index.append(i)
    i+=1

# plt.plot(index,fnreals,label=r'$F_{n,real}$',c='red')
# # plt.ylabel(r'$F_{n,real}$')
# plt.xlabel('n')
# # plt.show()

# plt.plot(index,fnimags,label=r'$F_{n,imaginary}$',c='blue')
# # plt.ylabel(r'$F_{n,imaginary}$')
# # plt.xlabel('n')
# plt.legend()
# plt.savefig('fn6.4.pdf')
# plt.show()

recons=[]
realrecons=[]
imagrecons=[]
times=[]
diff=[]
i=0
while i<N:
    a=fm(i)
    recons.append(a)
    realrecons.append(np.real(a))
    imagrecons.append(np.imag(a))
    times.append(i*h)
    diff.append(realrecons[i]-funcs[i])
    i+=1

# plt.plot(times,imagrecons)
# plt.show()

# plt.plot(smoothtime,smoothfunc,linewidth=1,label='Original',zorder=1,c='orange',alpha=0.5)
# plt.plot(times,realrecons,linewidth=3,label='Reconstruction',zorder=2,c='black')
# plt.scatter(times,funcs,label='Sampled Points',zorder=3,c='orange',alpha=0.75)
# plt.xlabel(r't')
# plt.ylabel(r'f(t)')
# plt.legend()
# plt.savefig('Reconstruction6.4.pdf')
# plt.show()

# plt.plot(times,diff)
# plt.show()

powerspec=[]
i=0
while i<N:
    powerspec.append(fnreal(i)**2+fnimag(i)**2)
    i+=1
 
index2=[]
i=1
while i<=N:
    index2.append(i)
    i+=1

plt.bar(index,powerspec,color='blue')
plt.ylabel(r'$P_n$')
plt.xlabel('n')
# plt.savefig('Spectrum1.pdf')
plt.show()

fourier_transform = np.fft.rfft(funcs)

abs_fourier_transform = np.abs(fourier_transform)

power_spectrum = np.square(abs_fourier_transform)

plt.plot(power_spectrum)
plt.show()

plt.plot(scipy.signal.periodogram(funcs,h)[0],scipy.signal.periodogram(funcs,h)[1])
plt.show()







