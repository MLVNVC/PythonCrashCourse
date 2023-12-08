pizzas = ['Capriccosa', 'Pascatore', 'Quatro Stagione', 'Calcone']
friends_pizzas = pizzas[:]
print(pizzas)
print(friends_pizzas)
pizzas.append('Margharita')
friends_pizzas.append('Veggy')
print("My favorite pizzas are: ")
print(pizzas)
print("Friends favorite pizzas are: ")
print(friends_pizzas)
for pizza in pizzas:
    print("My favorite is: " + pizza.upper())
for zzapi in friends_pizzas:
    print("His favorite is: " + zzapi.upper())