import streamlit as st
import pandas as pd
import numpy as np

st.title("Interactive Data Visualization")
data = np.random.randn(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
st.line_chart(df)
