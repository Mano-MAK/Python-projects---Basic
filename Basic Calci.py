def add(a, b):
    answer = a + b
    print(str(a) + '+' + str(b) + '=' + str(answer) + '\n')

def sub(a, b):
    answer = a - b
    print(str(a) + '-' + str(b) + '=' + str(answer) + '\n')

def mul(a, b):
    answer = a * b
    print(str(a) + '*' + str(b) + '=' + str(answer) + '\n')

def div(a, b):
    answer = a / b
    print(str(a) + '/' + str(b) + '=' + str(answer) + '\n')
    
# from the above code, we have added the '\n', to have a little space between these operations.
# we have added the str operation to view the output more clearly.
    
while True:
    print('A. add')
    print('B. sub')
    print('C. mul')
    print('D. div')
    print('E. exit')

    choice=input('input of your choice:')

    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('enter the value for a :'))
        b = int(input('enter the value for b :'))
        add(a, b)

    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('enter the value for a :'))
        b = int(input('enter the value for b :'))
        sub(a, b)

    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('enter the value for a :'))
        b = int(input('enter the value for b :'))
        mul(a, b)

    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('enter the value for a :'))
        b = int(input('enter the value for b :'))
        div(a, b)

    elif choice == 'e' or choice == 'E':
        print('program ended')
        quit()
