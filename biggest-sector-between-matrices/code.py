import random    #use this library to create matrices with 100x100 size.



####create 10 matrices with 1000x1000 size with random values between 0 to 255.

#create a list of 10 names for matrices.
list_of_matrices_names = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j']     
all_matrices = {}      #Initilize dict of all matrices.
for matrice_name in list_of_matrices_names :  #Loop through each name in the list.
    lists = [[] , [] , [] , [] , [] ,[] , [] ,[] , [] , []]
    for matrice_values in lists :    #Loop through each list in the lists.
        for i in range(100) :     #Create 100 rows for each matrix.
            b = []
            for j in range(100) :    #Create 100 columns for each matrix.
                b.append(random.randint(0,255))      #Create a list with 100 random values between 0 to 255.
            matrice_values.append(b)
    all_matrices[matrice_name] = matrice_values        #Add each matrix to the dict with its name as key.



buffer_list = []

buffer = [[],[],[],[],[],[],[],[],[]]

for item in list_of_matrices_names[1:] :
    for i in range(len(all_matrices['a'])) :
        for j in range(len(all_matrices['a'][0])) :
            if all_matrices['a'][i][j] == all_matrices[item][i][j] :
                buffer[list_of_matrices_names.index(item) - 1].append(all_matrices['a'][i][j])





buffer2 = [{} , {} , {} , {} , {} , {} , {} , {} , {}]

for j in buffer :
    for i in j :
        if f"{i}" in buffer2[buffer.index(j)]:
            buffer2[buffer.index(j)][f"{i}"] += 1
        else:
            buffer2[buffer.index(j)][f"{i}"] = 1

result = {}
for i in buffer2 : 
    result[list_of_matrices_names[buffer2.index(i) + 1]] = sum(i.values())
print(result)

