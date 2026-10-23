# lab4_1.py - Student Management System (List Operations)
# หมายเหตุ: โค้ดนี้ตัดส่วน "Challenge" (ระบบเมนูแบบ while loop) ออก
#          เพื่อให้นักศึกษานำ concept ด้านล่างไปต่อยอดคิดเองเป็นแบบฝึกหัด

print("--- Lab 4.1: Student Management System ---")

# 1) เริ่มต้นด้วย list ว่างสำหรับเก็บชื่อนักศึกษา
student_names = []

# 2) เพิ่มนักศึกษา: รับชื่อจากผู้ใช้ 3 คน แล้ว append() เข้า list
print("\n[1] Add Students")
for i in range(3): #กำหนดตัวแปรใน loop 👈ต้องทำ
    student_name = input(f"Enter student name #{i + 1}: ") #กำหนดตัวแปร 👈ต้องทำ
    student_names.append(student_name)

print(f"Current list: {student_names}")

# 3) ค้นหานักศึกษา: ใช้ 'in' เพื่อเช็คว่ามีชื่อนี้อยู่ใน list หรือไม่
#    ถ้าพบ ให้แสดง index ด้วย index()
print("\n[2] Find a Student")
search_name = input("Enter a name to search for: ")

if search_name in student_names: #เขียนเงื่อนไข ถ้าหากมีชื่อในลิส: 👈ต้องทำ
    position = student_names.index(search_name)
    print(f"Found '{search_name}' at index {position}")
else:
    print(f"'{search_name}' not found in the list")

# 4) ลบนักศึกษา: เช็คก่อนว่ามีอยู่จริงหรือไม่ (กัน error) แล้วค่อย remove()
print("\n[3] Remove a Student")
remove_name = input("Enter a name to remove: ")

if remove_name in student_names:
    student_names #เติมฟังก์ชัน remove(remove_name) 👈ต้องทำ
    print(f"'{remove_name}' has been removed")
else:
    print(f"'{remove_name}' not found, nothing removed")

print(f"Updated list: {student_names}")

# 5) เรียงลำดับรายชื่อตามตัวอักษรด้วย sort()
print("\n[4] Sort Students")
student_names #เติมฟังก์ชันsort()
print(f"Sorted list: {student_names}")

# 6) นับจำนวนนักศึกษาทั้งหมดด้วย len()
print("\n[5] Count Students")
print(f"Total students: {'''ใช้คำสั่งlen() หาจำนวนนักศึกษาในลิส student_names'''}") #ใช้คำสั่งlen() หาจำนวนนักศึกษาในลิส student_names👈ต้องทำ

# --------------------------------------------------------------------
# ให้นักศึกษาลองต่อยอดเอง (Challenge):
# ลองเขียนระบบเมนูด้วย while loop (จาก Week 3) ที่ให้ผู้ใช้เลือกได้ว่า
# จะเพิ่ม / ลบ / ค้นหา / เรียงลำดับ / หรือออกจากโปรแกรม
# โดยนำโค้ดแต่ละส่วนด้านบนไปจัดเป็นฟังก์ชันหรือเงื่อนไขในเมนู
# --------------------------------------------------------------------\

# Challenge
student_names = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Find Student")
    print("4. Sort Students")
    print("5. Show Students")
    print("6. Exit")

    choice = input("Choose menu: ")

    if choice == "1":
        name = input("Enter student name: ")
        student_names.append(name)
        print("Student added.")

    elif choice == "2":
        name = input("Enter name to remove: ")
        if name in student_names:
            student_names.remove(name)
            print("Student removed.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in student_names:
            print(f"Found at index {student_names.index(name)}")
        else:
            print("Student not found.")

    elif choice == "4":
        student_names.sort()
        print("Students sorted.")

    elif choice == "5":
        print(student_names)
        print(f"Total students: {len(student_names)}")

    elif choice == "6":
        print("Exit Program")
        break

    else:
        print("Invalid menu.")