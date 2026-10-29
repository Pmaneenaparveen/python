d = {'a': 3, 'b': 1, 'c': 2, 'd':2}
ascending = dict(sorted(d.items()))
print("Ascending order:", ascending)
descending = dict(sorted(d.items(), reverse=True))
print("Descending order:", descending)

