from logexample import Logging
log = Logging()
while(True):
    try:
        digit1 = int(input("Enter digit1: "))
        digit2 = int(input("Enter digit2: "))
        log.Log(20, f"{digit1};\t{digit2}")
        print(digit1/digit2)
    except ZeroDivisionError as zde:
        log.Log(40, zde)
    except TypeError as te:
        log.Log(40, te)
    except Exception as ex:
        log.Log(40, ex)
    finally:
        yes = input("Do you want to try again?[y/n]: ")
        if(yes.lower() != 'y'):
            log.Log(20, "End!")
            break