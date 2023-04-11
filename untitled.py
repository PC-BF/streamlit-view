import streamlit as st
import pandas as pd

st.write('# youtube view')
st.write('raw')
view = [100,30,150]

view

st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview