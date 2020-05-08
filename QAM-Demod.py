import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np
from scipy.signal import butter,filtfilt
import matplotlib.pyplot as plt

# Butterworth Lowpass Filter
def butter_lowpass_filter(data, cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

st.title('QAM Demodulation')
st.text('Nabanita Sarkar')

A_m = st.sidebar.slider('Message Amplitude', 0, 10, 5)
f_m1 = st.sidebar.slider('Message1 Frequency', 0.0, 5.0, 2.0)
f_m2 = st.sidebar.slider('Message2 Frequency', 0.0, 10.0, 8.0)
A_c = st.sidebar.slider('Carrier Amplitude', 0, 10, 5)
f_c = st.sidebar.slider('Carrier Frequency', 0, 100, 80)
modulation_index = st.sidebar.slider('Modulation Index', 0.0, 1.0, 0.5)

t = np.linspace(0, 1, 1000)
c_t = np.linspace(0, 1, 500)

carrier = A_c*np.cos(2*np.pi*f_c*t)
carrier2 = A_c*np.sin(2*np.pi*f_c*t)
message1 = A_m*np.sin(2*np.pi*f_m1*t)
message2 = A_m*np.sin(2*np.pi*f_m2*t)
p1 = message1*carrier
p2 = message2*carrier2
product = p1 + p2

r1_message = butter_lowpass_filter(product*carrier,8.0,1000,2)
r2_message = butter_lowpass_filter(product*carrier2,8.0,1000,2)

f = make_subplots(rows=4, cols=1)


f.add_trace(
    go.Line(x=c_t, y=product, name="Generated QAM"), row=1, col=1
)


f.add_trace(
    go.Line(x=c_t, y=carrier, name="Locally Generated Carrier"), row=2, col=1
)

f.add_trace(
    go.Line(x=t, y=r1_message, name="Recovered Message 1"), row=3, col=1
)

f.add_trace(
    go.Line(x=t, y=r2_message, name="Recovered Message 2"), row=4, col=1
)
f.update_layout(width=800, height=600)

st.plotly_chart(f)
