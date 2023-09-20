import re

class MoneyExtractor():
    def __init__(self):
        self.brl_pattern = r'R\$\s?(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)'
    
    def execute(self, text_value, currency = 'BRL'):
        if currency == 'BRL':
            return self.extract_brl_value(text_value)
    
    def extract_brl_value(self, text_value):
        match = re.search(self.brl_pattern, text_value)
        if match:
            value = match.group(1).replace('.', '').replace(',', '.')
            
            return float(value)
        else:
            return None  