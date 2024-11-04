#Create a class Book with attributes title, author, and pages. Include methods to read and display the book's information.
# Then, create a subclass EBook that adds an attribute file_format and overrides the display method to include the file format.

# class Book:
#     def __init__(self, title, author, pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def read(self):
#         print("i am reading", self.title,"Written By",self.author,"this Book have",self.pages)
#     def disply(self):
#         print("Title: ",self.title)
#         print("Author: ",self.author)
#         print("Pages: ",self.pages)
# class Ebook(Book):
#     def __init__(self, title, author, pages,fileformate):
#         super().__init__(title, author, pages)
#         self.fileformate=fileformate 
#     def display(self):
#         print("Title: ",self.title)
#         print("Author: ",self.author)
#         print("Pages: ",self.pages)
#         print("FileFormate: ",self.fileformate)


# b=Ebook("Python","Sachin",100,'pdf')
# b.display()


# Implement a class BankAccount with methods to deposit, withdraw, and check the balance.
# Ensure that the balance cannot go negative.
# Add a subclass SavingsAccount that has an interest rate and a method to apply interest to the balance.

# class BankAccount:
#     def __init__(self,an,b) -> None:
#         self.an=an
#         self.b=b
#     def deposite(self,ammount):
#         if ammount>0:
#             self.b+=ammount
#             print("Deposited Ammount = ", ammount,"Total Ammount = ",self.b)
#         else:
#             print("Invalid Ammount or Insufficent Balance")
#     def withdraw(self,ammount):
#         if ammount>0:
#             self.b-=ammount
#             print("Withdrawn AMMOUNT = ",ammount,"Remmaining Balance = ",self.b)
#         else:
#             print("Invalid Ammount or Insufficent Balance")
# class SavingsAccount(BankAccount):
#     def __init__(self,an,b,rate = 0.01):
#         super().__init__(an,b)
#         self.rate=rate
#     def apply_interest(self):
#         interest = self.b*self.rate
#         self.b +=interest
#         print("Interest Applied = ",interest,"Total Balance = ",self.b)


# a = SavingsAccount(123123,200000)
# a.deposite(23)
# a.withdraw(1000)
# a.apply_interest()


# Inheritance and Polymorphism
# Design a class hierarchy for a zoo management system, starting with a base class Animal and subclasses Mammal,
# Bird, and Reptile.
# Each subclass should have specific attributes and methods. 
# Demonstrate polymorphism by creating a list of animals and calling a method that is defined in the Animal class but overridden in each subclass.

class Animal:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
class Birds(Animal):
        def __init__(self, name, weight, color, wingspan):
            super().__init__(name, weight, color)
            self.wingspan=wingspan
        def speak(self,speak):
              self.speak =speak
              print(f"{self.name} make sound like",self.speak)
class Reptile(Animal):
        def __init__(self, name,  weight, color, type):
              super().__init__(name, weight, color)
              self.type = type
        def movement(self,move):
              self.move=move
              print(f"{self.name} move",self.move)


animals = [Birds("swan",'30kg',"white",'cm'),
          Reptile('snake','2kg','black','venom')]

for animal in animals:
      print(f'Here is  brd{animal.speak("kaww")} here is reptile {animal.movement("fast")}')
    

# Create a base class Shape with a method area. Derive classes Rectangle, Circle, and Triangle from Shape,
# each with their own implementation of the area method. Write a program that takes a list of shapes and prints the area of each shape.

# Encapsulation
# Write a class Employee with private attributes name, position, and salary. Provide public methods to get and set each attribute, ensuring that the salary cannot be set to a negative value. Demonstrate encapsulation by creating and manipulating Employee objects.
# Create a class SecureVault that uses private attributes to store sensitive information. Include methods to add, retrieve, and delete items, ensuring that only authorized users can perform these actions. Use encapsulation to protect the vault's contents.

# Abstraction
# Design an abstract class Vehicle with abstract methods start_engine and stop_engine. Create subclasses Car and Motorcycle that implement these methods. Write a program that demonstrates creating objects of these subclasses and calling their methods.
# Create an abstract class Account with abstract methods deposit and withdraw. Derive classes CheckingAccount and SavingsAccount that provide implementations for these methods. Demonstrate the use of these classes in a banking application.

# Composition
# Implement a class House that contains rooms. Each room should be an object of a Room class. The House class should have methods to add rooms, remove rooms, and calculate the total area of the house.
# Create a class Library that contains a collection of Book objects. Implement methods to add a book, remove a book, and list all books in the library. Use composition to model the relationship between the library and the books.
# Design Patterns
# Implement the Singleton pattern for a class Logger that logs messages to a file. Ensure that only one instance of the Logger class can exist.
# Design a class structure that uses the Factory pattern to create different types of Animal objects (e.g., Dog, Cat, Bird). The factory class should have a method that takes a string parameter and returns the appropriate Animal object.