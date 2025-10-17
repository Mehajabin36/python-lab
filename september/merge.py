print("MERGING OF TWO DICTIONARIES")
dict1={}
dict2={"name":"mehajabin","dob":2004,"class":"mca"}
print(dict2)
dict3={"place":"kkm","age":21}
print(dict3)
dict4=dict2.copy()
dict4.update(dict3)
print("dictionaries after meging:",dict4)
