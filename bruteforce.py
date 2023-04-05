
actions_list = [
    {'name': 'Action-1', 'price': 20, 'profits': 5},
    {'name': 'Action-2', 'price': 30, 'profits': 10},
    {'name': 'Action-3', 'price': 50, 'profits': 15},
    {'name': 'Action-4', 'price': 70, 'profits': 20},
    {'name': 'Action-5', 'price': 60, 'profits': 17},
    {'name': 'Action-6', 'price': 80, 'profits': 25},
    {'name': 'Action-7', 'price': 22, 'profits': 7},
    {'name': 'Action-8', 'price': 26, 'profits': 11},
    {'name': 'Action-9', 'price': 48, 'profits': 13},
    {'name': 'Action-10', 'price': 34, 'profits': 27},
    {'name': 'Action-11', 'price': 42, 'profits': 17},
    {'name': 'Action-12', 'price': 110, 'profits': 9},
    {'name': 'Action-13', 'price': 38, 'profits': 23},
    {'name': 'Action-14', 'price': 14, 'profits': 1},
    {'name': 'Action-15', 'price': 18, 'profits': 3},
    {'name': 'Action-16', 'price': 8, 'profits': 8},
    {'name': 'Action-17', 'price': 4, 'profits': 12},
    {'name': 'Action-18', 'price': 10, 'profits': 14},
    {'name': 'Action-19', 'price': 24, 'profits': 21},
    {'name': 'Action-20', 'price': 114, 'profits': 18},
]

list_actions_prediction = []
for action in actions_list:
    profit = action['profits']
    value = int(action['price'])
    if profit < 10:

        price_prediction = value * (profit/100+1)
    else:
        price_prediction = value * (profit/100+1)

    action_prediction = {'name': action['name'],
                         'initial_price': action['price'],
                         'price_prediction': round(price_prediction, 2)}
    list_actions_prediction.append(action_prediction)

print(list_actions_prediction)
