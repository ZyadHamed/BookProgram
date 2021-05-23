class Book:
    ID = 0
    Name = ""
    Price = 0
    AmountInStock = 0
    def __init__(self, id, bookName, bookPrice, amountInStock):
        self.ID = id
        self.Name = bookName
        self.Price = bookPrice
        self.AmountInStock = amountInStock

def AddBook(book):
    File = open("Data.txt", "a+")
    DataToWrite = str(book.ID) + "," + book.Name + "," + str(book.Price) + "," + str(book.AmountInStock) + "\n"
    File.write(DataToWrite)
    File.close()

def EditBook(bookID, newBook):
    i = 0
    File = open("Data.txt", "r")
    Lines = File.readlines()
    File.close()
    for index in range(len(Lines)):
        Data = Lines[index].split(",")
        if(Data[0] == str(bookID)):
            i = index
            break
    NewData = str(newBook.ID) + "," + newBook.Name + "," + str(newBook.Price) + "," + str(newBook.AmountInStock) + "\n"
    Lines[i] = NewData
    File2 = open("Data.txt", 'w')
    File2.writelines(Lines)

def PrintAllBooks():
    File = open("Data.txt", "r")
    Lines = File.readlines()
    File.close()
    for line in Lines:
        Data = line.split(",")
        print("Book ID: " + Data[0] + ", Book Name: " + Data[1] + ", Book Price: " + Data[2] + ", Amount of that book left in stock: " + Data[3])

def FindBook(id):
    File = open("Data.txt", "r")
    Lines = File.readlines()
    File.close()
    for line in Lines:
        Data = line.split(",")
        if(Data[0] == str(id)):
            book = Book(int(Data[0]), Data[1], int(Data[2]), int(Data[3]))
            return book
    
    return None

def DeleteBook(bookID):
    File = open("Data.txt", "r")
    Lines = (File.read()).split("\n")
    File.close()
    for line in Lines:
        Data = line.split(",")
        if Data[0] == str(bookID):
            Lines.remove(line)
            break
    fullText = ""
    for line in Lines:
        fullText = fullText + line + "\n"
    File = open("Data.txt", "w")
    File.write(fullText)

def IsBookExistent(id):
    book = FindBook(id)
    if book != None:
        return True
    else:
        return False
UserName = "Zyad"
Password = "1234"
HasTheUserLoggedIn = False

userType = input("Please enter wheather you are an admin or a user: ")
if userType == "admin":
        while HasTheUserLoggedIn == False:
            userName = input("Username: ")
            password = input("Password: ")
            if (userName == UserName) and (password == Password):
                HasTheUserLoggedIn = True
                print("Hello " + userName)
                print("What action do you want to do?")
                print("1: Add a new book")
                print("2: Alter the data of existing book")
                print("3: Delete a book")
                print("4: View the data of all books")
                print("5: Close the program")
            else:
                print("Invalid Username or password, Try again")


        IsProgramExited = False
        while IsProgramExited == False:
            
            choise = input("Choose an action by entering it's number: ")
            if choise == "1":
                id = int(input("What is the book ID: "))
                if IsBookExistent(id):
                    print("Sorry, but this book already exists")
                else:
                    name = input("What is the book name: ")
                    price = input("What is the book price: ")
                    amountinstock = int(input("How much is currently in stock: "))
                    book = Book(id, name, price, amountinstock)
                    AddBook(book)
                    print("Book " + str(id) + " was added sucessfully")
            elif choise == "2":
                bookID = input("Please enter a book ID: ")
                book = FindBook(int(bookID))
                if(True):
                    newBookID = int(input("Please enter the new book ID: "))
                    newBookName = input("Please enter the new book Name: ")
                    newBookPrice = int(input("Please enter the new book Price: "))
                    newBookAmountInStock = int(input("Please enter the new AmountInStock: "))
                    book = Book(newBookID, newBookName, newBookPrice, newBookAmountInStock)
                    EditBook(bookID, book)
                    print("Book " + str(bookID) + " Was altered successfully")

                else:
                    print("Book wasn't found")
            elif choise == "3":
                id = int(input("What is the book ID: "))
                if IsBookExistent(id) == True:
                    DeleteBook(id)
                    print("Book " + str(id) + " was deleted sucessfully")
                else:
                    print("Book " + str(id) + " Dosen't exist")
            elif choise == "4":
                PrintAllBooks()
            elif choise == "5":
                IsProgramExited = True
                exit()

elif userType == "user":
    print("What action do you want to do?")
    print("1: Buy a book")
    print("2: View the data of all books")
    print("3: Exit the program")

    IsProgramExited = False
    while IsProgramExited == False:
        choise = input("Choose an action by entering it's number: ")
    
        if choise == "1":
            bookID = int(input("Enter the ID of the book: "))
            if IsBookExistent(bookID) == True:
                AmountOfOrder = int(input("Enter the Amonut that you want: "))
                book = FindBook(bookID)
                if book.AmountInStock - AmountOfOrder >= 0:
                    book.AmountInStock -= AmountOfOrder
                    EditBook(bookID, book)
                    print("Purchase was done successfully")
                else:
                    print("No enough amount of books for your order")
            else:
                print("Book " + str(bookID) + " wasn't found")

        elif choise == "2":
            PrintAllBooks()

        elif choise == "3":
            IsProgramExited = True
            exit()
    

