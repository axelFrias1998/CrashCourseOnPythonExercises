word = "mountains"
print(word.upper())
print(word.lower())
word = " yes "
print(word.strip())
print(word.lstrip())
print(word.rstrip())
phrase = "The number of time e occurs in this string is: "
print(phrase + str(phrase.count('e')))
word = "forest"
print(word.endswith("rest"))
number = "12345"
print(number.isnumeric())
print(' '.join(["this", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["this", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
print("this is another example".split())