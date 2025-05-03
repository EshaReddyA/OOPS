class Lines:
    @staticmethod
    def add_lines(func):
        def wrapper():
            print("------")
            func()
            print("------")
        return wrapper
class Message:
    @Lines.add_lines
    def show():
        print("Welcome to Python!")
Message.show()
