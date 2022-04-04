

#exercise 1

def count_vowels(text:str):
    vowels = "aeiou"
    count = 0
    if type(text) == str: #whyy isn't it workiiing # yeeaah it's workiiing remember to check type(whatever) == str not just whatever == str
        for i in text.casefold():
            if i in vowels:
                count += 1
        return int(count)
    else:
        return 42

# print(count_vowels("Esther"))

"""2)Write a function hamming(text1, text2) that accepts two strings as arguments. The
function determines the hamming distance of the strings. The hamming distance is the
number of characters that are different between the two strings. Example: the strings ‘cat’ and
‘kat’ have a hamming distance of 1 because the first character is different. The function
checks if both given strings are of equal length and returns 0 they are not. If both strings are of
equal length, it calculates the hamming distance and returns it as an integer"""

def hamming(text1:str,text2:str):
    count = 0
    if len(text1) == len(text2): #passt
        for i in text1.casefold():
            if i in text2.casefold():
                count +=1
        return int(count)
    else:
        return 0 #passt

print(hamming("Kate", "Cate"))

#3

class Vehicle:
    def __init__(self, color: str, fuel_type: str):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color: str, fuel_type: str, doors):
        super().__init__(color, fuel_type)
        self.doors = doors
    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)
    #def print_override_string(self):
        #print("Color: {0}, Fuel Type: {1}, Doors:{2}").format(self.color, self.fuel_type, self.doors)

    def print_color(self):
        print(self.color)
    def print_fuel_type(self):
        print(self.fuel_type)
    def print_doors(self):
        print(self.doors)

#car01 = Car("red","bio",4)
#print(car01)

class Bus(Vehicle):
    def __init__(self,color:str ,fuel_type:str ,passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers
    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)

    def print_color(self):
        print(self.color)
    def print_fuel_type(self):
        print(self.fuel_type)
    def print_passengers(self):
        print(self.passengers)

#Bus01= Bus("red", "bio", 50)

#print(Bus01)


#4

class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0}, {1}".format(self.name, self.author)

book1 = Book("Normal People", "Sally Rooney")
print(book1)

#5

class BookShelf:
    def __init__(self, books):
        self.books = books

    def add_book_list(self, booklist):
        for i in booklist:
            if isinstance(i, Book):
                self.books.append(i)

    def books_by_author(self, author):
        bba = []
        for i in self.books:
            if str(i.author) == author:
                bba.append(str(i.name))
        return (bba)

    def get_books(self):
        ab = []
        for i in self.books:
            ab.append(str(i.name))
        return (ab)

    def clear_shelf(self):
        self.books = []


BS1 = BookShelf([Book("Das kleine Ich bin ich", "Weiß nicht"), Book("hello world", "ich")])

# for i in BS1.books:
#    print("{0},{1}".format(i.name,i.author))

aListe = [Book("a", "b"), Book("blabla", "blablabla"), Book("ceee", "b"), ("hehe", "hehe"), (123, 456)]
BS1.add_book_list(aListe)

for i in BS1.books:
    print("{0},{1}".format(i.name, i.author))

print(BS1.books_by_author("b"))
print(BS1.get_books())
BS1.clear_shelf()
print(BS1.books_by_author("Testauthor"))
print(BS1.get_books())