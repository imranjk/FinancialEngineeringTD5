# This is a sample Python script.
#At first, It was impossible for us to implement a code on github. So we made the code before on anaconda. Then, one of us got success on github.
#So we copied and pasted our code :
from functools import total_ordering


### BOOK OBJECTS ###
class Book:
    def __init__(self, name):
        self.name = name
        self.orderB = []
        self.orderS = []
        self.c = 1

    def insert_buy(self, quantity, price):
        id = self.c
        theorder = Order(quantity, price, id)
        if len(self.orderB) == 0:
            self.orderB.append(theorder)
        else:
            for i in range(len(self.orderB)):
                theorder2 = self.orderB[i]
                if theorder.price > theorder2.price:
                    self.orderB.insert(i, theorder)
                    break
                elif i == len(self.orderB) - 1:
                    self.orderB.append(theorder)
        transac = 'buy'
        self.display(theorder, transac)
        self.c += 1

    def insert_sell(self, quantity, price):
        id = self.c
        theorder = Order(quantity, price, id)
        if len(self.orderS) == 0:
            self.orderS.append(theorder)
        else:
            for i in range(len(self.orderS)):
                theorder2 = self.orderS[i]
                if theorder.price < theorder2.price:
                    self.orderS.insert(i, theorder)
                    break
                elif i == len(self.orderS) - 1:
                    self.orderS.append(theorder)
        transac = 'sell'
        self.display(theorder, transac)
        self.c += 1

    def display(self, theorder, transac):
        if transac == 'buy':
            print("--- Insert BUY", theorder, "id =", theorder.id, "on", self.name, '\n')
        else:
            print("--- Insert SELL", theorder, "id =", theorder.id, "on", self.name, '\n')

        while ((self.orderB != [] and self.orderS != []) and (self.orderB[0] >= self.orderS[0])):
            if self.orderB[0].quantity > self.orderS[0].quantity:
                print("Execute", self.orderS[0].quantity, "at", self.orderB[0].price, "on", self.name, '\n')
                self.orderB[0].quantity = self.orderB[0].quantity - self.orderS[0].quantity
                del self.orderS[0]

            else:
                print("Execute", self.orderB[0].quantity, "at", self.orderB[0].price, "on", self.name, '\n')
                self.orderS[0].quantity = self.orderS[0].quantity - self.orderB[0].quantity
                del self.orderB[0]

        print("Book on", self.name, '\n')
        for theorderS in self.orderS:
            print("     SELL", theorderS, "id =", theorderS.id, '\n')
        for theorderB in self.orderB:
            print("     BUY", theorderB, "id =", theorderB.id, '\n')
        print("------------------------", '\n')


### ORDER OBJECTS ###
@total_ordering
class Order:
    def __init__(self, quantity, price, id):
        self.quantity = quantity
        self.price = price
        self.id = id

    def __eq__(self, other):  # describes equality operator
        return other and self.quantity == other.quantity and self.price == other.price

    def __lt__(self, other):  # describes less than operator
        return other and self.price < other.price

    def __str__(self):
        return "%s@%s" % (self.quantity, self.price)


def main():
    book = Book("TEST")
    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)
    book.insert_buy(2, 11.0)
    book.insert_sell(1, 10.0)
    book.insert_sell(10, 10.0)


if __name__ == "__main__":
    main()

