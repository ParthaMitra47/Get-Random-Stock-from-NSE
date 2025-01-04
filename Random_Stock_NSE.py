import requests
def get_stocks():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response= requests.get(url)
    data= response.json()

    if data["success"] and "data" in data:
        stock_name= data["data"]["Name"]
        market_Cap= data["data"]["MarketCap"]
        current_Price= data["data"]["CurrentPrice"]
        roe= data["data"]["ROE"] 
        return stock_name, market_Cap, current_Price, roe
    else:
        raise Exception("Failed to load data")

def main():
    try:
        stock_name, market_Cap, current_Price, roe=get_stocks()
        print(f" 1. Stock Name: {stock_name}")
        print(f" 2. Market Cap: {market_Cap}")
        print(f" 3. Current Price: {current_Price}")
        print(f" 4. ROE: {roe}")
    except Exception as e:
        print(str(e))
    


if __name__ == "__main__":
     main()
