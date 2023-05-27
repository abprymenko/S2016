'''
while(True):
    try:
        digit1 = int(input("Enter digit1: "))
        digit2 = int(input("Enter digit2: "))
        print(digit1 / digit2)
    except ZeroDivisionError as zde:
        print(zde)
        print("You have to enter digit2 that doesn't equal 0!")
    except ValueError as ve:
        print(ve)
        print("You have to enter only integer digits")
    except Exception as ex:
        print(ex)
    finally:
        yes = input("Do you want to continue?[Y/N]: ")
        if(yes.lower() != "y"):
            break
'''
from limiterror import LimitError
from checker import Checker
checker = Checker()
while(True):
    try:
        amount = input("Enter amount: ")
        limit = "5"#"y" ValueError
        if(checker.Check(amount, limit)):
            print("Your oder has proccessed successfull!")
    except ValueError as ve:
        print(ve)
    except LimitError as le:
        print(le)
    except Exception as ex:
        print(ex)
    finally:
        yes = input("Do you want to try again?[Y/N]: ")
        if (yes.lower() != "y"):
            break