
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


def combinaisons_maker(actions, enveloppe):
    from itertools import combinations
    nb_actions = len(actions)
    all_combinaisons = []

    for i in range(1, nb_actions + 1):
        for combination in combinations(actions, i):
            total_buy_price = sum([a['initial_price'] for a in combination])
            total_price_prediction = sum([a['price_prediction'] for a in combination])
            if total_buy_price <= enveloppe:
                enveloppe_actions = {'combinaison': combination,
                                     'total_buy_price': total_buy_price,
                                     'total_price_prediction': int(total_price_prediction)}
                all_combinaisons.append(enveloppe_actions)
                #print(enveloppe_actions)

        best_combinaison = max(all_combinaisons, key=lambda x: x['total_price_prediction'])

    print(f'Voici la meilleure combinaison :{best_combinaison}')


combinaisons_maker(list_actions_prediction, 500)
