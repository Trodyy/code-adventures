import random    #use this library to create matrices with 100x100 size.


array_size = int(input("input the size of matrix : "))

####create 10 matrices with 1000x1000 size with random values between 0 to 255.

#create a list of 10 names for matrices.
list_of_matrices_names = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j']     
all_matrices = {}      #Initilize dict of all matrices.
for matrix_name in list_of_matrices_names :  #Loop through each name in the list.
    lists = [[] , [] , [] , [] , [] ,[] , [] ,[] , [] , []]
    for matrix_values in lists :    #Loop through each list in the lists.
        for rows in range(array_size) :     #Create 100 rows for each matrix.
            b = []
            for elements in range(array_size) :    #Create 100 columns for each matrix.
                b.append(random.randint(0,255))      #Create a list with 100 random values between 0 to 255.
            matrix_values.append(b)
    all_matrices[matrix_name] = matrix_values        #Add each matrix to the dict with its name as key.



list_of_same_elements = [[],[],[],[],[],[],[],[],[]]   

for item in list_of_matrices_names[1:] :
    for i in range(len(all_matrices['a'])) :
        for j in range(len(all_matrices['a'][0])) :     #Loop through each element in matrix 'a'.
            if all_matrices['a'][i][j] == all_matrices[item][i][j] :#Compare each element in matrix 'a' with the corresponding element in the other matrices.

                #If the elements are the same, add the element to the list of same elements.
                list_of_same_elements[list_of_matrices_names.index(item) - 1].append(all_matrices['a'][i][j])   
                 





reducer = [{} , {} , {} , {} , {} , {} , {} , {} , {}]

#Reduce the list of same elements to a dict with the count of each element.
for j in list_of_same_elements :
    for i in j :
        if f"{i}" in reducer[list_of_same_elements.index(j)]:   #If the element is already in the dict, increment its count by 1.
            reducer[list_of_same_elements.index(j)][f"{i}"] += 1   #Increment the count of the element by 1.
        else:             #If the element is not in the dict, add it with a count of 1.
            reducer[list_of_same_elements.index(j)][f"{i}"] = 1    #Add the element to the dict with a count of 1.

result = {}
for i in reducer :    #Loop through each dict in the reducer list.
    result[list_of_matrices_names[reducer.index(i) + 1]] = sum(i.values())   #Sum the counts of each element in the dict and add it to the result dict with the matrix name as key.
print(result)     #Print the result dict.

