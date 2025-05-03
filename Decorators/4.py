class LogAction:
    @staticmethod
    def log(func):
        def wrapper():
            print("Action starting...")
            func()
            print("Action completed..")
        return wrapper

class WashingMachine:
    
    @LogAction.log
    def turn_on():
        print("Washing machine is now ON")

    @LogAction.log
    def turn_off():
        print("Washing machine is now OFF")

WashingMachine.turn_on()
WashingMachine.turn_off()
