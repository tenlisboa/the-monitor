
import numpy as np

class Monitor():
    def __init__(self, scrapper):
        self.scrapper = scrapper
        
    def execute(self, product):
        prices_on_market = self.scrapper.execute(product)
        is_in_margin = self.is_price_within_margin(prices=prices_on_market, price_to_check=product['price'], margin=product['strictness'])
        
        if is_in_margin:
            print('Está na margem')
        else:
            print('Não está na margem')
        
    def is_price_within_margin(self, prices, price_to_check, margin=1):
        if not prices:
            print("A lista de produtos está vazia.")
            return False

        # Calcula a média e o desvio padrão dos preços
        avg_price = np.mean(prices)
        std_dev = np.std(prices)

        # Calcula o Z-score do preço a ser verificado
        z_score = (price_to_check - avg_price) / std_dev

        # Verifica se o Z-score está dentro da margem de erro
        if abs(z_score) <= margin:
            print(f"O preço R${price_to_check:.2f} está dentro da margem de erro.")
            return True
        else:
            print(f"O preço R${price_to_check:.2f} está fora da margem de erro.")
            return False