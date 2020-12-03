# This main menu function is called upon whenever the main menu is to be displayed
# I have grouped a number of functionalities together in order
# make the main menu more streamlined
def main():
    print('\n==================================================================== MAIN MENU ===============================================================================\n')
    print('********Welcome to My library. Hopefully I have what you are after!********\n')
    print('1. Show Library Item Details')
    print('2. Show User Details')
    print('3. Add/Remove Library Items')
    print('4. Add/Remove Users')
    print('5. Loan Book')
    print('6. Return Book')
    print('7. Search')
    print('8. Exit')
    print('===========================================================================================================================================================\n')




#LibraryItem is the Parent class that includes attributes and methods that both Book and Periodical will inherit
class LibraryItem:
    def __init__(self, uniqueid, title, year):
        self._id = uniqueid
        self._title = title
        self._year = year

    def get_name(self):
        return self._title

    def get_uniqueid(self):
        return self._id

    def get_year(self):
        return self._year

    def __str__(self):
        return 'Unique ID: '+str(self._id)+' Title: ' + self._title+', Year of Publication: '+str(self._year)



# Periodical and Book are Chile classes of Library Item,
# they both share attributes which have been set out in the Parent class and so inherit them
class Periodical(LibraryItem):
    def __init__(self,uniqueid,title,year,editor,vol,issue):
        super().__init__(uniqueid,title,year)
        self._editor = editor
        self._vol = vol
        self._issue = issue

    def get_editor(self):
        return self._editor

    def get_vol(self):
        return self._vol

    def get_issue(self):
        return self._issue

    def __str__(self):
        return super().__str__() + ', Editor: '+self._editor +', Volume: '+ str(self._vol) + ', Issue: ' + str(self._issue)



class Book(LibraryItem):
    def __init__(self,uniqueid, title, year, isbn, author):
        super().__init__(uniqueid, title, year)
        self._isbn = isbn
        self._author = author
        self._onloan = False #False by default until book is loaned
        self._loanedto = None #None by default until book is loaned it, is changed to person's name

    def get_isbn(self):
        return self._isbn

    def get_author(self):
        return self._author

    def __str__(self):
        return super().__str__() + ', ISBN: '+ str(self._isbn) + ', Author: '+self._author + ', On loan: ' + str(self._onloan) + ', On loan to: ' + str(self._loanedto)



#This class includes regular attributes about a user along with an empty booklist that can be appended upon
# which can be seen when user details are printed
#It also has its own methods for loaning and returning a book. When a book is loaned or returned, the book
# attribute .'_onloan' becomes True or False respectively. Also the attribute ._loaned to is replaced by the Name of the
# user and can be seen when details about the users are printed
class User:
    def __init__(self,userid, name, address): # booklist is defined as an empty list below
        self._userid = userid
        self._name = name
        self._address = address
        self._booklist = []

    def get_name(self):
        return self._name

    def get_userid(self):
        return self._userid

    def get_address(self):
        return self._address

    def get_booklist(self):
        return self._booklist

    def loan_book(self, booktoloan, person_name):
        self._title = booktoloan
        if booktoloan._onloan == False:
            booktoloan._onloan = True #Change to true if it isn't already
            booktoloan._loanedto = person_name
            print('\n******Thank you, You have now loaned',booktoloan._title,'out******\n')
            for u in listofusers:
                if u.get_name() == person_name:
                   u._booklist.append(book_name)
        else:
            # None
            print('\n******Sorry,',booktoloan._title, 'is already on loan******\n') #It it is already 'True': print this message


            # booktoloan._booklist = booklist.append(book_name)

    def return_book(self,booktoreturn,person_name):
        self._title = booktoreturn
        if p.get_booklist()==[]:
            print('\n******You do not have any books on loan to return!******')
        else:
            if booktoreturn._onloan == False:
                print('\n******We already have our copy of',booktoreturn._title,' it probably belongs to another library!******\n')
            else:
                print('\n******Thank you, You have now returned',booktoreturn._title,'******\n')
                booktoreturn._onloan = False
                booktoreturn._loanedto = None


                for u in listofusers:
                    if u.get_name() == person_name:
                       u._booklist.remove(book_name)
                       #Trying to append book name to specific user but appends to all user's booklists
                    else:
                        None


    def __str__(self):
        return 'User ID: ' + str(self._userid) + ' Name: ' + self._name + ', Address: ' + self._address + ', Books on loan: ' + str(self._booklist)



listofusers = [User('USERID001','CLOUD', 'NIBELHEIM'),
               User('USERID002','BARRETT', 'COREL'),
               User('USERID003','TIFA', 'NIBELHEIM'),
               User('USERID004','AERIS', 'MIDGAR'),
               User('USERID005','CAIT SITH', 'GOLDEN SAUCER'),
               User('USERID006','YUFFIE', 'WUTAI'),
               User('USERID007','VINCENT', 'MIDGAR'),
               User('USERID008', 'RED XIII', 'COSMO CANYON'),
               User('USERID009', 'CID', 'ROCKET TOWN')
               ]
listofbooks =[Book('UID001','LORD OF THE RINGS', 1960, 1111111111111, 'JRR TOLKIEN'),
              Book('UID002', 'HARRY POTTER', 1997, 1111111111112, 'JK ROWLING'),
              Book('UID003', 'WAR AND PEACE', 1997, 1111111111113, 'LEO TOLSTOY'),
              Book('UID004', 'GREAT EXPECTATIONS', 1865, 1111111111114, 'CHARLES DICKENS'),
              Book('UID005', 'MIDDLEMARCH', 1865, 1111111111115, 'GEORGE ELLIOT'),
              Book('UID006', 'MOBY DICK', 1865, 1111111111116, 'HERMAN MELVILLE'),
              Book('UID007', 'CRIME AND PUNISHMENT', 1865, 1111111111117, 'FYODOR DOSTOEVSKY'),
              Book('UID008', 'EMMA', '1865', 1111111111118, 'JANE AUSTEN'),
              Book('UID009', 'NINETEEN EIGHTY FOUR', 1949, 1111111111119, 'GEORGE ORWELL')
              ]
listofperiodicals = [Periodical('UID010','GARDENING WITH MAD JOHN', 1995, 'JOHN MADIGAN',4,4),
                     Periodical('UID011','POLITICS IN NORTH KOREA', 2007, 'ANTHONY BARTER', 5, 5),
                     Periodical('UID012','SEAMUS HORANS SHOES', 2006, 'SHIB HORAN', 5, 3),
                     Periodical('UID013', 'THE FARMERS JOURNAL', 1980, 'TOM CARROLL', 6, 6)
                     ]

library_list = listofbooks + listofperiodicals #Merge both Library Item Lists to make iterable when adding/removing a library item




#For usability when loaning/adding/removing a book
def show_books():
    if listofbooks !=[]:
        for b in listofbooks:
            print(b)
    else:
        print('There are currently no books in stock!')




#For usability when adding/removing a periodical
def show_periodicals():
    if listofperiodicals!=[]:
        for p in listofperiodicals:
            print (p)
    else:
        print('There are currently no periodicals in stock!')




#One of the main functionalities of the library system is to show what books are in stock
def show_library_items():
    print('\nBooks: ')
    show_books()
    print('\nPeriodicals: ')
    show_periodicals()




# To be called when adding/removing user
def show_users():
    for u in listofusers:
        print (u)

#Adding a book first checks if the user has entered valid isbn and Uniqye ID's. The ISBN must be
#numerical and unique and the Unique ID must also not be registered in
#
# the library
#Because the function iterates through all library item ids, when finally finished, the new book is
#also added to the library_list


def add_book():
    try:
        title = input('Enter Title of Book:').upper()
        year = int(input('Enter Year of Publication: ').upper())
        author = input('Enter Author\'s name: ').upper()
        print('=============================================================================================================')
        print('Thank you for adding this book to the library - Press 1 at the main menu to confirm it has been added!')
        print('=============================================================================================================')
        listofbooks.append(Book(uid, title, year, isbn, author))
        library_list.append(Book(uid,title,year,isbn,author)) #Add to this list as well
    except ValueError:
        print('\n******Invalid Input - Year be all numbers, se trpleay again******')


def add_periodical():
    try:
        title = input('Enter Title of Periodical: ').upper()
        year = int(input('Enter Year of Publication: '))
        editor = input('Enter Editor\'s name: ').upper()
        volume = int(input('Enter Volume Number: '))
        issue = int(input('Enter Issue Number: '))
        print('=============================================================================================================')
        print('Thank you for adding this periodical to the library - Press 1 at the main menu to confirm it has been added!')
        print('=============================================================================================================')
        listofperiodicals.append(Periodical(uid, title, year, editor, volume, issue))
        library_list.append(Periodical(uid,title,year,editor,volume,issue))#Add to this list as well


    except ValueError:
        print('\n******Invalid Input - Year, Volume and Issue must be numbers, please try again')




#The system asks for the User ID first to see if it already exists on the system, if it isn't, thisfunction is called and the
# user is added to the system.
def add_user():
    name = input('Enter Name: ').upper()
    address = input('Enter Address: ').upper()
    return listofusers.append((User(userid,name,address)))




#This function does not allow you to remove a user if they have books out on
# loan, only if they have an empty list can they be removed. The book is impossible to return
# otherwise and would no longer be able to be loaned to a future user
def remove_user(id):
    if u.get_booklist()==[]:
        print ('\n******You have removed '+ u._name +' from our system******')
        return listofusers.remove(u)
    else:
        return print('\n******That user must return the books they have loaned! Press 6 at the main menu to return it safely.******')




#Similar to removing a user, a book must be returned before it can be removed from the system.
def remove_book(uid):
    if b._onloan==True:
        print(b._title +' must be returned before it can be removed!')
    else:
        print('\nYou have removed ' + b._title + ' from our system')
        listofbooks.remove(b)





#A periodical cannot be loaned so there are no unusual conditions to satisy for this function to work
def remove_periodical(uid):
        print('\n You have removed ' + p._title + ' from our system')
        listofperiodicals.remove(p)
        #Remove from both lists for unique ID checking when re-adding




#The next two functions take less parameters than the search function and is
# in-built into the loan method of the User class
def find_user(listofusers, user_name):
    for u in listofusers:
        if u.get_name() == user_name:
            return u

    print('******No such user******')
    return None




def find_book(listofbooks, book_name):
    for m in listofbooks:
        if m.get_name() == book_name:
            return m
    print('******No such book******')
    return None

#In the search functions I defined an empty list and if any of the search criteria
#matched any of those in the attributes of a book, periodical or user that particular object would
#be appended into the list, printed and then returned.
def search_user(listofusers, name, userid, address):
    usearchresults=[]
    for u in listofusers:
        if u.get_name() == name \
                or u.get_userid() == userid \
                or u.get_address() == address:
            usearchresults.append(u.__str__())#Apply string method so memory address is not returned

    for u in usearchresults:
        print(u)
    if usearchresults ==[]:
        print('\n******There is no such user in this library!******')
    else:
        return usearchresults

#In the search functions I defined an empty list and if any of the search criteria
#matched any of those in the attributes of a book, periodical or user that particular object would
#be appended into the list, printed and then returned.
def search_book(listofbooks,uid, title, year, isbn, author):
    bsearchresults=[]
    for b in listofbooks:
        if b.get_uniqueid()== uid \
                or b.get_name() == title \
                or b.get_year() == year \
                or b.get_isbn() == isbn \
                or b.get_author() == author:
            bsearchresults.append(b.__str__())#Apply string method so memory address is not returned

    if bsearchresults == []:
        print('\n******There is no such book in this library!******')
    else:
        for i in bsearchresults:
            print(i)
        return bsearchresults




#In the search functions I defined an empty list and if any of the search criteria
#matched any of those in the attributes of a book, periodical or user that particular object would
#be appended into the list, printed and then returned.
def search_periodical(listofperiodicals, uid, title, year, editor, volume, issue):
    psearchresults = []
    for p in listofperiodicals:
        if p.get_uniqueid()== uid \
                or p.get_name() == title \
                or p.get_year() == year \
                or p.get_editor() == editor \
                or p.get_vol() == volume \
                or p.get_issue() == issue:
            psearchresults.append(p.__str__())#Apply string method so memory address is not returned

    for i in psearchresults:
        print(i)
    if psearchresults == []:
        print('\n******There is no such periodical in this library!******')
    else:
        return psearchresults

def welc():
    print('\n===========================================================================================================================================================')
    print('\n')
    print('#     # ####### #        #####  ####### #     # #######      ####### #######      #     # #     #      #       ### ######  ######     #    ######  #     #')
    print('#  #  # #       #       #     # #     # ##   ## #               #    #     #      ##   ##  #   #       #        #  #     # #     #   # #   #     #  #   #')
    print('#  #  # #       #       #       #     # # # # # #               #    #     #      # # # #   # #        #        #  #     # #     #  #   #  #     #   # #')
    print('#  #  # #####   #       #       #     # #  #  # #####           #    #     #      #  #  #    #         #        #  ######  ######  #     # ######     #')
    print('#  #  # #       #       #       #     # #     # #               #    #     #      #     #    #         #        #  #     # #   #   ####### #   #      #')
    print('#  #  # #       #       #     # #     # #     # #               #    #     #      #     #    #         #        #  #     # #    #  #     # #    #     #')
    print(' ## ##  ####### #######  #####  ####### #     # #######         #    #######      #     #    #         ####### ### ######  #     # #     # #     #    #')
    print('\n')#Makes the user interface a bit more personable

def thank():
    print('=================================================================')
    print('\n')
    print('####### #     #    #    #     # #    #    #     # ####### #     #')
    print('   #    #     #   # #   ##    # #   #      #   #  #     # #     #')
    print('   #    #     #  #   #  # #   # #  #        # #   #     # #     #')
    print('   #    ####### #     # #  #  # ###          #    #     # #     #')
    print('   #    #     # ####### #   # # #  #         #    #     # #     #')
    print('   #    #     # #     # #    ## #   #        #    #     # #     #')
    print('   #    #     # #     # #     # #    #       #    #######  ##### ')
    print('\n')
    print('=================================================================\n')#Ditto

welc()
main()
option = input('******Please enter an option: ******')



#Menu System:....
while(option!='8'):
    if option =='1':
        print('\n*********SHOWING LIBRARY ITEMS*********')
        show_library_items()

    elif option =='2':
        print('\n*********SHOWING USER DETAILS*********')
        show_users()

    elif option =='3':
        print('\n*********EDIT LIBRARY********')
        print('Press 1 to add an item')
        print('Press 2 to remove an item')
        print('Press any other key to return to the main menu')
        choice=input('\nAdd or Remove? ')
        if choice == '1':
            print('\n*********ADD ITEM********')
            print('Press 1 to add a book')
            print('Press 2 to add a periodical')
            print('Press any other key to return to the main menu')
            choice = input('\nBook or Periodical? ')
            if choice =='1':
                try:
                    print('\n****************ADDING A BOOK****************')
                    show_books()
                    uid = input('\nEnter Unique ID: ').upper()
                    for b in library_list:  #To Make sure the unique ID is not already taken
                        if uid == b._id:
                            print('\nWe already have that one:')
                            print(b)
                            print('\nMake sure the ID is Unique!')
                            break
                    else:
                        isbn= int(input('Enter ISBN(13 numbers):'))
                        strisbn = str(isbn)
                        while len(strisbn) != 13:
                            isbn = int(input("Invalid ISBN. Please enter ISBN (13 numbers): "))
                            strisbn = str(isbn)
                        else:
                            for i in listofbooks:
                                if i._isbn==isbn:
                                    print('\nWe already have that one:')
                                    print (i)
                                    print('\nMake sure the ISBN is Unique!')
                                    break
                            else:
                                add_book()
                except ValueError:
                    print('Make sure the ISBN is all numbers!')

            elif choice == '2':
                print('\n****************ADDING A PERIODICAL****************')
                show_periodicals()
                uid = input('Enter Unique ID: ').upper()
                for p in library_list:
                    if uid == p._id:
                        print('\n We already have that one:')
                        print(p)
                        break
                else:
                    # title = input('Enter Title of Periodical: ')
                    add_periodical()
            else:
                print('\nInvalid Choice, try again!')

        elif choice == '2':
            print('\n*********REMOVE ITEM********')
            print('Press 1 to remove a book')
            print('Press 2 to remove a periodical')
            print('Press any other key to return to the main menu')
            choice = input('\nBook or periodical? ')
            if choice =='1':
                print('\n****************REMOVING A BOOK****************')
                show_books()
                if listofbooks !=[]:
                    uid = input('Enter Unique ID: ').upper()
                    for b in listofbooks:
                        if uid == b._id:
                            remove_book(b)
                            break

                    for l in library_list:
                        if uid == l._id:
                            library_list.remove(l)
                            break
                    else:
                        print('\nThat book is not on our system!')
                else:
                    print('There are no books to remove!')

            elif choice == '2':
                print('\n********REMOVING A PERIODICAL*******')
                show_periodicals()
                if listofperiodicals !=[]:
                    uid = input('Enter Unique ID: ').upper()
                    for p in listofperiodicals:
                        if uid == p._id:
                            remove_periodical(p)
                            break

                    for l in library_list:
                        if uid == l._id:
                            library_list.remove(l)
                            break
                    else:
                        print('\nThat periodical is not on our system!')
                else:
                    print('There are no periodicals to remove!')

    elif option =='4':
        print('\n*********EDIT USERS********')
        print('Press 1 to add an user')
        print('Press 2 to remove an user')
        print('Press any other key to return to the main menu')
        choice=input('Add or Remove User?')
        if choice =='1':
            print('\n*****ADDING USER******')
            show_users()
            userid = input('Enter Unique User ID: ').upper()
            for u in listofusers:
                if userid == u._userid:
                    print('\nThat user already exists on our system!')
                    print(u)
                    break
            else:
                add_user()
                print('\nThanks for adding that user to the system!')
        elif choice == '2':
            print('\n******REMOVING USER******')
            show_users()
            if listofusers!=[]:
                userid = input('Enter Unique User ID: ').upper()
                for u in listofusers:
                    if userid == u._userid:
                        remove_user(userid)
                        break
                else:
                    print('\nThat user ID is not on our system!')
            else:
                print('There are no users to remove!')

    elif option =='5':
        try:
            print('\n******LOANING BOOK******')
            print('Here is a list of the books in my library: ')
            show_books()

            person_name = input('\nEnter person\'s name: ').upper()
            for u in listofusers:
                if person_name == u._name:
                    break
            else:
                person_name = input('That person is not registered with this library. Enter person\'s name again: ').upper()

            book_name = input('Enter book\'s title: ').upper()
            for b in listofbooks:
                if book_name == b._title:
                    break
            else:
                book_name = input('That is not a book in this library! Enter book\'s title that we actually have: ').upper()

            person = find_user(listofusers, person_name)
            book = find_book(listofbooks, book_name)

            person.loan_book(book, person_name)
        except AttributeError:
            print('Invalid Input for User or Book')
        #Change status of a book from onloan false to onloan true and track what user is taking it.
    elif option =='6':
        try:
            print('\n******RETURNING BOOK******\n')
            person_name = input('Enter person\'s name: ').upper()
            for u in listofusers:
                if person_name == u._name:
                    break
            else:
                person_name = input('That person is not registered with this library. Enter person\'s name again: ').upper()

            book_name = input('Enter book\'s title: ').upper()
            for b in listofbooks:
                if book_name == b._title:
                    break
            else:
                book_name = input('That is not a book in this library! Enter book\'s title that we actually have: ').upper()

            p = find_user(listofusers, person_name)
            b = find_book(listofbooks, book_name)

            p.return_book(b,person_name)
        except AttributeError:
            print('Invalid input for user or book')


    elif option == '7':
        print('\n*********SEARCH********')
        print('Press 1 to search a user')
        print('Press 2 to search a book')
        print('Press 3 to search a periodical')
        print('Press any other key to return to the main menu')
        choice = input('\nUser,Book or periodical? ')
        if choice == '1':
            print('\n******SEARCH USER******\n')
            print('\nFill in at least one field. Just leave blank if you are unsure\n')
            name = input('Enter Users Name: ').upper()
            userid = input('Enter userid: ').upper()
            address = input('Enter address: ').upper()
            search_user(listofusers,name,userid,address)

        if choice == '2':
            print('\n******SEARCH BOOK******\n')
            print('\nFill in at least one field. Just leave blank if you are unsure\n')
            uid = input('Enter Unique ID: ').upper()
            title = input('Enter Title of Book:').upper()
            year = input('Enter Year of Publication: ')
            isbn = input('Enter ISBN: ').upper()
            author = input('Enter Author\'s name: ').upper()
            search_book(listofbooks,uid,title,year,isbn,author)


        if choice == '3':
            print('\n******SEARCH PERIODICAL******\n')
            print('\nFill in at least one field. Just leave blank if you are unsure\n')
            uid = input('Enter Unique ID: ').upper()
            title = input('Enter Title of Periodical: ').upper()
            year = input('Enter Year of Publication: ').upper()
            editor = input('Enter Editor\'s name: ').upper()
            volume = input('Enter Volume Number: ').upper()
            issue = input('Enter Issue Number: ').upper()
            search_periodical(listofperiodicals,uid,title,year, editor, volume, issue)

    else:
        print('\n*****************WRONG INPUT!*****************\n')
        print('\nPlease enter a one of the options on screen: \n')

    main()
    option = input("\nPlease enter an option: ")

thank()
print('\n***************Thank you for using my library, goodbye and come back soon!***************\n')