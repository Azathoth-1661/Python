import pandas as pd
import matplotlib.pyplot as plt

def rolling_baseline(df, window=7):
    df['yhat_baseline'] = df['order_count'].rolling(window=window).mean()
    return df.dropna(subset=['yhat_baseline'])

def evaluate_baseline(df):
    df['error'] = df['order_count'] - df['yhat_baseline']
    df['abs_error'] = df['error'].abs()
    df['ape'] = df['abs_error'] / df['order_count']
    mape = df['ape'].mean()
    rmse = (df['error'] ** 2).mean() ** 0.5
    return mape, rmse

def plot_baseline(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['order_count'], label='實際值', color='steelblue')
    plt.plot(df['date'], df['yhat_baseline'], label='Baseline 預測', color='green')
    plt.title('Baseline 模型預測結果')
    plt.xlabel('日期')
    plt.ylabel('訂單數')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()