capitals = {"USA":'Washington DC', "India":"New Delhi","Russia":'Moscow' }

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'LA'})
capitals.pop('Russia')

print(capitals["India"])
print(capitals.get('Russia'))
print((capitals.keys()))
print(capitals.values())
print(capitals.items())
capitals.clear()
for key,value in capitals.items():
    print((key,value))