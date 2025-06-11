import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path, header=2)
    df = df[["Po Number", "W/H", "Open PO Qty W/H", "Price In SAR", "Total In SAR"]].copy()
    df.columns = ["Po Number", "Warehouse", "Quantity", "Unit Price (SAR)", "Total Price (SAR)"]

    df.dropna(inplace=True)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Unit Price (SAR)"] = pd.to_numeric(df["Unit Price (SAR)"], errors="coerce")
    df["Total Price (SAR)"] = pd.to_numeric(df["Total Price (SAR)"], errors="coerce")
    df.dropna(inplace=True)

    # Simulate dates (or replace with actual if available)
    df["Date"] = pd.date_range(start="2024-01-01", periods=len(df), freq="D")

    return df

def forecast_demand(df, periods=30):
    ts = df.groupby("Date")["Quantity"].sum()
    model = ExponentialSmoothing(ts, trend="add", seasonal="add", seasonal_periods=7)
    fit = model.fit()
    forecast = fit.forecast(periods)
    return ts, forecast
