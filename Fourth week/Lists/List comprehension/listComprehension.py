multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

multiples = [ x * 8 for x in range(1, 11) ]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java"]
lengths = [ len(language) for language in languages ]
print(lengths)

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)