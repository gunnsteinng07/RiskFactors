def get_dimensions():
    '''Ask players how many dimensions the game should be. Has to be >= 3. If input Returns number of dimensions.'''
    dimensions = int(input("How many dimensions: "))
    return dimensions

def make_temp_list(x, y):
    temp_list = []
    for j in range(x, y):
        temp_list.append(j)
    return temp_list

def make_dimensions_list(dimensions):
    x = 1
    dimensions_list = []
    while x <= dimensions:
        start = 1
        end = dimensions + 1
        for i in range(start, end):
            temp_list = make_temp_list(start, end)
            dimensions_list.append(temp_list)
            x += 1
            start += dimensions
            end += dimensions
    return dimensions_list



# nota þetta hér til að prufa það sem ég er kominn með.
# uppfæri eftir því hvað ég er að prufa.
dimensions = get_dimensions()
dimensions_list = make_dimensions_list(dimensions)

print(dimensions_list)
