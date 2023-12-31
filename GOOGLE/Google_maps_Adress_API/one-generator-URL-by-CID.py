import urllib.parse

### PRIMER
# https://www.google.com/search?q=your+keyword+here&oq=your+keyword+here&rldimm=000000taregtCID00000&rlst=f#rlfi=hd:;si:0000YOURCID00000000
### CID Converter
# https://pleper.com/index.php?do=tools&sdo=cid_converter


KEYWORD = "купить матрас киев"
# купить ортопедический матрас киев, купить матрас киев
CID_TARGET_PLACE = 1217531233587440534
# 1217531233587440534 - Дарницкий район Киева
# 18050907804186843608 # Борисполь
# CID_MY_COMPANY = 13280552074301093291 # FreyaMebel
CID_MY_COMPANY = 8207621176809025478 # Instadivan

def fun_combi_url(KEYWORD, CID_TARGET_PLACE, CID_MY_COMPANY):
    encoded_str_keyword = urllib.parse.quote(KEYWORD.encode('utf-8'))
    combi_url = f"https://www.google.com/search?q={encoded_str_keyword}&oq={encoded_str_keyword}&rldimm={CID_TARGET_PLACE}&rlst=f#rlfi=hd:;si:{CID_MY_COMPANY}" 
    return combi_url

print_combi_url = fun_combi_url(KEYWORD, CID_TARGET_PLACE, CID_MY_COMPANY)
print(print_combi_url)


