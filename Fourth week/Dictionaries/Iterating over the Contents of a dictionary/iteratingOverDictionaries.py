file_counts = {"jpg": 10, "txt":14, "csv":2, "py":23 }
for extension in file_counts:
    print(extension)

for extension, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, extension))

hola = "Hola"
hola.replace()
hola.isle
print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("Hello world!"))
print(count_letters("A long string with a lot of letters"))