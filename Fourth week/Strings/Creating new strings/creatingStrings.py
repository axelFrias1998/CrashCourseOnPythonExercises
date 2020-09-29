message = "A kong string with a silly typo"
#message[2] = "l"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
message = "This is a new message"
print(message)
message = "And another one"
print(message)

pets = "Cats and dogs"
print(pets.index("and"))
print(pets.index('s'))

print ("Dragons" in pets)

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("axel.frias257@gmail.com", "gmail.com", "gamba.com"))
print(replace_domain("prueba@gamba.com", "hola.com", "gamba.com"))
