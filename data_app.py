import streamlit as st
import pandas as pd

st.title("Data Insights Generator")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Columns")
    st.write(list(df.columns))

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Basic Insights")

    insights = []

    for col in df.select_dtypes(include=['number']).columns:
        avg = df[col].mean()
        insights.append(f"Average of {col}: {avg:.2f}")

    st.write(insights)