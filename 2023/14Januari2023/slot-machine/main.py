import random

MAX_LINES   =   3
MAX_BET     =   100
MIN_BET     =   1

ROWS    =   3
COLS    =   3

symbolCount     =   {
    'A' :   2,
    'B' :   4,
    'C' :   6
}

def getSlotMachineSpin(rows, cols, symbols):
    pass

def deposit():
    while True:
        amount  =   input('What would you like to deposit? $')
        if amount.isnumeric():
            amount  =   int(amount)
            if amount >= 1:
                break
            else:
                print('Amount must be greater than 0!')
        else:
            print('Please enter a number!')
    
    return amount

def getNumberOfLines():
    while True:
        lines   =   input(f'Enter the number of lines to bet on (1-{MAX_LINES})? ')
        if lines.isnumeric():
            lines   =   int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number!')

    return lines

def getBet():
    while True:
        bet   =   input(f'What would you like to bet on each line? $')
        if bet.isnumeric():
            bet   =   int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET}-${MAX_BET}')
        else:
            print('Please enter a number!')

    return bet

def main():
    balance         =   deposit()
    numberOfLines   =   getNumberOfLines()
    
    while True:
        bet         =   getBet()
        totalBet    =   bet * numberOfLines

        if balance >= totalBet:
            break
        else:
            print(f'You do not have enough to bet that amount, your current balance is ${balance}')

    print(f'You are betting ${bet} on {numberOfLines} lines. Total bet is equal to ${totalBet}')

try:
    main()
except KeyboardInterrupt:
    print('\n')
    print('--- You close the program ---') 