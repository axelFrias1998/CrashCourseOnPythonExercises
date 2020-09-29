fullname = ("Grace", "M", "Hopper")

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, remaining_seconds = convert_seconds(2000)
print(hours, minutes, remaining_seconds, type(convert_seconds(200)))
