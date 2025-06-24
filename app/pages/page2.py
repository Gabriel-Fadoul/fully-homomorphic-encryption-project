import streamlit as st
import numpy as np
import pandas as pd

gen_data = pd.DataFrame(np.random.rand(5,5))

col1, col2, col3 = st.columns(3 , border=True)

with col1:
    col1.subheader("User")
    st.dataframe(gen_data)

col3.subheader("Server")