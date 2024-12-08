try:
    print('EP:1')
    print('US:2')
    while True:
        inputone = int(input('Enter the currency you want to calculate:>>>: '))
        inputow = int(input('Enter the price you want to calculate:>>>: '))
        if inputone == 1:
            result = inputow / 48.73
            print(round(result, 2))
        elif inputone == 2:
            result = inputow * 48.73
            print(round(result, 2))
        else:
            print('--------------------------------------------------------')
            print('There is an error. Please check the steps you took. ')
except Exception as e:
    print(f'An error occurred: {e}')
