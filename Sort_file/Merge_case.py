import timeit

start_time = timeit.default_timer()

def Merge_revers(a_list):
    n = len(a_list)
    
    if n < 2:
        return a_list

    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    Merge_revers(left)
    Merge_revers(right)

    a = 0  
    s = 0  
    d = 0 

    while a < len(left) and s < len(right):
        if left[a] > right[s]:
            a_list[d] = left[a]
            a += 1
        else:
            a_list[d] = right[s]
            s += 1
        d += 1

    
    while a < len(left):
        a_list[d] = left[a]
        a += 1
        d += 1

    while s < len(right):
        a_list[d] = right[s]
        s += 1 
        d += 1

    return a_list

file = 'tambol'
list_file = []
with open(f'Sorting-Algorithm/Convert/{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        
list_reversed = Merge_revers(list_file)

output_file = f'Sorting-Algorithm/Sort_file/output/Merge/{file}_Merge.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
Timespent = timeit.default_timer() - start_time
print(f"{Timespent} seconds")
