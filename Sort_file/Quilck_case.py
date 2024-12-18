import timeit

start_time = timeit.default_timer()

def Quilck_revers(a_list, start, end):

    if start < end:

        pIndex = QuickSort_partition(a_list, start, end)
        
  
        Quilck_revers(a_list, start, pIndex - 1)
        
        
        Quilck_revers(a_list, pIndex + 1, end)
    
    return a_list
def QuickSort_partition(a_list, start, end):
    pivot = a_list[end]
    pIndex = start  

    for i in range(start, end):
        if a_list[i] >= pivot:
            
            temp = a_list[i]
            a_list[i] = a_list[pIndex]
            a_list[pIndex] = temp
            pIndex += 1

    temp = a_list[pIndex]
    a_list[pIndex] = a_list[end]
    a_list[end] = temp

    return pIndex

file = 'tambol'
list_file = []
with open(f'Sorting-Algorithm/Convert/{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())

list_reversed = Quilck_revers(list_file, 0, len(list_file) - 1)

output_file = f'Sorting-Algorithm/Sort_file/output/Quilck/{file}_Quilck.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
Timespent = timeit.default_timer() - start_time
print(f"{Timespent} seconds")

