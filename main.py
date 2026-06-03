from product import Product
from employee import Employee
from user import User

# =========================
# KREIRANJE PROIZVODA
# =========================
products = [
    Product("Laptop", 1200.0, 15, "Gaming laptop"),
    Product("Mouse", 25.0, 100, "Wireless mouse"),
    Product("Keyboard", 80.0, 50, "Mechanical keyboard"),
    Product("Monitor", 300.0, 8, "27-inch monitor"),
    Product("USB Cable", 10.0, 200, "USB-C cable")
]


# =========================
# KREIRANJE ZAPOSLENIH
# =========================
employees = [
    Employee(
        "Marko Marković",
        "marko@gmail.com",
        80000,
        "Beograd"
    ),
    Employee(
        "Jelena Jovanović",
        "jelena@gmail.com",
        90000,
        "Novi Sad"
    )
]

# =========================
# KREIRANJE KORISNIKA
# =========================
users = [
    User(
        "Petar Petrović",
        "petar@gmail.com",
        "061111111",
        "Niš"
    ),
    User(
        "Ana Anić",
        "ana@gmail.com",
        "062222222",
        "Kragujevac"
    ),
    User(
        "Nikola Nikolić",
        "nikola@gmail.com",
        "063333333",
        "Subotica"
    )
]

# =========================
# DODAVANJE PROIZVODA KORISNICIMA
# =========================
users[0].add_product(products[0])  # Laptop
users[0].add_product(products[1])  # Mouse

users[1].add_product(products[2])  # Keyboard
users[1].add_product(products[3])  # Monitor

users[2].add_product(products[1])  # Mouse
users[2].add_product(products[4])  # USB Cable


# =========================
# UKUPNO POTROŠENO
# =========================
print("=== UKUPNO POTROŠENO ===")

for user in users:
    print(f"{user.name}: {user.total_spent()} RSD")
    
# =========================
# DEMONSTRACIJA ENKAPSULACIJE
# =========================
print("\n=== ENKAPSULACIJA ===")

# Pristup privatnoj ceni preko getter-a
print(f"Stara cena laptopa: {products[0].get_price()}")

# Izmena cene preko setter-a
products[0].set_price(1350.0)

print(f"Nova cena laptopa: {products[0].get_price()}")

# Pristup privatnoj plati preko getter-a
print(f"\nPlata zaposlenog: {employees[0].get_salary()}")

# Izmena plate preko setter-a
employees[0].set_salary(85000)

print(f"Nova plata zaposlenog: {employees[0].get_salary()}")


# Povećanje plate
employees[0].increase_salary(10)

print(
    f"Plata nakon povećanja od 10%: "
    f"{employees[0].get_salary()}"
)

# =========================
# PROVERA STANJA PROIZVODA
# =========================
print("\n=== STANJE ZALIHA ===")

for product in products:
    print(
        f"{product.name}: "
        f"{'Dovoljno na stanju' if product.check_quantity() else 'Nedovoljno na stanju'}"
    )
    
# =========================
# POLIMORFIZAM
# =========================
print("\n=== POLIMORFIZAM ===")

people = employees + users

for person in people:
    print("\n----------------")
    print(person.display_info())