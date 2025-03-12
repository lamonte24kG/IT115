#import json library
import json

#create json dictionary
data1 = {
    
    'name': 'LaMonte Golden',
    'age':54,
    'city': 'Seattle,WA',
    'interest': ['music', 'football', 'drawing', 'politics'],
    'is_student': True



}

#create json_file
with open('data1.json', 'w') as json_file:
    #dump data1 into json_file
    json.dump(data1,json_file,indent=4)

print("you have successfully written to data1.")

