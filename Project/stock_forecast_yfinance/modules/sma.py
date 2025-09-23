import pandas as pd

def calculate_sma(data: pd.Series, window: int) -> pd.Series:
    """
    計算簡單移動平均（SMA）
    :param data: 股價序列（如收盤價）
    :param window: 移動平均窗口大小
    :return: SMA 序列
    """
    return data.rolling(window=window).mean()