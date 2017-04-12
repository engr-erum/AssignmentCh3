pizza = ["peproni" , "chickenTIKKA" , "fajita"];
friend_pizzas = pizza[:];

print(pizza);
print(friend_pizzas);


pizza.append("New flavor original");
friend_pizzas.append("New friend pizza");

print("My Favorite Pizza's are:");
for items in pizza:
    print(items);

print("-----------------------------------");
print("My Friend's favorite Pizza's are:");
for items in friend_pizzas:
    print(items);

