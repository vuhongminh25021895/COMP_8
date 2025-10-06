#1
n = input("Nhap so nguyen n")
print(n[-1:])
#2
a = int(input("Nhap so nguyen"))
b = int(input("Nhap so nguyen"))
b = a^b
a = b^a
b = a^b
print(a)
print(b)
#3
n = int(input())
if n & (n-1) == 0:
    print(f"{n} la luy thua cua 2")
#4
import math 
m, n = map(float, input=().split())
c = m/n
print(math.floor(c))
#5
import math
m, n = map(float, input=().split())
c = m/n
print(math.celi(c))
#6
x = int(input("Nhap 1 so nguyen duong"))
if x%2 == 0:
    print("Even")
else:
    print("Odd")
#7
m , n = map(int, input("Nhap  2 so"))
if m<0 and n<0:
    print("Yes")
else:
    print("No")
#8
a = input()
b = input()
if len(a)>len(b):
    print("True")
else:
    print("False")
#9
a,b,c = map(int, input("Nhap 3 so nguyen duong").split)
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Yes")
else:
    print("No")
#10
a, b, c, d= map(int, input().split())
if a>b and a>c and a>d:
    max=a
elif b>c and b>d:
    max=b
elif c>d: 
    max=c
else:
    max=d 
print(max)
#11
a,b,c = map(int, input("Nhap 3 so nguyen duong").split())
if (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
       print("Tam giac deu")
    elif a==b or b==c or a==c:
       print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai la tam giac")
#12
n = int(input("Nhap so nguyen duong"))
if (n%4==0 and n%100!= 0) or n%400 == 0:
    print("Yes")
else:
    print("No")
#13
n = float(input("Nhap so dien tieu thu"))
if n <= 50:
    print(n*1500)
elif 51 <= n <= 100:
    print(n*2000)
elif n >= 100:
    print(n*3000)
#14
a,b = map(float, input("Nhap 2 so thuc").split())
if a !=0:
    x = b/a
    print("Phuong trinh co nghiem duy nhat",x)
elif a==0:
    print("Phuong trinh vo nghiem")
elif a==b==0:
    print("Phuong trinh co vo so nghiem")
#15
n = float(input("Nhap diem trung binh"))
if 0 <=n<=10:
    if n >= 8.0:
        print("Gioi")
    elif n >= 6.5:
        print("Kha")
    elif n >= 5.0:
        print("Trung binh")
    else:
        print("Yeu")
#16
a = float(input("Nhap so thuc"))
if a == int(a):
    print(a, a, a)
else:
    print(round(a//1+1), round(a//1),int(a))



