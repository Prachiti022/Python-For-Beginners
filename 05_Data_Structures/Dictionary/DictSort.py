def sort_dict(d):
    asc = dict(sorted(d.items(), key=lambda item: item[1]))
    desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    
    print("Ascending Order:", asc)
    print("Descending Order:", desc)

data = {'a': 3, 'b': 1, 'c': 5, 'd': 2}
sort_dict(data)
