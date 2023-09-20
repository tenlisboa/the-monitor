from lib.money_extractor import MoneyExtractor
from lib.monitor import Monitor
from lib.scrapper import Scrapper

product = {
    'title': 'Macbook Pro m2',
    'price': 5000.00,
    'currency_symbol': 'R$',
    'strictness': 1
}

integrations = [
    {'url': 'https://www.amazon.com.br/s?k=<PRODUCT_TITLE>', 'selector': 'span.a-price,span.a-price-whole'},
    {'url': 'https://www.casasbahia.com.br/<PRODUCT_TITLE>/b', 'selector': 'div.product-card__highlight-price'}
]

extractor = MoneyExtractor()
scrapper = Scrapper(extractor, integrations)
monitor = Monitor(scrapper)

monitor.execute(product)