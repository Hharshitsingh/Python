import requests
import datetime as dt
import html
import twilio
from twilio.rest import Client
# info for stock api
STOCK_NAME = "TSLA"
STOCK_APIKEY = ""
STOCK_TIME = "TIME_SERIES_DAILY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stoks_params = {
    "function": STOCK_TIME,
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY,
}

# info for news api
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = ""
news_params = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API
}


def stock_up_down(yes, dbyes, per):
    if dbyes > yes:
        return f"Stock Decreaed 🔻 {per}%"
    else:
        return f"Stock Increased 🔼 {per}%"


today_date = dt.datetime.now().day

stocks_response = requests.get(STOCK_ENDPOINT, stoks_params)
stocks_response.raise_for_status()
stock_data = stocks_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
print(stock_data_list[0])
yesterday_clos_stock = float(stock_data_list[0]["4. close"])
print(yesterday_clos_stock)
day_yesterday_clos_stock = float(stock_data_list[1]["4. close"])
print(day_yesterday_clos_stock)
diffrence = abs(yesterday_clos_stock-day_yesterday_clos_stock)
diff_percentage = round((diffrence/yesterday_clos_stock)*100)
print(diff_percentage)
if diff_percentage == 0:
    stock_anles = stock_up_down(
        yesterday_clos_stock, day_yesterday_clos_stock, diff_percentage)
    print(stock_anles)

    news_response = requests.get(NEWS_ENDPOINT, news_params)
    articles = news_response.json()["articles"][:3]
    # print(articles)
    formatted_articles = ''.join(
        [f"Headline: {html.unescape(article['title'])}. \nBrief: {html.unescape(article['description'])}\n" for article in articles])
    print(formatted_articles)

    account_sid = ""
    acoount_token = ""
    client = Client(account_sid, acoount_token)
    message = client.messages \
                    .create(
                        body=f"{stock_anles}\n{formatted_articles}",
                        from_='',
                        to=''
                    )
    print(message.sid)


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
