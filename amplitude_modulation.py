import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Amplitude Modulation')

A_m = st.sidebar.slider('Modulator Amplitude', 0, 10, 5)
f_m = st.sidebar.slider('Modulator Frequency', 0.0, 5.0, 1.5)
A_c = st.sidebar.slider('Carrier Amplitude', 0, 10, 5)
f_c = st.sidebar.slider('Carrier Frequency', 0, 100, 80)
modulation_index = st.sidebar.slider('Modulation Index', 0.0, 1.0, 0.5)

t = np.linspace(0, 1, 1000)
carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)
product = A_c*(1+modulation_index*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)

f = make_subplots(rows=3, cols=1)
f.add_trace(
    go.Line(x=t, y=modulator), row=1, col=1
)

f.add_trace(
    go.Line(x=t, y=carrier), row=2, col=1
)

f.add_trace(
    go.Line(x=t, y=product), row=3, col=1
)
st.plotly_chart(f)
