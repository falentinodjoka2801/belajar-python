try:
    5/0
except ZeroDivisionError as e:
    print('Zero Division Error')
    print(e)
    raise

#Reraise an exception means you try to trigger that exception one more time. It's for logging purposes.
#Logging means you could know what type of exception occurs.