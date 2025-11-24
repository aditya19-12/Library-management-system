def search_book():
    keyword = input("Enter title or author to search: ").lower()
    found = False

    with open("data/books.txt", "r") as f:
        for line in f:
            if keyword in line.lower():
                print("Found:", line)
                found = True

    if not found:
        print("No matching book found!")
