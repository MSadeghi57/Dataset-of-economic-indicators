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
    crypto_df = yf.download(crypto_symbol, start="2023-09-10", end="2023-12-19")
    # اضافه کردن ستون close به DataFrame
    crypto_data[crypto_symbol] = crypto_df['Close']
# تغییر شکل ماتریس داده
crypto_data = crypto_data.transpose()
# پر کردن مقادیر مفقود با میانگین
crypto_data = crypto_data.fillna(crypto_data.mean())
# حذف هر ستونی که مقدار NaN دارد
crypto_data = crypto_data.dropna(axis=1)
# اجرای الگوریتم KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(crypto_data)
crypto_data['Cluster'] = clusters
# نمایش نتایج
print(crypto_data)
# نمایش داده‌ها در نمودار
plt.scatter(crypto_data.index, crypto_data['Cluster'], c=crypto_data['Cluster'], cmap='viridis')
plt.xlabel('Cryptocurrencies')
plt.ylabel('Cluster')
plt.title('Cryptocurrency Clustering')
plt.show()