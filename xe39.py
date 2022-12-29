# create a mapping of state to abberviation
states = {
    'oregon': 'or',
    'florida': 'fl',
    'california': 'ca',
    'newyork': 'ny',
    'michigan': 'mi'
}

# create abasic set of staes and some cities in them
cities = {
    'ca': 'sanfrancisco',
    'mi': 'detroit',
    'fl': 'jacksonville'
}

# add some more cities
cities['ny'] = 'newyork'
cities['or'] = 'portland'

# print some states
print('-' * 10)
print("ny state has: ", cities['ny'])
print("or state has: ", cities['or'])

# print some states
print('-' * 10)
print("maichigan's abbreviation is: ", states["michigan"])
print("florida's abbreviation is: ", states['florida'])

# do it by using the state then cities dict
print('-' * 10)
print("michigan has: ", cities[states['michigan']])
print("florida has: ", cities[states['florida']])

# print every city in state
print('-' * 10)
for state, abbrev in list(cities.items()):
    print(f"{state} has the city {abbrev}")
# print every city in state

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('texas')

if not state:
    print("sorry, no texas.")

#
city = cities.get('ts', 'does not exist')
print(f"the city the state 'tx' is: {city}")









































































