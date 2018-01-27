import matplotlib.pyplot as pl  
import numpy as np

from matplotlib.ticker import MultipleLocator, FuncFormatter  
x = np.arange(0, 4*np.pi, 0.01)  
y = np.sin(x)  
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$sin(x)$")  
ax = pl.gca()  

def pi_formatter(x, pos):   
    m = np.round(x / (np.pi/4))  
    n = 4  
    if m%2==0: m, n = m/2, n/2  
    if m%2==0: m, n = m/2, n/2  
    if m == 0:  
        return "0"  
    if m == 1 and n == 1:  
        return "$\pi$"  
    if n == 1:  
        return r"$%d \pi$" % m  
    if m == 1:  
        return r"$\frac{\pi}{%d}$" % n  
    return r"$\frac{%d \pi}{%d}$" % (m,n)  

pl.ylim(-1.5,1.5)  
pl.xlim(0, np.max(x))  

  
pl.subplots_adjust(bottom = 0.15)  

pl.grid()  

ax.xaxis.set_major_locator( MultipleLocator(np.pi/4) )  
 
ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )  
  
ax.xaxis.set_minor_locator( MultipleLocator(np.pi/20) )  
 
for tick in ax.xaxis.get_major_ticks():  
    tick.label1.set_fontsize(16)  

pl.legend()  
pl.show()  