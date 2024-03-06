''' Author: Brock Hemsouvanh and Zadkiel Rodriguez
    Date: 2024-03-08
    whatabook_app.py Description: Console for fictional client, WhatABook Company, which allows
    their users to utilize their book database with the following qualities in mind:
    Display all books available in the store.
    Display books filtered by genre, with the user being able to select a genre and see the corresponding books.
    Display books filtered by author.
    Search for a specific book by its bookId.
    Show a customer's wishlist by their customerId.
    Allow a customer to add books to their wishlist.
    Allow a customer to remove books from their wishlist.
    etc...
'''

from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('insert_mongodb_connection_string_here')
db = client['WhatABook']

# Functions for database operations
def show_all_books():
    books = db.books.find({})
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

# ... (more functions for other operations)

# Main menu function
def main_menu():
    while True:
        print("\nWhatABook Menu")
        print("1. Display all books")
        print("2. Display books by genre")
        print("3. Display books by author")
        print("4. Display a customer's wishlist")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_books()
        elif choice == '2':
            # Call function to show books by genre
        elif choice == '3':
            # Call function to show books by author
        elif choice == '4':
            # Call function to display a customer's wishlist
        elif choice == '5':
            print("Thank you for using WhatABook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == '__main__':
    main_menu()
