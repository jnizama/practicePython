# Given a list of dictionaries containing information about books:
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "pages": 281},
    {"title": "1984", "author": "George Orwell", "year": 1949, "pages": 328},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "pages": 432},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "pages": 180},
    {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "pages": 635}
]

# Your tasks:

# 1. Use filter() and a lambda function to create a new list of books published after 1900.
modern_books = list(filter(lambda b: b["year"] > 1900, books))

# 2. Use map() and a lambda function to create a list of tuples 
# containing only the title and author of each book.
title_author_pairs = tuple(map(lambda b: b["title"] +"-"+ b["author"], books))

# 3. Use filter(), map(), and lambda functions to create a list of the titles of books with more than 300 pages.
long_book_titles = list(map(lambda m : m["title"], filter(lambda b: b["pages"] > 300, books))) 
# Write your solutions below:

# Task 2:
#title_author_pairs = 

# Task 3:
#long_book_titles = 

# Print your results
print("Modern books:", modern_books)
print("Title-author pairs:", title_author_pairs)
print("Long book titles:", long_book_titles)