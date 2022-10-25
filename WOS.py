import streamlit as st
from PIL import Image
import pandas as pd

image = Image.open('https://github.com/basbroers/opti/blob/main/Taghleef.png')
GS = ['TSS20','TZZ20']

with st.sidebar:
    st.image(image)
    st.markdown("""# Web Order Services""")
    action = st.sidebar.radio("",['Order Status','Add Order','Modify Order','Confirm Order','Call off','Reprint Documents','Reports','Update Profile','Logout'])

if action == 'Add Order':
    st.markdown("""# Add an new order""")
    colGS, colMinWdith, colminDiam, colMinLen = st.columns([30,20,20,20])

    colMetal, colMaxWdith, colmaxDiam, colMaxLen = st.columns([30,20,20,20])

    with colGS:
        st.selectbox('Available Grade Spec',GS)
    with colMinWdith:
        st.number_input('Min Width (mm)',min_value=10)
    with colminDiam:
        st.number_input('Min Diameter (mm)',min_value=10)
    with colMinLen:
        st.number_input('Min Length (km)',min_value=0)

    with colMetal:
        st.selectbox('Metalized',['Yes','No'])
    with colMaxWdith:
        st.number_input('Max Width (mm)',min_value=10)
    with colmaxDiam:
        st.number_input('Max Diameter (mm)',min_value=10)
    with colMaxLen:
        st.number_input('Max Length (km)',min_value=0)

    order = st.button('Order now')

    if bool(order):
        st.write('Order Successfull')

    df = pd.DataFrame([[24.9959, 55.1064]],columns=['lat','lon'])
    st.map(df)
    
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
##st.markdown(hide_menu_style, unsafe_allow_html=True)

