from lib.book import Book

def test_a_book_construct():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'
    
def test_compare_identical_books():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book1 == book2

def test_format_books():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book) == "1 - Nineteen Eighty-Four - George Orwell"
