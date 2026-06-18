import person
import product

class User(person.Person):
    
    def __init__(self, name, email,  phone, address):
        super().__init__(name, email, address)
        self.phone = phone
        self.shopping_history = []
        
    # Getter for the phone number
    def get_phone(self):
        return self.phone

    # Setter za broj telefona
    def set_phone(self, phone):
        self.phone = phone
        
    def add_product(self, product):
        self.shopping_history.append(product)
        
    def total_spent(self):
        total = 0
        
        for product in self.shopping_history:
            total += product.get_price()

        return total
    
    # Implementacija apstraktne metode
    def display_info(self):
        return (
            f"Ime: {self.name}\n"
            f"Email: {self.get_email()}\n"
            f"Telefon: {self.phone}\n"
            f"Adresa: {self.get_address()}\n"
            f"Broj kupljenih proizvoda: {len(self.shopping_history)}\n"
            f"Ukupno potrošeno: {self.total_spent()}"
        )
        