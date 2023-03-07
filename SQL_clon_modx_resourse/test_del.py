dict_id_clon_resouses = {"10": [1, 2, 3], "20": [4, 5, 6]}

if "25" in dict_id_clon_resouses:
    dict_id_clon_resouses["25"].append(33)
else:
    dict_id_clon_resouses["25"] = [33]

print(dict_id_clon_resouses)
