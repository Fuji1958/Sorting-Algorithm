import sqlite3

# ชื่อไฟล์ฐานข้อมูล
database_file = 'mm.py'

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect(database_file)

try:
    # สร้าง Cursor สำหรับรันคำสั่ง SQL
    cursor = conn.cursor()
    
    # Query ดึงข้อมูลจากฟิลด์ ID และ Name
    query = "mcode,`mname`"  # เปลี่ยน table_name เป็นชื่อจริงของตารางคุณ
    cursor.execute(query)
    
    # ดึงผลลัพธ์
    rows = cursor.fetchall()
    
    # แสดงผลข้อมูล
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}")
finally:
    # ปิดการเชื่อมต่อฐานข้อมูล
    conn.close()
