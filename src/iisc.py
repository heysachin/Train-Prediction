

# Created by Sachin Dev on 28/06/18

def counts(list_of_numbers,ind):
    x=[0]
    while i<ind:
        while k<ind:
            if list_of_numbers[k]<list_of_numbers[i]:
                x.append(list_of_numbers[k])
    return len(x)

    # x=[i for i in list_of_numbers if i < list_of_numbers[ind]]
    # return len(x)


test_case = int(input())


for i in range(test_case):
    print("Test")
    print(i)
    array_elements_count = int(input())
    a = [None] * array_elements_count
    count = [0] * array_elements_count
    for x in range(array_elements_count):
        a[x] = int(input())
    for y in range(array_elements_count):
        count[y] = counts(a,y)
    print(count)

