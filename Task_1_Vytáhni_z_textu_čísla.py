import re

text = "test43543lfdsfdslf534543fdgl432fr"

seznam = re.findall(r"\d+", text) # pro vytáhnutí číslic samostatně pattern: [0-9]
print (seznam)

seznam_1 = re.findall(r"[a-zA-Z]", text)
print(seznam_1)