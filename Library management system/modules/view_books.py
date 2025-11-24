def view_books():
    print("\n--- Available Books ---")
    try:
        with open("data/books.txt", "r") as f:
            data = f.read()
            print(data if data else "No books found!")
    except FileNotFoundError:
        print("Book data file not found!")
