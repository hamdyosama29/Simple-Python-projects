try:
    cal = True
    while cal:
        enter = input(':>>:')
        if enter == 'exit':
            cal = False
        elif '/' in enter:  
            new_enter = enter.replace('/', '//')
            print(int(new_enter))
        else:
            print(int(enter))
except Exception as e:
    print(f'حدث خطأ: {e}')
