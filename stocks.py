stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]



for stock_tuple in purchases:
    if stock_tuple[0] in stockDict.keys():
        stock_name = stockDict[stock_tuple[0]]
        full_purchase_price = stock_tuple[1]*stock_tuple[3]
    print(f"I purchased {stock_name} stock for ${full_purchase_price}.")

print()
purchaseDict = dict()

for purchase in purchases:
    if purchase[0] in purchaseDict.keys():
        to_add = purchase[1]*purchase[3]
        purchaseDict[purchase[0]] += to_add
    else:
        purchaseDict[purchase[0]]= (purchase[1]*purchase[3])

for (stock, total) in purchaseDict.items():
    print(f"------ {stock} ------")
    for purchase in purchases:
        if purchase[0] == stock:
            print(f"{purchase[1]} shares at {purchase[3]} dollars each on {purchase[2]}")
    print()
    print(f"Total value of stock in portfolio: ${total}")
    print()

