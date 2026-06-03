class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name              # public
        self.__price = price          # private
        self.quantity = quantity      # public
        self._description = description  # protected

    # Getter za cenu
    def get_price(self):
        return self.__price

    # Setter za cenu
    def set_price(self, price):
        self.__price = price

    # Getter za opis
    def get_description(self):
        return self._description
    
    # Setter za opis
    def set_description(self, description):
        self._description = description

    # Provera količine na stanju
    def check_quantity(self):
        return self.quantity >= 10
    
