def my_decor(func):
    def my_wrapper():
        print("Something before my_wrapper")
        func()
        print("Something after my func")
    return my_wrapper()

@my_decor
def my_hi():
    print("Hello")

