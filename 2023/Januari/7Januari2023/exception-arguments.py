try:
    raise Exception('Falentino', 'Andrian', 'Fery', 'Robby')
except Exception as e:
    print(e.args)