

class KrmuDigitalLibrary:
    def __init__(self, listOfBooks):
        self.Books = listOfBooks

    def DisplayAvailableBooks(self):
        print("List of available books are:")
        for i in self.Books:

            print("* "+i)

    def BorrowBooks(self, Bookname):
        if Bookname in self.Books:
            a = int(input("Please Enter your roll no. : "))
            b = input("Please Enter your name here: ")
            c = input("Please Enter your course name: ")
            
            print("")
            print(f"Dear {b}, You have successfully borrowed {Bookname}.\nPlease keep it safe, and return it within 30 days.\nHAVE A NICE DAY AHEAD!")
            print("MADE BY RAHUL RAJ PARIDA BTECH CSE (AIML)")
            self.Books.remove(Bookname)
            return True
        else:
            print(
                "Sorry!, Either this book is already borrowed to someone or not available at this moment. ")
            print("MADE BY RAHUL RAJ PARIDA BTECH CSE (AIML)")
            return False

    def ReturnBook(self, Bookname):
        a = int(input("Please Enter your roll no. : "))
        b = input("Please Enter your name here: ")
        c = input("Please Enter your course name: ")
        d = input("Please Enter your course's year: ")
        print("")
        print(f"Thankyou {b}, for submitting or returning the book.")
        print("MADE BY RAHUL RAJ PARIDA BTECH CSE (AIML)")


class student:
    def BorrowBook(self):
        self.books = input("Enter the name of the book to borrow or issue: ")
        return self.books

    def ReturnBook(self):
        self.books = input("Enter the name of the book to return or Donate: ")


if __name__ == "__main__":
    krmu = KrmuDigitalLibrary(
        ["Machine Learning with Python", "Django King", "Engineering Mathematics", "Flask","Introduction To Algorithms","Modern Control Engineering","Chemical Engineering","Electrical Circuits"])
    student = student()

    Introduction = '''
    ******* WELCOME TO KRMU DIGITAL LIBRARY *******
    PLEASE PRESS THE NUMBER KEY ACCORDINGLY AS MENTIONED BELOW :-
    1. DISPLAY AVAILABLE BOOKS (PRESS 1)
    2. BORROW BOOKS (PRESS 2)
    3. RETURN OR DONATE BOOKS  (PRESS 3)
    4. EXIT THE APPLICATION (PRESS 4)

    '''
    while(True):
        print(Introduction)
        inputFromTheUser = int(input("Enter your choice: "))
        print("")
        if inputFromTheUser == 1:
            krmu.DisplayAvailableBooks()
        elif inputFromTheUser == 2:
            krmu.BorrowBooks(student.BorrowBook())
        elif inputFromTheUser == 3:
            krmu.ReturnBook(student.ReturnBook())
        else:
            print("Thankyou for using this application")
            exit()


'''
MADE BY: RAHUL RAJ PARIDA
COURSE: BTECH CSE AIML
ROLL NO: 2101730027
PARTCIPATION TYPE: SOLO

'''