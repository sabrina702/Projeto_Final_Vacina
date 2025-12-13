# app.py
import streamlit as st
import geopandas as gpd 

st.set_page_config(layout="wide") 

st.title("✅ GeoPandas e Streamlit prontos na nuvem!")
st.write("Agora você pode copiar e colar seu código de mapa e ranking neste arquivo.")
st.write(f"Versão do GeoPandas (Verificação): {gpd.__version__}")

if st.button('Próximo Passo'):
    st.success('O ambiente Codespaces está funcionando perfeitamente!')
