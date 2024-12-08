# Dictionaries on python 
# key Value
# Bug 
# Function
# Loop


x={"key": 1,"value":3}
x["value"]

print(x["value"])
print(x['key'])

x["key"]=5
print(x['key'])

x['loop']='hello'

print(x)


empty_list={}
empty_list['loop']='this loop'
empty_list['function']='this is function'
empty_list['key']=1


for key in empty_list:
    print(key)
# empty_list['loop']=empty_list['notloop']

# normal Dictionaries
capitals={
    'France':'Paris',
    'Germany':'Berlin'
}

# Nested List in Dictionary
Travel_log={
    "France":['Paris','Lille','Dijon'],
    "Egypt":['Alexandria','Cairo']
}

# for key in Travel_log['Egypt']:
for key in Travel_log['Egypt']:
    print(key)
print(Travel_log['Egypt'][1])


# list
Travel=[
    ["A","B"]
    ,["C","D"]
]
print(Travel[0][1])
# print(Travel_log['Egypt'][1])
# Dictionaries on python 
Travel_logs={
    'Egypt':['alex','cairo'],
    'UAE':['SHJ','Dubai']
}