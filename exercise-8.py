import json

def validateJson(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        print("It is invalid data")
        return False
    return True

invalid_Data = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}"""
isValid = validateJson(invalid_Data)

print(isValid)