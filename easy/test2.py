places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

# Using a normal function:

def names_of(place):
    if len(place) > 2:
        return True
    else:
        return False
places_list = list(filter(names_of, places))
print(places_list)


# Using a Lambda function:

lambda_places = list(filter(lambda a: True if len(a) > 2 else False,places))
print(lambda_places)


