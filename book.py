class Book:
    def __init__(self, title, author, isbn, publication_year):
        self._title = title  # Encapsulated attribute
        self._author = author
        self._isbn = isbn
        self._publication_year = publication_year
        self._is_available = True
        self._current_reader = None

    def check_out(self, reader_name):
        if self._is_available:
            self._is_available = False
            self._current_reader = reader_name
            return f"'{self._title}' has been checked out by {reader_name}"
        return f"'{self._title}' is currently checked out by {self._current_reader}"

    def return_book(self):
        if not self._is_available:
            self._is_available = True
            previous_reader = self._current_reader
            self._current_reader = None
            return f"'{self._title}' has been returned by {previous_reader}"
        return f"'{self._title}' is already available"

    def get_book_info(self):
        return {
            "Title": self._title,
            "Author": self._author,
            "ISBN": self._isbn,
            "Year": self._publication_year,
            "Status": "Available" if self._is_available else f"Checked out by {self._current_reader}"
        }


class EBook(Book):
    def __init__(self, title, author, isbn, publication_year, file_format, file_size_mb):
        super().__init__(title, author, isbn, publication_year)
        self._file_format = file_format
        self._file_size_mb = file_size_mb
        self._is_downloaded = False

    def download(self):
        if not self._is_downloaded:
            self._is_downloaded = True
            return f"'{self._title}' has been downloaded ({self._file_size_mb}MB)"
        return f"'{self._title}' is already downloaded"

    def get_book_info(self):
        info = super().get_book_info()
        info["Format"] = self._file_format
        info["File Size"] = f"{self._file_size_mb}MB"
        info["Download Status"] = "Downloaded" if self._is_downloaded else "Not Downloaded"
        return info


class Textbook(Book):
    def __init__(self, title, author, isbn, publication_year, subject, edition):
        super().__init__(title, author, isbn, publication_year)
        self._subject = subject
        self._edition = edition
        self._has_online_resources = False

    def activate_online_resources(self):
        if not self._has_online_resources:
            self._has_online_resources = True
            return f"Online resources for '{self._title}' have been activated"
        return f"Online resources for '{self._title}' are already active"

    def get_book_info(self):
        info = super().get_book_info()
        info["Subject"] = self._subject
        info["Edition"] = self._edition
        info["Online Resources"] = "Available" if self._has_online_resources else "Not Available"
        return info


# Example usage
if __name__ == "__main__":
    # Create an ebook
    ebook = EBook("The Digital Age", "Doreen Kanini", "978-3-16-148410-0", 2023, "PDF", 15.5)
    print("\nEBook Demo:")
    print(ebook.check_out("Victor J"))
    print(ebook.download())
    print("Book Info:", ebook.get_book_info())

    # Create a textbook
    textbook = Textbook("Advanced Mathematics", "Dr. Robert Brown", "978-1-23-456789-0", 2022, "Mathematics", "3rd")
    print("\nTextbook Demo:")
    print(textbook.check_out("Tina M"))
    print(textbook.activate_online_resources())
    print("Book Info:", textbook.get_book_info()) 