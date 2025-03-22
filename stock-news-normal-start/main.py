import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
Stock_Api_Key = "IU4QKRIRHNP2U4B1"
News_Api_Key = "0174b27f58424e818ef0db9799840332"
stock_parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":Stock_Api_Key
}
response = requests.get(STOCK_ENDPOINT,params=stock_parameter)
news_parameters={
    "apiKey":News_Api_Key,
    "qInTitle":COMPANY_NAME,
}

data = response.json()["Time Series (Daily)"]
data_list = [value for(key,value)in data.items()]
yesterday_stock = data_list[0]
yesterday_closing = yesterday_stock["4. close"]
print(yesterday_closing)
day_before = data_list[1]
day_closing = day_before["4. close"]
print(day_closing)


difference = abs(float(yesterday_closing)-float(day_closing))
print(difference)


percentage = (difference/float(yesterday_closing))*100
print(percentage)

if percentage>1:
    new = requests.get(NEWS_ENDPOINT,params=news_parameters)
    articles = new.json()["articles"]
    #print(articles)

    three_articles = articles[:3]
    #print(three_articles)

    formatted_articles =[f"Headline :{articles["title"]}. \nBrief : {articles["description"]}" for articles in three_articles]
    print(formatted_articles)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login("pknath759@gmail.com", "cvfi tjim wbse frpy")  # Log in to the email account
        server.sendmail("pknath759@gmail.com", "pknath761@gmail.com", formatted_articles)
        print("Email sent successfully!")
   