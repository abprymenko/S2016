class LimitError(Exception):
    def __init__(self, amount = 0, limit = 0):
        self.Amount = amount
        self.Limit = limit
    def __str__(self):
        return f"Dear customer unfortunetly you want {self.Amount} goods\n" \
               f"but we have only {self.Limit} goods\n" \
               f"If you want more than we have you have to wait 2 days\n" \
               f"Thank you."