import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def load_data(filepath):
    return pd.read_csv(filepath)

def get_summary_stats(df):
    return df[["GHI", "DNI", "DHI"]].describe()

def plot_ghi_boxplot(df, country):
    fig = px.box(df, y="GHI", title=f"GHI Boxplot - {country}", points="all")
    return fig

def get_top_ghi_by_day(df, top_n=5):
    # Ensure time is datetime
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # Extract just the date (drop time part)
    df["Date"] = df["Timestamp"].dt.date

    # Group by date and calculate average GHI
    daily_avg = df.groupby("Date")["GHI"].mean().reset_index()

    # Sort descending and get top N
    top_days = daily_avg.sort_values(by="GHI", ascending=False).head(top_n)

    # Optional: rename columns for display
    top_days.columns = ["Date", "Average GHI (W/m²)"]

    return top_days


