import os
import timeit
start_time = timeit.default_timer()
import re

def read_sql_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    result = []
    for line in content:
        if line.strip():  # ตรวจสอบว่าบรรทัดไม่ว่าง
            parts = line.strip('(),').split(', ')  # แยกด้วย ", " 
            # เอาข้อมูลมาในรูปแบบที่เหมือนกัน
            if len(parts) >= 6:
                row = (parts[0], parts[1].strip("'"), parts[2], parts[3].strip("'"), parts[4], parts[5].strip("'"))
                result.append(row)
    return result

# รายชื่อไฟล์ที่ต้องการประมวลผล
file_path = "d:/work/mm.sql"


for file in file_path:
    data = read_sql_file(file)
    print(f"Processed data from {file}:")
    for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
        print(row[0], row[1])
    print("\n")
    
with open('work/Convert/mm.txt', 'w', encoding='utf-8') as write_province:
  for row in data:
    write_province.write(f"{row[0]} {row[1]}\n")

Timespent = timeit.default_timer() - start_time
print(f"{Timespent} seconds")