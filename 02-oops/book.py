class Book:
    def __init__(self, name, copies=0):
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much


# copies
# increase_copies
# decrease_copies

the_art_of_computer_programming = Book('The Art of Computer Programming')
learning_python = Book('Learning Python in 100 Steps', 100)
learning_restful_services = Book('Learning RestFul Service in 50 Steps')

# print(the_art_of_computer_programming.name)
# print(learning_python.name)
# print(learning_restful_services.name)

learning_python.increase_copies(25)
learning_python.decrease_copies(10)
learning_python.copies = 50

print(learning_python.copies)