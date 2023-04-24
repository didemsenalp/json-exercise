import json

json_str_data = '''[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]'''

list_of_data = json.loads(json_str_data)


for dict_value_and_key in list_of_data:
    print(dict_value_and_key)
    convert_to_dict = dict(dict_value_and_key)
    for key,value in convert_to_dict.items():
        if key == 'name':
            print(key,value)
        
        

