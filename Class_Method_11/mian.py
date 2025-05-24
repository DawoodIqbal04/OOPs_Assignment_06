
class Book:
    total_books = 0
    
    def __init__(self, book_name):
        self.book_name = book_name
        print(f'Book {self.book_name} added.')
    
    @classmethod
    def increment_book_count(self):
        Book.total_books += 1
        print(f'Total number of books are {self.total_books}')
        
book1 = Book('Rich Dad Poor Dad')
book1.increment_book_count()

book2 = Book('Atomic Habits')
book2.increment_book_count()
        

        