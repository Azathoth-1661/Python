import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

def prepare_data(df):
    df['ds'] = pd.to_datetime(df['date'])
    df['y'] = df['order_count']
    return df[['ds', 'y']]

def train_prophet(df, holidays_df=None):
    model = Prophet(holidays=holidays_df) if holidays_df is not None else Prophet()
    model.fit(df)
    return model

def forecast_and_plot(model, periods=60):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    fig = model.plot(forecast)
    plt.title('Prophet 預測結果', fontsize=18)
    plt.xlabel('日期')
    plt.ylabel('預測訂單數')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return forecast