import requests
import constants

def get_latest_updates(symbol):
    iex_api_key = constants.API_KEY
    iex_api_url = constants.API_URL_BASE
    api_url = f"{iex_api_url}/stock/{symbol}/batch?types=chart&range=1m&last=10&token={iex_api_key}&filter=close,volume,date,label,change,changePercent"
    return requests.get(api_url).json()['chart']
