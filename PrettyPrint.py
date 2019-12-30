#!/usr/bin/python
import pprint

my_hash = {
    'Jan': ["London", "Lisbon"],
    'Feb': "my_string",
    'Mar': 3,
    'Apr': [1,4],
    'May': [(1, 2, 3), 56, 78]
}
print(my_hash)
pprint.pprint(my_hash)
