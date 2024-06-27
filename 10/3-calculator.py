def plus(a, b):
    return a + b

def divide(a, b):
    return a / b

def minus(a, b):
    return a - b

def multy(a, b):
    return a * b

operationDict = {
    '+': plus,
    '/': divide,
    '-': minus,
    '*': multy
}

def calc(n1=None):
    if n1 is None:
        n1 = int(input('What is your first number: '))
    operation = input('What operation would you like to choose? ')
    n2 = int(input('What is your second number: '))
    return operationDict[operation](n1, n2)

answer = calc()

while True:
    user_continue = input(f"The result is {answer}! Would you like to continue with the result? Please choose 'yes' or 'no': ")
    if user_continue.lower() == 'no':
        print(f'Final answer is {answer}')
        break
    elif user_continue.lower() == 'yes':
        answer = calc(answer)  # Update answer with the result of calc
    else:
        print('Invalid input')
