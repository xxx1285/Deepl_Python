# dict_id_clon_resouses = {"10": [1, 2, 3], "20": [4, 5, 6]}

# if "25" in dict_id_clon_resouses:
#     dict_id_clon_resouses["25"].append(33)
# else:
#     dict_id_clon_resouses["25"] = [33]

# print(dict_id_clon_resouses)
import re

s = "aviator aviator-gorup---"
s = re.sub(r'-+$', '', s)

d = "aviator aviator-gorup---"
d = re.sub(r'[^a-zA-Z0-9]+', '-', d)

w = "aviator aviator-gorup---"
w = re.sub(r'[^a-zA-Z0-9]+-*$' , '', re.sub(r'[^a-zA-Z0-9]+', '-', w))


print(s)
print(d)
print(w)









chan_locale = {

              'sv': '[[$sv_SE]]',

               'ar': '[[$ar_EG]]', 'az': '[[$az_AZ]]', 'kz': '[[$kz_KZ]]', 'uz': '[[$uz_UZ]]'
               }

context_and_lang = ["ru","es","pl","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et","lt","lv","nl",
                    "cs","da","ja","nb","sk","sl","sv"]
