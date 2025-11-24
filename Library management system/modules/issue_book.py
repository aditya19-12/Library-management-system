def issue_book():
    user = input("Enter your name: ")
    book_id = input("Enter book ID to issue: ")

    with open("data/issued_books.txt", "a") as f:
        f.write(f"{user},{book_id}\n")

    print("Book issued successfully!")
