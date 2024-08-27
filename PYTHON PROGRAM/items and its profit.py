items = [{'name':'item1','cost':20,'selling':100},
        {'name':'item2','cost':15,'selling':250}]
profit = {item['name']:item['selling']-item['cost']for item in items}
print(profit)
