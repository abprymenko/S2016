from limiterror import LimitError
class Checker:
    def __init__(self):
        pass
    def Check(self, amount, limit):
        strAmount = str(amount)
        strLimit = str(limit)
        if(not strAmount.isdigit() or not strLimit.isdigit()):
            raise ValueError("You have to enter integer digit!")
        if(int(amount) > int(limit)):
            raise LimitError(amount, limit)
        return True