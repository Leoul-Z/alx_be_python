# main.py
from book_class import Book
from library_system import Book as BaseBook, EBook, PrintBook, Library
from polymorphism_demo import Rectangle, Circle
from class_static_methods_demo import Calculator


def run_magic_methods_demo():
    print("\n--- Task 0: Magic Methods Demo ---")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)          # __str__
    print(repr(my_book))    # __repr__
    del my_book             # __del__


def run_inheritance_composition_demo():
    print("\n--- Task 1: Inheritance & Composition Demo ---")
    my_library = Library()
    classic_book = BaseBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


def run_polymorphism_demo():
    print("\n--- Task 2: Polymorphism Demo ---")
    shapes = [Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


def run_class_static_methods_demo():
    print("\n--- Task 3: Class vs Static Methods Demo ---")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    run_magic_methods_demo()
    run_inheritance_composition_demo()
    run_polymorphism_demo()
    run_class_static_methods_demo()
