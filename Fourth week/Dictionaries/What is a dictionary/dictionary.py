x = {}
print(type(x))

file_counts = {"jpg" : 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts, file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)
file_counts["cfg"] = 8
print(file_counts)
file_counts["jpg"] = 10
print(file_counts)
del file_counts["jpg"]
print(file_counts)