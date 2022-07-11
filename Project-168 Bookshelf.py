class Book:
    def __init__(self,name,author,price,publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishingyear = publishing_year
        
    def add_book(self):
        print("Name : "+self.book_name)
        print("Author : "+self.book_author)
        print("Price : "+str(self.book_price))
        print("Publishing Year : "+str(self.book_publishingyear))
        print("Book added")
        

book1 = Book("Harry Potter and the Philosopher's Stone","J.K Rowling","$1730",1997)
book1.add_book()

book2 = Book("Gulliver's Travels","Jonathan Swift","$1405",1726)
book2.add_book()