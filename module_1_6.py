my_dict = {'Roman': 2000, 'Denis': 2001, 'Oleg': 1980, 'Anton': 2020}
print(my_dict)
print(my_dict['Roman'])
my_dict['Max'] = 2003
print(my_dict['Max'])
my_dict.update({'Tom': 1917, 'Roben': 2007})
a = my_dict.pop('Denis')
print(a)
print(my_dict)

print()

my_set = {1, 2, 1, 2, 45, 17, 'den', 'den', 'oleg'}
print(my_set)
my_set.update([218, 6])
my_set.discard(45)
print(my_set)