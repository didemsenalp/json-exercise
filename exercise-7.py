import json  

str_of_data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

class Vehicle(object):
    def __init__(self, name, engine,price):
        self.name = name
        self.engine = engine
        self.price = price

dict_to_data = json.loads(str_of_data)
pass_the_parameter = Vehicle(**dict_to_data)

print(pass_the_parameter.name,pass_the_parameter.engine,pass_the_parameter.price)


    
