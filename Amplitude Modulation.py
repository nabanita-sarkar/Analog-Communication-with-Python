import numpy as np
import matplotlib.pyplot as plt

#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)

A_c = float(input('Enter carrier amplitude: '))
f_c = float(input('Enter carrier frquency: '))
A_m = float(input('Enter message amplitude: '))
f_m = float(input('Enter message frquency: '))
modulation_index = float(input('Enter modulation index: '))
#print(modulation_index)

t = np.arange(100000.0)/100000
carrier=A_c*np.cos(2*np.pi*f_c*t)
modulator=A_m*np.cos(2*np.pi*f_m*t)

product=A_c*(1+modulation_index*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)

plt.subplot(3,1,1)
plt.title('Amplitude Modulation')
plt.plot(modulator,'g')
plt.ylabel('Amplitude')
plt.xlabel('Modulator signal')

plt.subplot(3,1,2)
plt.plot(carrier, 'r')
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,1,3)
plt.plot(product, color="purple")
plt.ylabel('Amplitude')
plt.xlabel('Output signal')
plt.subplots_adjust(hspace=1)

plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16, 9)
#fig.savefig('Amplitude Modulation.png', dpi=100)
