import person

class Employee(person.Person):
    
    def __init__(self, name, email, salary, address):
        super().__init__(name, email, address)
        self.__salary = salary
        
    def get_salary(self): 
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
        
    def increase_salary(self, percentage): 
        self.__salary += self.__salary * (percentage / 100)
        
    def display_info(self):
        return  (
            f"Ime: {self.name}\n"
            f"Email: {self.get_email()}\n"
            f"Adresa: {self.get_address()}\n"
            f"Plata: {self.get_salary()}"
        )
