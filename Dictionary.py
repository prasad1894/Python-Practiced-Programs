Capitals = {'Bihar': 'Patna', 'Madhya Pradesh': 'Bhopal', 'Telangana': 'Hyderabad', 'Tamil Nadu': 'Chennai'}
Capitals.update({'Goa': 'Punjab'})
#print(Capitals.get('Bihar'))
#print(Capitals.pop('Telangana'))
#print(Capitals.keys())
#print(Capitals.values())
#print(Capitals.items())
#print(Capitals['Bihar'])
for key, value in Capitals.items():
    print(key, value)