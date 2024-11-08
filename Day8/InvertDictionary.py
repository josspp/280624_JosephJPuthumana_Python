dict_main={1:'a',2:'b',3:'c'}
dict_inv={}
print(dict_main)
for kv in dict_main:
    dict_inv[dict_main[kv]]=kv

print(dict_inv)