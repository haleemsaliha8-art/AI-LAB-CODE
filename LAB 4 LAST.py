# Base class
class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def viewFullDescription(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")

    def addToShoppingBasket(self):
        print(f"{self.name} added to shopping basket.")

    def removeFromShoppingBasket(self):
        print(f"{self.name} removed from shopping basket.")


# Derived class 1
class MP3(Item):
    def __init__(self, name, description, price, artist, duration):
        super().__init__(name, description, price)
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing MP3: {self.name} by {self.artist}")

    def download(self):
        print(f"Downloading MP3: {self.name}")


# Derived class 2
class DVD(Item):
    def __init__(self, name, description, price, certificate, duration, actors):
        super().__init__(name, description, price)
        self.certificate = certificate
        self.duration = duration
        self.actors = actors

    def viewTrailer(self):
        print(f"Viewing trailer for DVD: {self.name}")


# Derived class 3
class Book(Item):
    def __init__(self, name, description, price, author, numberOfPages, genre):
        super().__init__(name, description, price)
        self.author = author
        self.numberOfPages = numberOfPages
        self.genre = genre

    def previewContent(self):
        print(f"Previewing content of book: {self.name}")


# ---------- Example Run ----------
if __name__ == "__main__":
    # Creating objects
    mp3 = MP3("Shape of You", "Popular song", 250, "Ed Sheeran", "4:24")
    dvd = DVD("Avengers: Endgame", "Action Movie", 1500, "PG-13", "3h 2m", ["Robert Downey Jr.", "Chris Evans"])
    book = Book("Python Basics", "Learn Python Programming", 900, "John Doe", 300, "Education")

    # Using methods
    mp3.viewFullDescription()
    mp3.play()
    mp3.download()

    print("------")

    dvd.viewFullDescription()
    dvd.viewTrailer()

    print("------")

    book.viewFullDescription()
    book.previewContent()
