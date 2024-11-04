# def division(n1 , n2):
#     try:
#         result =  n1/n2
#     except ZeroDivisionError:
#         return "Cannot Divide With A Zero Denominator"
#     else:
#         return result
# print(division(3,0))
# print(division(4,2))
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def talk(self):
#         print(f"Hello, There My Name Is '{self.name}'\nand my age is '{self.age}'")

#     # def greetings(self):
#     #     print(f"Greeting Sir {self.name}")


# class Employe(Person):
#         def __init__(self,name,age,salary):
#             super().__init__(name,age)
#             self.salary=salary
#         def Salary(self):
#              super().Salary()
#              print(f"My Salary is f{self.salary}")
             


# # people = Person("Labeeb Khan",23)
# # people.talk()
# # people.greetings()
# employe_1 = Employe("Labeeb Khan",23,50000)
# employe_1.salary()




# # Rectangle Programme without any OOPS concept simple
# class rectangle:
#     def __init__(self) -> None:
#         self.length = 0
#         self.width = 0
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2*(self.length+self.width)
    

# a=rectangle()
# a.length=5
# a.width=4
# print(a.area())
# print(a.perimeter())




# class vehical:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model

# class car(vehical):
#     def __init__(self, make, model,doors):
#         super().__init__(make, model)
#         self.doors = doors
#     def car_info(self):
#         print(f"Make: {self.make}\nModel: {self.model}\nDoors: {self.doors}")

# class miles(car):
#     def __init__(self, make:str, model:int, doors:int,miles:float):
#         super().__init__(make, model, doors)
#         self.miles = miles
#     def car_full_info(self):
#         print(f"Make: {self.make}\nModel: {self.model}\nDoors: {self.doors}\nMiles: {self.miles}")


# a=miles('Honda',2000,4,43000)
# a.car_full_info()

# def greet(f):
#     def newS():
#         print(f"Hello")
#         f()
#         print("have a great day")
#     return newS
# @greet
# def fun():
#     print("Name")

# fun()

# class Car:
#     def __init__(self,model,year):
#         self.model = model
#         self.year = year
#     def info(self):
#         print(f"Model: {self.model}\nYear: {self.year}")
# class Carupgrade(Car):
#     def __init__(self, model, year, name):
#         super().__init__(model, year)
#         self.name = name
#     def info(self):
#         print(f"Model: {self.model}\nYear: {self.year}\nName: {self.name}")


# car_1 = Carupgrade('XLI',2020,"Toyota")
# print(car_1.info())

# class Student:
#     def __init__(self,name,mark_1,mark_2,mark_3):
#         self.name = name
#         self.mark_1 = mark_1
#         self.mark_2 = mark_2
#         self.mark_3 = mark_3

#     def average(self):
#         print(f"The Average = {self.mark_1+self.mark_2+self.mark_3/3}")


# s1 = Student('Rana',12,33,44)
# s2 = Student('noman',22,33,52)
# s1.average()
# s2.average()



class Account:
    def __init__(self, name:str, balance:float, Account_no:int):
        self.name = name
        self.balance = balance
        self.Account_no = Account_no

    def debit(self):
        print('amount debited = ', self.debit)

    def credit(self):
        print('amount credited = ', self.credit)
    
    def Balance(self):
        print('Balance = ', self.balance)


s1 = Account('zain',2312,1232131)
s2 = Account('sda',23212,421)
s1.Balance()
s2.Balance()
