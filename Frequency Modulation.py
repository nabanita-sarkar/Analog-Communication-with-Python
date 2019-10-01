import numpy as np
import matplotlib.pyplot as plt

#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c*np.cos(2*pi*f_c*t + modulation_index*np.sin(2*pi*f_m*t))

f_m = float(input('Enter message frquency: '))
A_m = float(input('Enter message amplitude: '))
f_c= float(input('Enter carrier frquency: '))
A_c = float(input('Enter carrier amplitude: '))
modulation_index= float(input('Enter modulation index: '))

time = np.linspace(0, 1, 1000)
modulator = A_m*np.cos(2.0*pi*f_m*time)
carrier = A_c*np.cos(2.0*pi*f_c*time)

product = A_c*np.cos(2.0*pi*f_c*time + modulation_index*np.sin(2*pi*f_m*time))

plt.subplot(3,1,1)
plt.title('Frequency Modulation')
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
plt.xlabel('FM signal')
plt.subplots_adjust(hspace=1)
#plt.savefig("Frequency Modulation.png")

plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16, 9)
#fig.savefig('Frequency Modulation.png', dpi=100)

