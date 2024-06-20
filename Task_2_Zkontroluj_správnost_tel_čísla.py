import re



numbers = "516615132154,420486453154,414554855,186422".split(",")
print(numbers)

 # tel_number = re.findall(r"[0-9]{9}", numbers)
for num in numbers:
    print(f"{num} {bool(re.fullmatch(r"(420)?[0-9]{9}", num))}")




