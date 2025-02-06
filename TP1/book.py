class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self._is_borrowed = False
        self._is_reserved = False

    def present(self):
        print(
            f"Book:\n"
            f"  - Title : {self.title}\n"
            f"  - Author : {self.author}\n"
            f"  - Genre : {self.genre}"
        )

    def borrow(self):
        if self._is_borrowed:
            print(f"The book {self.title} is already borrowed.")
        elif self._is_reserved:
            print(f"The book {self.title} is reserved. It cannot be borrowed.")
        else:
            self._is_borrowed = True
            print(f"The book {self.title} has been borrowed successfully.")

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            print(f"The book {self.title} has been returned successfully.")
        else:
            print(f"The book {self.title} is available.")

    def reserve(self):
        if self._is_borrowed:
            print("Impossible of reserving a borrowed book.")
        elif self._is_reserved:
            print(f"The book {self.title} is already reserved.")
        else:
            self._is_reserved = True
            print(f"The book {self.title} has been reserved successfully.")

    def cancel_reservation(self):
        if self._is_reserved:
            self._is_reserved = False
            print("The reservation has been canceled successfully.")
        else:
            print(f"The book {self.title} is not reserved.")


if __name__ == "__main__":
    # Exemple d'utilisation
    normal_people = Book(
        title="Normal people",
        author="Sally Rooney",
        genre="Novel",
    )
    normal_people.present()
    normal_people.borrow()
    normal_people.borrow()
    normal_people.return_book()
    normal_people.reserve()
    normal_people.cancel_reservation()
