for x in range(25):
    print(x)

for x in [25]:
    print(x)

#for x in 25:
#    print(x)

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(["Axel", "Mariana", "Mariel", "Bryan"])