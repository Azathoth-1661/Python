import pandas as pd

def calculate_ema(data: pd.Series, span: int) -> pd.Series:
    """
    計算指數移動平均（EMA）
    :param data: 股價序列（如收盤價）
    :param span: EMA 的平滑係數
    :return: EMA 序列
    """
    return data.ewm(span=span, adjust=False).mean()