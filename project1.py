
#مدیریت لیست دانش اموزان

#1: اضافه کردن دانش اموز:دریافت نام و سن و افزودن به لیست
#2: حذف دانش اموز:..دریافت نام..اگه موجود بود..حذف.. اگه نبود خطا
#3: جستجوی دانش اموزان:دریافت نام..اگه موجود بود ..چاپ جزییات..اگه نبود پیام خطا
#4: چاپ کل دانش اموزان:نمایش همه ی دانش اموزان با جزییات
#5: منوی انتخابی کاربر:کاربر انتخاب کنه که چه عملی رو میخواد انجام بده و امکان خروج از برنامه رو داشته باشه

#اضافه کردن دانش اموز
students=[]
def add_student(name,age):
    students.append("name:",name,"age:",age)
    print(name,"دانش اموز اضافه شد")
   # add_student("bahare",22)  برای اجرای مسیله به مسیله و خط به خط  فانکشن رو صدا میزنیم تا اجرا بشه
  
   #حذف دانش اموز
def remove_student(name):
    for i in students:
        if i["name"]==name:
            students.remove(i)
            print(i,"دانش اموز حذف شد!")
        else:
            print(i,"دانش اموزی با این مشخصات یافت نشد")
           
           
            #جستجوی دانش اموز
def search_student(name):
    for i in students:
      if i["name"]==name:
        print("found:",i)
        return
    print(i,"پیدا نشد")

    #چاپ کل دانش اموزان
def print_student():
    if not students:
        print("دانش اموز پیدا نشد!")
    else:
        for i in  students:
            print(i)


            #منوی انتخابی کاربر 
while True:
     print("\n=====منوی دانش اموزان=====")
     print("1 : اضافه کردن دانش اموز")
     print("2 : حذف کردن دانش اموز")
     print("3 : سرچ کردن دانش اموز")
     print("4 : چاپ کل دانش اموزان")
     print("5: خارج شدن")
     choice=input("عدد مورد نظر را وارد کنید:")
     if choice==1:
            name=input("نام دانش اموز را وارد کنید:")
            age=input("سن دانش اموز را وارد کنید:")
            add_student(name,age)
     elif choice==2:
            name=input("نام دانش اموز را وارد کنید")
            remove_student(name)
     elif choice==3:
            name=input("نام دانش اموز را وارد کنید")
            search_student(name)
     elif choice==4:
            print_student()
     elif choice==5:
            print("خداحافظ")
            break
     else:
            print("عدد  مورد نظر پیدا نشد")

                    





