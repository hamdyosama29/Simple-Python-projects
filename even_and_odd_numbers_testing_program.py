try:
    open = True
    while open:
        numbers = int(input('>>>>:'))
        math = numbers % 2
        if math == 0:
            print('Even number')
        elif math == 1:
            print('Odd number')
        else:
            open = False
except Exception as error:
    print(error)
