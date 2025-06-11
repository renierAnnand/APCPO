import streamlit as st
import matplotlib.pyplot as plt
from utils import load_and_clean_data_from_multiple, forecast_demand

st.set_page_config(page_title="Multi-File Procurement Forecast", layout="centered")

st.title("📦 Smart Procurement Demand Forecasting (Multi-File)")

# Allow multiple CSVs
csv_files = st.file_uploader("Upload one or more structured PO CSV files", type=["csv"], accept_multiple_files=True)

if csv_files:
    st.success(f"{len(csv_files)} files uploaded successfully.")

    # Clean and merge all files
    df = load_and_clean_data_from_multiple(csv_files)

    if not df.empty:
        st.subheader("Merged PO Data Sample")
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

        st.subheader("Forecast Data")
        st.write(forecast)
    else:
        st.warning("No valid data could be extracted from the uploaded files.")
else:
    st.info("Please upload one or more structured CSV files to begin.")
