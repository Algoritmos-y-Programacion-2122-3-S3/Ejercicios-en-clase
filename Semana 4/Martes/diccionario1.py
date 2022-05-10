currency = {'Euro':'E', 'Dollar':'$', 'Yen':'Y'}
currency_selected = input("Please enter a currency\nEuro - E\nDollar - $\nYen - Y\n")
print(currency.get(currency_selected, "The currency was not found"))