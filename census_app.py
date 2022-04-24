import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
@st.cache()
def load_data():
    df = pd.read_csv("adult.csv", header=None)
    df.head()
    column_name = ['age', 'workclass', 'fnlwgt', 'education', 'education-years',
                   'marital-status', 'occupation', 'relationship', 'race', 'gender',
                   'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    for i in range(df.shape[1]):
        df.rename(columns={i:column_name[i]},inplace=True)
    df.head()
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
census_df = load_data()

st.title("Census App")
if st.checkbox("Display DataFrame"):
    st.subheader("Census Data Set")
    st.dataframe(data = census_df)
    st.markdown(f"Number of Rows: {census_df.shape[0]}, Number of columns: {census_df.shape[1]}")
