the_count = [1, 2, 3, 4, 5]
fruits = ['people', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first king of for-loop goes though a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type; {fruit}")

#
for i in change:
    print(f"i got {i}")
#

elements = []

#
for i in range(0, 6):
    print(f"adding {i} to the list.")
    #
    elements.append(i)

#
for i in elements:
    print(f"element was: {i}")
