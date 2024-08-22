items = [{'name': 'Item1', 'cost': 20, 'selling': 30}, 
         {'name': 'Item2', 'cost': 15, 'selling': 25}]

profits = {item['name']: item['selling'] - item['cost'] for item in items}
print(profits)
