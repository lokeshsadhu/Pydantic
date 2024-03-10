import requests 
import json
from pprint import pprint
from models import Student,Module

# url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()
del data[-1]['date_of_birth']
# data.append({
#         "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
#         "name": "Eric Travis",
#         "date_of_birth": "2010-05-25",
#         "GPA": "5.0",
#         "course": "Computer Science",
#         "department": "Science and Engineering",
#         "fees_paid": False
#     })
# print(data)
# data[-1]['modules'].append({
#                 "id": 3,
#                 "name": "Relational Databases and SQL",
#                 "professor": "Prof. Samantha Curtis",
#                 "credits": 20,
#                 "registration_code": "abc"
#             })
    
for student in data:
    try:
        model=Student(**student)
        print(f"GPA:{model.GPA}, Department:{model.department}")
    except ValueError as e:
        print(e)
    
    # exclude_keys={
    #     'id':True,
    #     'modules':{'__all__':{'registration_code'}}
    # }
    # pprint(json.dumps(model.model_json_schema(), indent=2))
    # break
    # print(json.dumps(model.model_json_schema(), indent=2))
    # for module in model.modules:
    #     print(module.id)
    # print(model)

# print(json.dumps(Student.model_json_schema(), indent=2))