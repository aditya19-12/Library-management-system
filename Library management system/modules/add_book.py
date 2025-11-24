def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter unique book ID: ")

    with open("data/books.txt", "a") as f:
        f.write(f"{book_id},{title},{author}\n")

    print("Book added successfully!")
