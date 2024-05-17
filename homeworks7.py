def print_params( a=1, b='str', c=True):
    print(a,b,c)
print_params(1, 'str', True)
print_params(b=25, c=[1,2,3])
valeus_list = ['str', 35, False]
valeus_dict = {'a': 325, 'b': 444, 'c': 525}
print_params(valeus_list, valeus_dict, c=True )
print_params(*valeus_list)
print_params(**valeus_dict)
valeus_list2 = [2, 42]
print_params(*valeus_list2, 42)