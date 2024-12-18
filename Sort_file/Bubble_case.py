import timeit

start_time = timeit.default_timer()
def Bubble_revers(list):
    n = len(list)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            
            if list[j] < list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
                flag = 1
        if flag == 0:
            break
    return list

file = 'tambol' #เปลี่ยนชื่อไฟล์ได้
list_file = []
with open(f'Sorting-Algorithm/Convert/{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        
list_reversed = Bubble_revers(list_file)

output_file = f'Sorting-Algorithm/Sort_file/output/Bubble/{file}_Bubble.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
Timespent = timeit.default_timer() - start_time
print(f"{Timespent} seconds")
