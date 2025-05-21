import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, plot_ghi_boxplot, get_summary_stats,get_top_ghi_by_day
# from app.utils import load_data, plot_ghi_boxplot, get_summary_stats

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("Solar Data Dashboard")
selected_country = st.selectbox("Select Country", ["Benin", "Togo", "Sierraleone"])

if selected_country == "Benin":
    path = "../data/benin_cleaned.csv"
elif selected_country == "Togo":
    path = "../data/togo_cleaned.csv"
else:
    path = "../data/sierraleone_cleaned.csv"

df = load_data(path)

st.subheader("Summary Statistics")
st.dataframe(get_summary_stats(df))

st.subheader("GHI Distribution")
fig = plot_ghi_boxplot(df, selected_country)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 5 Days with Highest Average GHI")
top_days_df = get_top_ghi_by_day(df, top_n=5)
st.dataframe(top_days_df)

