from lib.book import Book
from lib.book_repository import BookRepository

#return list of all books

def test_get_all_books(db_connection):
    db_connection.seed('seeds/book_store.sql')
    book_repository = BookRepository(db_connection)
    books = book_repository.all()
    assert books == [Book(1, 'Nineteen Eighty-Four', 'George Orwell'), Book(2, 'Mrs Dalloway', 'Virginia Woolf'), Book(3, 'Emma', 'Jane Austen'), Book(4, 'Dracula', 'Bram Stoker'), Book(5, 'The Age of Innocence', 'Edith Wharton')]
