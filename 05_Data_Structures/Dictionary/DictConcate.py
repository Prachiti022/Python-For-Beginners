def merge_dicts(d1, d2, d3):
    new_dict = d1.copy()  
    new_dict.update(d2)  
    new_dict.update(d3)  
    print("Concatenated Dictionary:", new_dict)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merge_dicts(dic1, dic2, dic3)
