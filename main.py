import json
import os  

data_file = "lib-txt"

def loading_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
        return []
    
def save_library(library):
    with open(data_file, "w")as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter The Title Of The Book : ")
    author = input("Enter The Author Of The Book : ")
    year = input("Enter The Year Of The Book : ")
    genre = input("Enter The Genre Of The Book : ")
    read = input("Have You Read The Book ? (yes/no) : ").lower() == "yes"

    new_book = {
        "title":title,
        "author":author,
        "year":year,
        "genre":genre,
        "read":read
    }

    library.append(new_book)
    save_library(library)
    print("Book Added Successfully !")

def remove_book(library):
    title = input("Enter The Title Book To Remove From Library : ")
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < initial_length:
        save_library(library)
        print("Book Removed Successfully !")

    else:
        print("Book Not Found In Library !")

def search_library(library):
    searching = input("Search By Title Or Author : ").lower()
    search_term = input(f"Enter The {searching} : ").lower()

    results = [book for book in library if search_term in book[searching] .lower()]
    if results:
        for book in results:
          status = "Read" if book['read'] else "Not Read"
        print(f"{book['title']}  by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("Book Not Found In Library !")


def display_books(library):
    if library:
        for book in library:
         status = "Read" if book['read'] else "Not Read"
        print(f"{book['title']}  by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("The Library Is Empty")
    
def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total Books : {total_books}")
    print(f"Percentage read : {percentage_read:.2f}%")

def main():
    library = loading_library()
    while True:
        print("\n Library Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter Your Choice : ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Bye Bye !")
            break
        else:
            print("Invalid Choice !")

if __name__ == "__main__":
   main()

