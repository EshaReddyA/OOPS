class Decorators:
    @staticmethod
    def start_end(func):
        def wrapper():
            print("Start")
            func()
            print("End")
        return wrapper

class Greeter:
    @Decorators.start_end
    def greet():
        print("Hello!")

Greeter.greet()

