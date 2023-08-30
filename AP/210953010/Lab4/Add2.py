import json
data={
    'name':'Yashaswi',
    'age':19,
    'city':'Manipal'
}
json_string=json.dumps(data)
print('The string is: ',json_string)

print('The string converted back to a JSON object: ')

a=json.loads(json_string)

print(a)