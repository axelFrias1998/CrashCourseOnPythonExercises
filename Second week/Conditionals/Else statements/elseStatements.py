def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 chracters long")
    else:
        print("Valid username")

def is_even(number):
    if number % 2 == 0:
        return True
    return False