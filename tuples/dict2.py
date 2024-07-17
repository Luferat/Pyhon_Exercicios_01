car = { "brand": "Ford", "model": "Mustang", "year": 1964 }

x = car.keys()

print(1, x) #before the change

car["color"] = "white"

print(2, x) #after the change

print(car.keys())  # Retorna as chaves na forma de uma list

print(car.values())  # Retorna os valores na forma de uma list

print(4, car.items())  # Retorna as chaves e valores na forma de uma list de tuples