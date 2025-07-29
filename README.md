# -Amazon-Sunblock-Scraper-Analyzer
This project scrapes sunblock product listings from Amazon.eg and analyzes the pricing data to identify the most affordable products. It uses Python with BeautifulSoup for scraping and Matplotlib/Seaborn for data visualization.

-Features
Scrapes multiple pages of Amazon search results for sunblock products

Extracts product titles, prices, and image URLs

Cleans and stores the data in a CSV file

Sorts products by price to identify the top cheapest sunblocks

Generates a bar chart to visualize the most affordable sunblocks

-Requirements
Install the following Python libraries before running the script:

pip install requests beautifulsoup4 pandas matplotlib seaborn

-How It Works
Sends HTTP requests to multiple pages of the sunblock search results.

Parses product info including:
Title
Price (in EGP)
Image URL

Stores the data in a pandas DataFrame.

Cleans and sorts the data by price.

Exports results to a CSV file (amazon_sunblocks.csv).

Displays a bar chart of the top cheapest products.

📊 Sample Output
<img width="842" height="495" alt="image" src="https://github.com/user-attachments/assets/7c07ba91-e66f-47bc-84ed-84ec58dbd8cc" />
<img width="1498" height="827" alt="Screenshot 2025-07-29 152600" src="https://github.com/user-attachments/assets/1625e579-e6ed-44c0-907d-3a9fa0c364b7" />
