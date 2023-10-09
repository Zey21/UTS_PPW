import streamlit as st
import pandas as pd
import numpy as np

st.header("UTS PPW")
st.subheader("Mengambil Data CSV pada Github")
st.write("**pada repo Zey21/dataset/**")
st.text("load data")

##Load data
df = pd.read_csv('https://raw.githubusercontent.com/Zey21/dataset/main/DataSteaming.csv')
out_df = df.head()
st.text(out_df)
