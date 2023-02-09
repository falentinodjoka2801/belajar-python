while True:
    try:
        age =   int(input('Enter your age please ..\n'))
        print(age)
        break
    except (ValueError):
        print('Please input a valid age (correct number)')