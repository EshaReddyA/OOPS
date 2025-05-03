class Logger:
    @staticmethod
    def log_in_message(func):
        def wrapper():
            print("Logging in...")
            func()
        return wrapper
class User:
    @Logger.log_in_message
    def login():
        print("Welcome, user!")
User.login()

