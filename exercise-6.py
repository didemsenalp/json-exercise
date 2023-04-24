import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
if __name__ == "__main__":
    vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

    parse = json.dumps(vehicle.__dict__, indent = 2)

    print(parse)
