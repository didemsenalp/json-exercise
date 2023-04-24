import json  

str_of_data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

class Vehicle(object):
    def __init__(self, name, engine,price):
        self.name = name
        self.engine = engine
        self.price = price

dict_of_data = json.loads(str_of_data)
    
pass_parameters = Vehicle(**dict_of_data)

print (pass_parameters.name, pass_parameters.engine, pass_parameters.price)