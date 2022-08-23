place = {
    'name': 'Bluebird pub',
    'post_code': 'D01 3WN',
    'street_number': 12,
    'location':{
        'longitude': 1221,
        'latitude': -3123,
    }
}

print(place.keys())
place['location']

pets = [{'name': 'Banzé', 'age': 13, 'breed':'schnauzer'},
        {'name': 'Spyro', 'age': 4, 'breed':'sausage lab'},]
for pet in pets:
    print(pet['name'], ", the", pet['breed'])
