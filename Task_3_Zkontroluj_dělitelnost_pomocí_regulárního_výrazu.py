import re

    # Dělitelné deseti

two_numbers = "156,153,1486,1456,13,2,1,54,87".split(",")

ten_numbers = "123,100,50,354,12545,1215,2131,1010,0". split(",")
print(ten_numbers)

for ten in ten_numbers:
    print(f"{ten} je {bool(re.fullmatch(r"\d*0", ten))}")


for two in two_numbers:
    print(f"{two} je {bool(re.fullmatch(r"\d*[0248]", two))}")