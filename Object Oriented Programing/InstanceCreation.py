
'''
    In this program we created a Class and it's instance.
    We Initialized class construtor while creating an instance.
    Validated the types of arrguments passed to the constructor
'''
class Book:
    #defining class constructor using __init__ method
    def __init__(self,name: str,author: str,price:float, quantity:int):
        self.name = name 
        self.author = author
        self.price = price
        self.quantity = quantity
    #Calculates the total price of books purchased
    def total_price(self):
        return self.price * self.quantity
#Creating Instance of book class
book1 = Book('Rich Dad Poor Dad','Robert Kiyosaki ',345,4)

#Creating Instance of book class
book2 = Book('I\'m Hungry ','Me',400,4)

#Printing the Instance values 
print(book1.name,book1.author,book1.price ,end='\n')
print(f'Total price for {book1.quantity}  books is {book1.total_price()}')
print(book2.name,book2.author,book2.price ,end='\n')
print(f'Total price for {book2.quantity}  books is {book2.total_price()}')