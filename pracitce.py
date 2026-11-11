#Coddy membership program
# Create a program that receives two lists and prints
# a new list of all elements that are in the first list but NOT in the second list.
def membership():
    lst1 = [1,2,3,4,5]
    lst2 = [2,4,6]

    result =[]
    for char in lst1:
        if char not in lst2:
            print('hi')
            result.append(char)
        else:
            print('bye')

    print(result)

print('hi')


