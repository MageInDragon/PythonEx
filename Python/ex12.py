import json

num = int(0)
with open('data.json', 'r') as infile:
    data = json.load(infile)
    for i in data['events_data']:
        if((str(i['client_id']) == '62602') and (str(i['category']) == 'page')):
            num += 1
print(num)
            
            
