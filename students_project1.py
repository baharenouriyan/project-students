#ساخت یک برنامه کوچک برای مدیریت دانش اموزان که بتونه:
#1=اضافه کردن دانش اموز(نام,سن =ذخیره در لیست)
#2=حذف دانش اموز(اگه وجود داشت حذف بشه اگر نه پیام خطا بده)
#3=جستجوی دانش اموز=(اگه وجود داشت جزییات چاپ بشه )
#4چاپ کل دانش اموزان
#5=منوی انتخابی کاربر(انتخاب عملیات و امکان خروج)

students = []
def add_student():
 name = input("enter your number:")
 age  = int(input("enter your age:"))
 student = {"name":name, "age":age}
 students.append(student)
 print(f"{name} has been added")
def remove_student():
 name = input("Enter student name to remove:")
 for student in students:
    if  student ["name:"]==name:
        students.remove(student)
        print(f"{name} has been removed")
    return
print(f"student not found")
def search_student():
  name = input("enter student name to search:")
  for student in students:
        if student["name:"]==name:
           print(f"name:{student['name']},age:{student['age']}")
           return
        print(f"student {name} not found")
def print_student():
   if not students:
        print("no student found!")
   else:
        for student in students:
           print(f"name :{student['name']},age:{student['age']}")
def main():
   while True:
        print("-----menu-----")
        print("1 :add students")
        print("2 :remove students")
        print("3 :search students")
        print("4 :print students")
        print("5 :exit")
        choice=input("enter your choice:")
        if choice=="1":
           add_student()
        if choice=="2":
           remove_student()
        if choice=="3":
           search_student()
        if choice=="4":
           print_student()
        if choice=="5":
           print("exiting program")
           break
        else:
           print("invalid choice! pleas enter 1-5")

           main()
                
               


