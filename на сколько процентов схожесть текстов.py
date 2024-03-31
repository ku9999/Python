from fuzzywuzzy import fuzz

# Пример сравнения двух строк на основе схожести
string1 = "блядсука"
string2 = "сука"
similarity = fuzz.ratio(string1, string2)
print(f"Схожесть: {similarity}%")

