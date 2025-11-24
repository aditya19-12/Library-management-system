import os

print("Current directory:", os.getcwd())
print("Available folders/files:", os.listdir())
print("Inside data folder (if exists):", os.listdir("data") if os.path.exists("data") else "Data folder missing!")

from modules.add_book import add_book
from modules.view_books import view_books
from modules.issue_book import issue_book
from modules.search_book import search_book

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Search Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")