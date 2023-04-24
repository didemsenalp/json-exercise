import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

name = vehicle.name
engine = vehicle.engine
price = vehicle.price

dict_of_data = {"name": name,"engine": engine,"price":price}
convert_to_json = json.dumps(dict_of_data, indent = 2)

print(convert_to_json)
