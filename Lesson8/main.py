from logexample import Logging
log = Logging()
while(True):
    try:
        digit1 = int(input("Enter digit1: "))
        digit2 = int(input("Enter digit2: "))
        log.Message = f"{digit1};\t{digit2}"
        log.Log(20)
        print(digit1/digit2)
    except ZeroDivisionError as zde:
        log.Message = zde
        log.Log(40)
    except TypeError as te:
        log.Message = te
        log.Log(40)
    except Exception as ex:
        log.Message = ex
        log.Log(40)
    finally:
        yes = input("Do you want to try again?[y/n]: ")
        if(yes.lower() != 'y'):
            log.Message = "End!"
            log.Log(20)
            break