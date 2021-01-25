print("Task N 1")

class Person():

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, yr_of_study, GPA):
        super().__init__(name, age, gender)
        self.yr_of_study = yr_of_study
        self.GPA = GPA

stud_1 = Student("Susan", 21, "female", 2, 4.5)
stud_2 = Student("Mike", 22, "male", 3, 4.5)

print(stud_2.GPA)



print("Task N2")

class Country():
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def description(self):
        return f"Country's name is {self.name} and it is in {self.continent}"  # stex arajin Country's i poxaren grel ei {self} ira hascen er veradardzrel, vonc piti grem vor instance i anuny veradardzni?

country_1 = Country("Armenia", "Europe")
print(country_1.description()) 


class Brand():
    def __init__(self, business_name, business_start_date):
        self.business_name = business_name
        self.business_start_date = business_start_date

    def presentation(self):
        return f"This is {self.business_name} and it was established in {self.business_start_date}"



class Season():
    def __init__(self, season_name, average_temperature):
        self.season_name = season_name
        self.average_temperature = average_temperature

    def presentation(self):
        return f"This is {self.season_name} and it's average temperature is {self.average_temperature}"


class Product(Country, Brand, Season):
    def __init__(self, name, continent, business_name, business_start_date, season_name, average_temperature, product_name, product_type, product_price, product_quantity):
        Country.__init__(self, name, continent)
        Brand.__init__(self, business_name, business_start_date)
        Season.__init__(self, season_name, average_temperature)
        self.product_name =  product_name
        self.product_type = product_type 
        self.product_price = product_price
        self.product_quantity = product_quantity

    def presentation(self):
        return f"This is {self.product_name}, it's type is {self.product_type}, it's price is {self.product_price} and it's quantity is {self.product_quantity}"

    def discount(self, percent):
        return self.product_price - self.product_price / 100 * percent 

    def increase_quantity(self, amount):
        return self.product_quantity + amount 

product_1 = Product("Switzerland", "Europe", "Milka", 1966, "fall", 15, "chocolate", "sweets", 2, 1)

print(product_1.discount(30))
print(product_1.increase_quantity(2))
print(product_1.presentation())