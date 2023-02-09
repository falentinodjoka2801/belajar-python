def only_ints(first, second):
    if type(first) == int and type(second) == int :
        return True

    return False

print(only_ints(1, "1"))