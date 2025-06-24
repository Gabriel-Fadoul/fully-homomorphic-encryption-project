import streamlit as st
import random as rand
import pandas as pd
import numpy as np
import tenseal as ts
from time import time 
rand.seed(0)

st.title("Fully Homomorphic Encryption (FHE) - Statistics Project")

if 'L' not in st.session_state:
    st.session_state['L'] = 'value'
    st.session_state['aux'] = 'value'
    
if 'sum_clicked' not in st.session_state:
    st.session_state['sum_clicked'] = False

if 'mult_clicked' not in st.session_state:
    st.session_state['mult_clicked'] = False    

context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)

#size = st.slider("Defina o tamanho do vetor de Dados", 0, 100000, 1000)

size = st.number_input("Defina o tamanho do vetor de Dados",value=100)

if st.button("Generate", type='primary'):
    L = [rand.randint(0,100000) for _ in range(size)]
    aux = [rand.randint(0,100000) for _ in range(size)]
    st.dataframe(pd.DataFrame(L))
    st.session_state['L'] = L
    st.session_state['aux'] = aux
    st.session_state['sum_clicked'] = False
    st.session_state['mult_clicked'] = False

st.header("Operações")
st.subheader("Soma")
col1, col2 = st.columns(2 , border=True)
with col1:
    st.markdown("### Com FHE")
    st.markdown('''
                    ``` 
                        encv = ts.bfv_vector(context, vector)
                        result = encv + aux
                        
                    ```
                ''')
    #if st.button("Execute", type='primary',  key='sum_fhe'):
    if st.session_state.sum_clicked:
        t_start = time()
        encv = ts.bfv_vector(context, st.session_state.L)
        result = encv + st.session_state.aux
        t_end = time()
        st.markdown("*BFV c2p sum time*: {} ms".format((t_end - t_start) * 1000))

with col2:
    st.markdown("### Sem FHE")
    if st.session_state.sum_clicked:
        t_start = time()
        D = [ (a + b) for a, b in zip(st.session_state.L, st.session_state.aux)]
        t_end = time()
        st.markdown("*Commom sum time*: {} ms".format((t_end - t_start) * 1000))
    
if st.button("Execute", type='primary', key='sum'):
    st.session_state['sum_clicked'] = True

st.subheader("Multiplicação")
col3, col4 = st.columns(2 , border=True)
with col3:
    st.markdown("### Com FHE")
    st.markdown('''
                    ``` 
                        encv = ts.bfv_vector(context, vector)
                        result = encv * aux
                        
                    ```
                ''')
    #if st.button("Execute", type='primary',  key='sum_fhe'):
    if st.session_state.mult_clicked:
        t_start = time()
        encv = ts.bfv_vector(context, st.session_state.L)
        result = encv * st.session_state.aux
        t_end = time()
        st.markdown("*BFV c2p mult time*: {} ms".format((t_end - t_start) * 1000))

with col4:
    st.markdown("### Sem FHE")
    if st.session_state.mult_clicked:
        t_start = time()
        np.array(st.session_state.L).dot(np.array(st.session_state.aux))
        t_end = time()
        st.markdown("*Commom sum time*: {} ms".format((t_end - t_start) * 1000))
    
if st.button("Execute", type='primary', key='mult'):
    st.session_state['mult_clicked'] = True
        