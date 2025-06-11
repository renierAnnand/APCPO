import streamlit as st
import matplotlib.pyplot as plt
from utils import load_and_clean_data, forecast_demand

st.set_page_config(page_title="Demand Forecasting App", layout="centered")

st.title("📦 Smart Procurement Demand Forecasting")
csv_file = st.file_uploader("Upload your structured PO CSV file", type=["csv"])

if csv_file:
    st.success("File uploaded successfully.")
    
    # Load and display raw data
    df = load_and_clean_data(csv_file)
    st.subheader("Cleaned PO Data Sample")
    st.dataframe(df.head())

    # Forecast
    st.subheader("Forecasted Demand")
    ts, forecast = forecast_demand(df)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ts.plot(label="Historical Demand", ax=ax)
    forecast.plot(label="Forecasted Demand", linestyle="--", ax=ax)
    ax.set_title("30-Day Demand Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Quantity")
    ax.legend()
    st.pyplot(fig)

    # Show data
    st.subheader("Forecast Data")
    st.write(forecast)
else:
    st.info("Please upload a structured CSV file to begin.")
