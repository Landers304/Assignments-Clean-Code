#Task 1:


class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")


# Additional functions related to book management
def check_availability(book):
    if book.stock > 0:
        print(f"{book.title} is available.")
    else:
        print(f"{book.title} is out of stock.")
