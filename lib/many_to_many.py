class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f'<Author {self.name}>'

    def contracts(self):
        contracts = []
        for contract in Contract.all:
            if contract.author == self:
                contracts.append(contract)
        return contracts

    def books(self):
        books = []
        for contract in self.contracts():
            books.append(contract.book)
        return books

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def __repr__(self):
        return f'<Book {self.title}>'

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def __repr__(self):
        return f'<Contract {self.date}>'

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]