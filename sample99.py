class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

def printBookArray(books):
    # ループ
    for s in range(0,len(books)):
        print(books[s].title + " written by Stephen Hawkings in " + books[s].year)

# 出力
books = []
books.append(Book("How Did It All Begin?", "2021"))
books.append(Book("The Theory of Everything", "2010"))
books.append(Book("God Created the Integers", "2006"))

printBookArray(books)
