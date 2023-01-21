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

symbolValue =   {
    'A' :   5,
    'B' :   4,
    'C' :   3,
    'D' :   2
}

def checkWinnings(columns, lines, bet, values):
    for line in range(lines):
        symbol  =   columns[0][line]
        for column in columns:
            symbolToCheck   =   column[line]
            if symbol != symbolToCheck:
                break

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
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()

def deposit():
    while True:
        amount  =   input('What would you like to deposit? $')
        if amount.isdigit():
            amount  =   int(amount)
            if amount >= 1:
                break
            else:
                print('Amount must be greater than or equal to 1')
        else:
            print('Please enter a number')

    return amount

def getNumberOfLines():
    while True:
        lines   =   input(f'Enter the number of lines to bet on (1-{MAX_LINES})? ')
        if lines.isdigit():
            lines   =   int(lines)
            if lines >= 1 and lines <= MAX_LINES :
                break
            else:
                print(f'Please enter a valid number of lines : 1 to {MAX_LINES}')
        else:
            print('Please enter a number')

    return lines

def getBet():
    while True:
        bet     =   input('What would you like to bet on each line? $')
        if bet.isdigit():
            bet =   int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Please enter a number')
    
    return bet

def main():
    balance =   deposit()
    lines   =   getNumberOfLines()

    while True:
        bet     =   getBet()
        
        totalBet    =   bet * lines
        if totalBet > balance:
            print(f'You do not have enough to bet that amount, your current balance is ${balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}')

    slots   =   getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)

main()