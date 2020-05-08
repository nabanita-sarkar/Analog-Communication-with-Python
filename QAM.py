import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('QAM Modulation')

A_m = st.sidebar.slider('Message Amplitude', 0, 10, 5)
f_m1 = st.sidebar.slider('Message1 Frequency', 0.0, 5.0, 2.0)
f_m2 = st.sidebar.slider('Message2 Frequency', 0.0, 10.0, 8.0)
A_c = st.sidebar.slider('Carrier Amplitude', 0, 10, 5)
f_c = st.sidebar.slider('Carrier Frequency', 0, 100, 80)
modulation_index = st.sidebar.slider('Modulation Index', 0.0, 1.0, 0.5)

t = np.linspace(0, 1, 1000)


carrier = A_c*np.cos(2*np.pi*f_c*t)
carrier2 = A_c*np.sin(2*np.pi*f_c*t)
message1 = A_m*np.sin(2*np.pi*f_m1*t)
message2 = A_m*np.sin(2*np.pi*f_m2*t)
p1 = message1*carrier
p2 = message2*carrier2
product = p1 + p2

f = make_subplots(rows=4, cols=1)
f.add_trace(
    go.Line(x=t, y=message1), row=1, col=1
)

f.add_trace(
    go.Line(x=t, y=message2), row=2, col=1
)

f.add_trace(
    go.Line(x=t, y=carrier), row=3, col=1
)

f.add_trace(
    go.Line(x=t, y=product), row=4, col=1
)
st.plotly_chart(f)
