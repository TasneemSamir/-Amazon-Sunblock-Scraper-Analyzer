import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time
import re
import matplotlib.pyplot as plt
import seaborn as sns
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

}

url_base='https://www.amazon.eg/-/en/s?k=sunblock&crid=1EL5864DHYMCW&qid=1753780644&sprefix=sunbli%2Caps%2C142&xpid=BDOM06GtwEqvu&ref=sr_pg_{}'

data=[]
for page in range(1,4):
    url=url_base.format(page)
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,"html.parser")

    time.sleep(4)
    products=soup.find_all("div", {"data-component-type": "s-search-result"})

    for product in products:
        title_tag=product.find('h2')
        title=title_tag.get_text(strip=True) if title_tag else None

        image=product.find("img",class_="s-image")
        image_url=image["src"] if image else None

        price_tag=product.find('span',class_="a-price")

        if price_tag:
            price_text=price_tag.find("span",class_='a-offscreen')
            if price_text:
                price=price_text.get_text(strip=True)
                cleaned_price =float(re.sub(r'[^\d.]', '',price))
            else:
                cleaned_price=None
        else:
            cleaned_price=None
        if title and cleaned_price is not None:  
            data.append({
            'title':title,
            'price_EGP':cleaned_price,
            'image_url':image_url
        })


df=pd.DataFrame(data)

print(df.columns)
print(df.head())
sorted_df=df.sort_values(by='price_EGP')
sorted_df.to_csv("amazon_sunblocks.csv",index=False)

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")

top_products=sorted_df.head(20)
sns.barplot(x="price_EGP",y="title",data=top_products)

plt.title("Top Cheapest Sunblocks on Amazon.eg", fontsize=16)
plt.xlabel("Price (EGP)")
plt.ylabel("Product Title")

plt.tight_layout()
plt.show()
