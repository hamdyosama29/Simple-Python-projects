
while True:
    with open(r'C:\Users\Flash\Documents\Flash.txt', 'r+') as f:
        red = f.read().strip()
        if red:
            current_value = int(red)
        else:
            current_value = 0  
        print('1: Withdrawal')
        print('2: Deposit')
        print('-----------------------------')
        print('To exit theprogram, type exit')
        print('-----------------------------')
        check = input('What process do you want: ')
        if check == '1':
            enter = int(input('Enter the withdrawal anmount: '))
            result = current_value - enter

        elif check == '2':
            enter = int(input('Enter the deposit anmount: '))
            result = current_value + enter
        elif check == 'exit':
            break
        else:
            print('An error occurred, please try again')
            print('-----------------------------------')
            continue
        f.seek(0) 
        f.write(str(result))
        f.truncate()
    print('______________________________________________________')
    print(f"The previous number in the file was: {current_value}")
    print(f"The new total after addition is: {result}")
    print('______________________________________________________')
