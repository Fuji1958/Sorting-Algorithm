import timeit

start_time = timeit.default_timer()

def QuickSort_reverse(a_list, start, end):
    if start >= end:  # Base case: If the range is invalid or a single element
        return

    pIndex = QuickSort_partition(a_list, start, end)

    # Recursive calls only proceed on valid ranges
    if pIndex - 1 > start:
        QuickSort_reverse(a_list, start, pIndex - 1)
    if pIndex + 1 < end:
        QuickSort_reverse(a_list, pIndex + 1, end)

def QuickSort_partition(a_list, start, end):
    pivot = a_list[end]
    pIndex = start

    for i in range(start, end):
        if a_list[i] >= pivot:  # For reverse order, use `>=`
            a_list[i], a_list[pIndex] = a_list[pIndex], a_list[i]
            pIndex += 1

    a_list[pIndex], a_list[end] = a_list[end], a_list[pIndex]
    return pIndex


file = 'mm'
list_file = []
with open(f'Sorting-Algorithm/Convert/{file}.txt', 'r', encoding='utf-8') as files:
    list_file = [line.strip() for line in files]

list_reversed = QuickSort_reverse(list_file, 0, len(list_file) - 1)

output_file = f'Sorting-Algorithm/Sort_file/output/Quick/{file}_Quick.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
Timespent = timeit.default_timer() - start_time
print(f"{Timespent} seconds")
