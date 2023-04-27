import csv
import time


with open('dataset2_Python+P7.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    actions_list = []
    for row in reader:
        action = {
            'name': row['name'],
            'price': float(row['price']),
            'profit': float(row['profit'])
        }
        actions_list.append(action)

start_time = time.time()


def combinaison_knapsack(actions, enveloppe):
    list_actions_prediction = []
    for action in actions:
        profit = action['profit']
        value = action['price']

        price_prediction = value * (profit / 100 + 1)

        action_prediction = {'name': action['name'],
                             'initial_price': action['price'],
                             'price_prediction': round(price_prediction, 2)}
        list_actions_prediction.append(action_prediction)

    list_actions_prediction = sorted(list_actions_prediction,
        key=lambda x: x['price_prediction'] / x['initial_price'] if x['initial_price'] != 0 else 0, reverse=True)
    total_value = 0
    total_weight = 0
    selected_actions = []
    for action in list_actions_prediction:
        if action['price_prediction'] > 0 and total_weight + action['initial_price'] <= enveloppe:
            selected_actions.append(action['name'])
            total_value += action['price_prediction']
            total_weight += action['initial_price']
            profit = total_value - total_weight

    print(f"La combinaison d'actions dans la limite d'un budget de {enveloppe} est : {selected_actions}.\n"
          f"Valeur initiale totale : {total_weight}\n"
          f"Valeur estimée dans 2 ans : {total_value}\n"
          f"Profit total : {profit}"
          )

    return selected_actions


combinaison_knapsack(actions_list, 500)

end_time = time.time()
duration_time = end_time - start_time
print("Durée d'exécution : {:.2} secondes".format(duration_time))
