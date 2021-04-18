clothes = ["socks", "shirt", "skirt", "scarf"]

def insert_element(new_cloth,index=0):
    clothes.insert(index,new_cloth)

insert_element("jacket",2)
print(clothes)
insert_element("sweater",-2)
print(clothes)
insert_element("jeans")
print(clothes)

