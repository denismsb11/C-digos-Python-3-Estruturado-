algo = input("Digite algo: ")
print("O tipo primitivo de algo é ", type(algo)) # A função input sempre retorna uma String
print("Só tem espaço? ", algo.isspace()) # Retorna um boolean
print("É um numero? ", algo.isnumeric()) # Retorna um boolean
print("É alfabético? ", algo.isalpha()) # Retorna um boolean
print("É alfanumerico? ", algo.isalnum()) # Retorna um boolean
print("Possui somente letras maiusculas? ", algo.isupper()) # Retorna um boolean
print("Possui somente letras minusculas? ", algo.islower()) # Retorna um boolean
print("Esta captalizada? ", algo.istitle()) # Retorna um boolean
# algo é um objeto
# ***.metodo -> tudo quem vem após "." é um metodo. Ex: isupper

