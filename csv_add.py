import pickle

data = ("Alice má kočky")


with open("Alice.csv", "wb") as f:
    pickle.dump(data, f)
