import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_data (1).csv")

st.set_page_config(page_title="Home", page_icon="🍻",layout="wide")
st.title("🥂Cheers to pour decisions🥂")
st.subheader("✨Welcome ✨")
st.header("Details:-")
total_pubs= len(df['fsa_id'].unique())
total_localAuthority= len(df['local_authority'].unique())
total_postalCodes= len(df['postcode'].unique())
st.subheader(f"Total pub present in United Kingdom is {total_pubs}")
st.subheader(f"Total local authorities of pubs is {total_localAuthority}")
st.subheader(f"Total postal codes of pubs present in UK is {total_postalCodes}")
