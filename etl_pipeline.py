import requests
import pandas as pd

def fetch_crypto_data():
    """Extract: Получение актуальных данных о криптовалютах через публичный REST API CoinGecko."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def transform_data(raw_data):
    """Transform: Очистка, фильтрация и рассчет дополнительных метрик с использованием Pandas."""
    df = pd.DataFrame(raw_data)
    
    # Отбираем только нужные колонки
    selected_columns = ['id', 'name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']
    df = df[selected_columns]
    
    # Рассчитываем соотношение объема торгов к рыночной капитализации
    df['volume_to_market_cap_ratio'] = (df['total_volume'] / df['market_cap']).round(4)
    
    # Округляем цены
    df['current_price'] = df['current_price'].round(2)
    
    # Преобразуем обратно в список словарей для отдачи через API
    return df.to_dict(orient='records')

def run_etl():
    """Запуск полного цикла ETL."""
    raw_data = fetch_crypto_data()
    clean_data = transform_data(raw_data)
    return clean_data