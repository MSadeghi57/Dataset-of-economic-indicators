#pip install yfinance pandas beautifulsoup4 requests
import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests
# تعریف تاریخ‌ها
start_date = "2021-01-01"
end_date = "2023-12-31"
# تعریف نمادها
symbols = ["GOLD", "CL=F", "USD"]
# ساخت DataFrame برای ذخیره اطلاعات
df = pd.DataFrame(index=pd.date_range(start=start_date, end=end_date))
# دریافت قیمت سهام با استفاده از yfinance
for symbol in symbols:
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    stock_columns = [f"{symbol}_{col}" for col in ["Open", "Close", "High", "Low", "Volume"]]
    df[stock_columns] = stock_data[["Open", "Close", "High", "Low", "Volume"]]
    # دریافت اخبار اقتصادی با استفاده از google news
    query = f"{symbol} economy"
    url = f"https://news.google.com/rss/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # استخراج عناوین اخبار
    news_titles = [item.text for item in soup.find_all("title")[1:]]  # اولین عنوان مربوط به Feed است
    # افزودن عناوین به DataFrame
    df[f"{symbol}_News"] = pd.Series(news_titles)
# نمایش نتیجه
print(df)