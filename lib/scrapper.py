from bs4 import BeautifulSoup
import time
from selenium import webdriver
import re

class Scrapper():
    def __init__(self, extractor, integrations):
        self.extractor = extractor
        self.integrations = integrations
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
    
    def _has_title_in_text(self, title, text):
        title_list = title.lower().split()
        pattern = '|'.join(title_list)
        match = re.findall(pattern, text, flags=re.IGNORECASE)
        return bool(match)
        
    def execute(self, product):
        title = product['title']
        prices_list = []

        for integration in self.integrations:
            url = integration['url'].replace('<PRODUCT_TITLE>', title)
            self.driver.get(url)
            time.sleep(3)
            
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            selected_tags = soup.select(integration['selector'])
            
            if not selected_tags:
                continue

            prices = [self.extractor.execute(tag.get_text()) for tag in selected_tags]
            filtered_prices = list(filter(lambda price: bool(price), prices))
            first_ten_prices = filtered_prices[:10]

            prices_list.extend(first_ten_prices)
                    
        self.driver.quit()
        return prices_list