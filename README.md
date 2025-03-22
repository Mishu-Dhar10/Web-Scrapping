# Web-Scrapping
This project involved scraping and analyzing data from the UK-based toy retailer Wicked Uncle to gain insights into product pricing, customer sentiment, and visual marketing strategies. The aim was to explore how digital data from websites can be leveraged for social science research using computational tools. 
Tools & Technologies Used
Languages: R and Python
Libraries/Packages: rvest, RSelenium, scikit-learn, PIL, ggplot2, stringr, tidyverse
Techniques: Web scraping, sentiment analysis, image color clustering, data cleaning
Main Methods and Steps
• Used R to scrape product names, prices, and customer reviews.
• Switched to Python to download and process product images for color analysis using KMeans clustering (scikit-learn).
• Performed sentiment analysis on customer reviews using text mining and visualization techniques.
• Analyzed product pricing distribution and identified key pricing clusters.
• Explored dominant color trends in product images to examine visual marketing patterns.
Key Findings
• Product Pricing: The price distribution was multimodal, showing strategic segmentation (most products under £20 with pricing peaks at £10 and £20).
• Sentiment Analysis: Customer feedback was overwhelmingly positive, with dominant sentiments being trust, joy, and anticipation. Frequently used words included “great,” “excellent,” and “fast.”
• Color Analysis: Neutral colors like white, snow, and black were the most common in product images, possibly to make the products stand out visually.
Challenges & Limitations
• Initial attempt to scrape a Bangladeshi bookstore failed due to non-English encoding issues (Bengali fonts).
• Limitations in NLP sentiment detection, such as missing sarcasm.
• Color extraction may mislabel tones by assigning nearest RGB matches rather than exact shades.
Ethical Considerations
Although the project used public HTML data, it recognized GDPR implications and the ethical concerns of collecting and using business-related information without direct consent.
![image](https://github.com/user-attachments/assets/e62da12e-9780-4dbe-ad18-29735bc77b58)
