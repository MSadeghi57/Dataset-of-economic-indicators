import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests
# تابع برای دریافت قیمت سهم
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data["Close"]
# تابع برای دریافت اخبار اقتصادی
def get_news_titles(symbol):
    query = f"{symbol} economy"
    url = f"https://news.google.com/rss/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # استخراج عناوین اخبار
    news_titles = [item.text for item in soup.find_all("title")[1:]]  # اولین عنوان مربوط به Feed است
    return news_titles
# تعیین تاریخ‌های مورد نظر
start_date = "2021-01-01"
end_date = "2023-12-31"
# تعیین نمادها (symbols)
symbols = ["GOLD", "CL=F", "^USD"]
# ساخت DataFrame برای ذخیره اطلاعات
df = pd.DataFrame(index=pd.date_range(start=start_date, end=end_date))
# دریافت قیمت سهام و اخبار با استفاده از توابع تعریف شده
for symbol in symbols:
    # دریافت قیمت سهم و افزودن به DataFrame
    df[f"{symbol}_Close"] = get_stock_data(symbol, start_date, end_date)
    # دریافت اخبار و افزودن به DataFrame
    df[f"{symbol}_News"] = get_news_titles(symbol)

# نمایش نتیجه
print(df)


#pip install yfinance pandas beautifulsoup4 requests
import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests
# تعیین تاریخ‌های مورد نظر
start_date = "2021-01-01"
end_date = "2023-12-31"
# تعیین نمادها (symbols)
symbols = ["GOLD", "CL=F", "USD"]
# ساخت DataFrame برای ذخیره اطلاعات
df = pd.DataFrame(index=pd.date_range(start=start_date, end=end_date))
# دریافت قیمت سهام با استفاده از yfinance
for symbol in symbols:
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    df[f"{symbol}_(Open)"] = stock_data["Open"]
    df[f"{symbol}_(Close)"] = stock_data["Close"]
    df[f"{symbol}_(High)"] = stock_data["High"]
    df[f"{symbol}_(Low)"] = stock_data["Low"]
    df[f"{symbol}_(Volume)"] = stock_data["Volume"]
    # دریافت اخبار اقتصادی با استفاده از google news
for symbol in symbols:
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