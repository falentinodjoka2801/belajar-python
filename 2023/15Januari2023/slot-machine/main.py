import random

MAX_LINES   =   3
MAX_BET     =   100
MIN_BET     =   1

ROWS    =   3
COLS    =   3

symbolCount =   {
    'A' :   2,
    'B' :   4,
    'C' :   6,
    'D' :   8
}

def deposit():
    while True:
        amount  =   input('What would you like to deposit? $')
        if amount.isdigit():
            amount  =   int(amount)
            if amount >= 1:
                break
            else:
                print('Amount must be greater than zero!')
        else:
            print('Please enter a number!')

    return amount

def getNumberOfLines():
    while True:
        numberOfLines   =   input(f'Enter the number of lines to bet on (1-{MAX_LINES})? ')
        if numberOfLines.isdigit():
            numberOfLines  =   int(numberOfLines)
            if 1 <= numberOfLines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines!')
        else:
            print('Please enter a number!')
    
    return numberOfLines

def getBet():
    while True:
        bet   =   input('What would you like to bet on each line? $')
        if bet.isdigit():
            bet  =   int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Bet must be between ${MIN_BET} - ${MAX_BET}!')
        else:
            print('Please enter a number!')
    
    return bet

def getSlotMachineSpin(rows, cols, symbols):
    allSymbols  =   []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns =   []
    for _ in range(cols):
        column  =   []
        currentSymbols  =   allSymbols[:]
        for _ in range(rows):
            value   =   random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def printSlotMachine(columns):
    itemLength  =   len(columns[0])
    for row in range(itemLength):
        for i, column in enumerate(columns):
            isLastIndex =   i == (itemLength - 1)
            endOfRows   =   '|'
            if isLastIndex:
                endOfRows   =   ''
            
            item        =   column[row] 
            print(f'{item}', end=endOfRows)
        print()

def main():
    balance         =   deposit()
    numberOfLines   =   getNumberOfLines()

    while True:
        bet         =   getBet()
        totalBet    =   bet * numberOfLines
        if totalBet > balance:
            print(f'You do not have enough to bet that amount, your current balance is ${balance}')
        else:
           break

    print(f'You are betting ${bet} on {numberOfLines} lines. Total bet is equal to ${totalBet}')

    slots   =   getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)
try:
    main()
except KeyboardInterrupt:
    print('\n')
    print('You close the program!')