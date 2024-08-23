import random


current_number = random.randint(1, 12)


class NumberTooSmallError(Exception):
    pass


class NumberTooLargeError(Exception):
    pass


while 1:
    try:
        num = int(input("Enter a number to check: "))
        if num < current_number:
            raise NumberTooSmallError("too small")
        elif num > current_number:
            raise NumberTooLargeError("too big")
        else:
            print("even")
            break
    except NumberTooSmallError as error:
        print(error)
    except NumberTooLargeError as error:
        print(error)
    except ValueError:
        print("you did not provide any number")
