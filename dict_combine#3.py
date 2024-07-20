def join_dictionaries(dict1, dict2, dict3):
    dict_final = {**dict1, **dict2, **dict3}
    return dict_final

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

print(join_dictionaries(dic1, dic2, dic3))