print(" .........IISER B Library Management System.........")
print("                                 - by Yash Gupta")
class Library :
    def __init__(self,list , name):
        self.bookslist = list
        self.name = name
        self.lendDict ={}

    def displaybooks(self):
        print(f"we have following books in our library : {self.name}")
        for book in self.bookslist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(" Lender - book database has been updated")
            print("you can take the book now !!!!!")
        else:
            print(f"sorry !! The Book is already been taken by {self.lendDict[book]}")

    def addbook(self,book):
        self.bookslist.append(book)
        print("Book has been added successfully")

    def returnbook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    iiserblibrary= Library(['Python','Rich Daddy Poor Daddy', 'Harry Potter','C++ basics','Basics of machine learning','Advanced Python'] , "Central_Library_IISERB")


    while(True):
        print(f"Welcome to the {iiserblibrary.name} !!!!! \n Enter your choice to continue ")
        print("You can choose: ")
        print("1.Display Books")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice= int(input())

        if user_choice==1:
            iiserblibrary.displaybooks()

        elif user_choice==2:
            book= input("Enter the name of the book you want to lend : ")
            user = input("Please enter your name : ")
            iiserblibrary.lendbook(user,book)

        elif user_choice==3:
            book = input("Enter the name of the book you want to add :")
            iiserblibrary.addbook(book)

        elif user_choice==4:
            book=input("Enter the name of the book you want to return : ")
            iiserblibrary.returnbook(book)

        else:
            print("Your option is not valid ")

        print("Press c to continue and q to quit")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue



