import pandas as pd

def calculate_macd(data: pd.Series) -> pd.DataFrame:
    """
    計算 MACD 指標與交叉訊號
    :param data: 股價序列（如收盤價）
    :return: 包含 MACD 線、Signal 線與交叉訊號的 DataFrame
    """
    ema_fast = data.ewm(span=12, adjust=False).mean()
    ema_slow = data.ewm(span=26, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    crossover = macd_line - signal_line

    df = pd.DataFrame({
        'MACD': macd_line,
        'Signal': signal_line,
        'Crossover': crossover
    })
    return df