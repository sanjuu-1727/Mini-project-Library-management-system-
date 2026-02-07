# Library Management System using Loops

book_name = []
book_status = []   # "Available" or "Issued"

while True:
    print("\n====== LIBRARY MENU ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # ADD BOOK
    if choice == 1:
        n = int(input("How many books to add? "))

        for i in range(n):
            name = input("Enter book name: ")
            book_name.append(name)
            book_status.append("Available")

        print("Books added successfully ✅")

    # VIEW BOOKS
    elif choice == 2:

        if len(book_name) == 0:
            print("No books in library ❌")

        else:
            print("\nBook List:")

            for i in range(len(book_name)):
                print(i+1, ".", book_name[i], "-", book_status[i])

    # ISSUE BOOK
    elif choice == 3:

        issue = input("Enter book name to issue: ")

        found = False

        for i in range(len(book_name)):

            if book_name[i] == issue:

                found = True

                if book_status[i] == "Available":
                    book_status[i] = "Issued"
                    print("Book issued successfully ")
                else:
                    print("Book already issued ")

                break

        if found == False:
            print("Book not found ")

    # RETURN BOOK
    elif choice == 4:

        ret = input("Enter book name to return: ")

        found = False

        for i in range(len(book_name)):

            if book_name[i] == ret:

                found = True

                if book_status[i] == "Issued":
                    book_status[i] = "Available"
                    print("Book returned successfully ")
                else:
                    print("Book was not issued ")

                break

        if found == False:
            print("Book not found ")

    # EXIT
    elif choice == 5:
        print("Thank you for using Library System ")
        break

    else:
        print("Invalid choice Try again")
