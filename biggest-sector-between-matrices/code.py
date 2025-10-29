import random




list = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j']
dicts = {}
for shirin in list : 
    lists = [[] , [] , [] , [] , [] ,[] , [] ,[] , [] , []]
    for kh in lists :
        for i in range(1000) :
            b = []
            for j in range(1000) :
                b.append(random.randint(0,255))
            kh.append(b)
    dicts[shirin] = kh



buffer_list = []

buffer = [[],[],[],[],[],[],[],[],[]]

for item in list[1:] :
    for i in range(len(dicts['a'])) :
        for j in range(len(dicts['a'][0])) :
            if dicts['a'][i][j] == dicts[item][i][j] :
                buffer[list.index(item) - 1].append(dicts['a'][i][j])





buffer2 = [{} , {} , {} , {} , {} , {} , {} , {} , {}]

for j in buffer :
    for i in j :
        if f"{i}" in buffer2[buffer.index(j)]:
            buffer2[buffer.index(j)][f"{i}"] += 1
        else:
            buffer2[buffer.index(j)][f"{i}"] = 1

result = {}
for i in buffer2 : 
    result[list[buffer2.index(i) + 1]] = sum(i.values())
print(result)

