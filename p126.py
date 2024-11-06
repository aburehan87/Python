#NESTED DICTIONARY
#using nested dictionary

p={"name":"Amit","roll":101,"age":25}
b={"company":"Vespa","cost":90000}
d={"person":p, "bike":b}


for v in d.values():
    print(v)