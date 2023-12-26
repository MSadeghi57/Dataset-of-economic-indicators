import yfinance as yf
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# تعریف لیست ارزها
crypto_list = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD', 'ADA-USD', 'XLM-USD', 'LINK-USD',
               'BNB-USD', 'USDC-USD', 'DOGE-USD', 'WBTC-USD', 'AAVE-USD', 'EOS-USD', 'XTZ-USD','BSV-USD', 
               'CRO-USD', 'NEO-USD', 'XMR-USD', 'VET-USD', 'TRX-USD', 'MKR-USD', 'HT-USD', 'MIOTA-USD',
               'DASH-USD', 'ZEC-USD', 'FTT-USD', 'XEM-USD', 'SNX-USD', 'CEL-USD', 'YFI-USD', 'FTM-USD',
               'NEAR-USD' , 'SOL-USD', 'DAI-USD', 'LEO-USD', 'DOT-USD', 'MATIC-USD','WETH-USD', 'UNI-USD']
# ساخت یک DataFrame با استفاده از pandas
crypto_data = pd.DataFrame()
# برای هر ارز دیجیتال داده‌های مربوط به آن را از یافتن تاریخ فراخوانی کنید.
for crypto_symbol in crypto_list:
    try:
        crypto_df = yf.download(crypto_symbol, start="2023-09-10", end="2023-12-19")
        crypto_data[crypto_symbol] = crypto_df['Close']
    except Exception as e:
        print(f"Failed download: [{crypto_symbol}]: {e}")
# پر کردن مقادیر مفقود با میانگین
crypto_data = crypto_data.transpose().fillna(crypto_data.mean())
# اجرای الگوریتم KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(crypto_data)
crypto_data['Cluster'] = clusters
# نمایش نتایج
print(crypto_data) 

import yfinance as yf
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# 1. لیست اسم ۴۰ ارز دیجیتال را در یک ارایه قرار دهید
crypto_list = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD', 'ADA-USD', 'XLM-USD', 'LINK-USD',
               'BNB-USD', 'USDC-USD', 'DOGE-USD', 'WBTC-USD', 'AAVE-USD', 'EOS-USD', 'XTZ-USD','BSV-USD', 
               'CRO-USD', 'NEO-USD', 'XMR-USD', 'VET-USD', 'TRX-USD', 'MKR-USD', 'HT-USD', 'MIOTA-USD',
               'DASH-USD', 'ZEC-USD', 'FTT-USD', 'XEM-USD', 'SNX-USD', 'CEL-USD', 'YFI-USD', 'FTM-USD',
               'NEAR-USD','XTZ-USD', 'BSV-USD', 'CRO-USD', 'NEO-USD', 'XMR-USD','XLM-USD', 'LINK-USD']
# 2. داده‌های close صد روز اخیر هر ارز را بگیرید
crypto_data = yf.download(crypto_list, start="2023-09-10", end="2023-12-18")['Close']
# 3. هر ارز بعنوان ایندکس قرار بگیرد و هر روز بعنوان یک فیچر
crypto_data = crypto_data.transpose()
# 4. ارز‌ها را با kmeans به سه کلاستر تقسیم کنید
kmeans = KMeans(n_clusters=3, random_state=42)
crypto_data['Cluster'] = kmeans.fit_predict(crypto_data)
# نمایش نتایج
print(crypto_data)
