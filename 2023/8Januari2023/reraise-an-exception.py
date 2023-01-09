# def example():
#     try:
#         int('N/A')
#     except ValueError:
#         print('Did not work')
#         raise

# example()

try:
    5/0
except ZeroDivisionError as e:
    raise ZeroDivisionError('Got an error', e)

#Reraise an exception for logging purpose. If you want to inspect it, you could use
#this concept. Or you could use this concept to make your programs have an issue warning message
#for example about deprecated features or usage problem