
import timeit

start_time = timeit.default_timer()
def Selection_revers(a_list):
    n = len(a_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a_list[j] > a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

    return a_list


file = 'amphoe' #เปลี่ยนชื่อไฟล์ได้
list_file = []
with open(f'Sorting-Algorithm/Convert/{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        

list_reversed = Selection_revers(list_file)

output_file = f'Sorting-Algorithm/Sort_file/output/Selection/{file}_Selection.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")

