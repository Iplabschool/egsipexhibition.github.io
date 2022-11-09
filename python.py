import cgitb
cgitb.enable()
#areaofcircle
r=float(input("Enter radius of the circle:"))
pi=3.14
a=pi*r*r
print("Area of the circle is",a,"m")

#area of square
s=float(input("enter side of square"))
area of square=s*s
print("area of square is: ",area of square)

#area of rectangle
l=float(input("enter length of rectangle"))
b=float(input("enter breadth of rectangle"))
area of rectangle=l*b
print("area of ractangle is: ",area of rectangle)

#volume of cuboid
l=float(input("enter length of cuboid"))
b=float(input("enter breadth ofcuboid"))
h=float(input("enter height of cuboid"))
volume of cuboid=l*b*h
print("volume of cuboid",volume of cuboid)

#gain list from user
n=int(input("enter number of elements"))
l=list()
fot i in range (0,n):
  z=int(input("enter element :"))
  l.append(z)
print("list is: ",l)

#profit %
cgos=float(input("enter cost of goods sold"))
revenue=float(input("enter the revenue amount"))
profit=revenue-cgos
profit%=(profit/cgos)*100
print("cost of goods : ",cgos)
print("revenue generated : ",revenue)
print("profit % : ",profit%)

#miles convert into km
miles=int(input("enter miles : "))
km=miles/0.621371
print("miles : ",miles)
print("kilometers : ",km)

#even or odd
n=int(input("enter the number : "))
if n%2==0:
  print(n," is a even number")
else:
  print(n," is a odd number")
  
#ascending order of no.
a=int(input("enter first number : "))
b=int(input("enter second number : "))
c=int(input("enter third number : "))
if a<b and a<c:
  if b<c:
    min, mid, max = a,b,c
  else :
    min, mid, max = a,c,b
elif b<a and b<c:
  if a<c:
    min, mid, max = b,a,c
  else :
    min, mid, max = b,c,a
else :
  if a<b:
    min, mid, max = c,a,b
  else :
    min, mid, max = c,b,a
print("numbers in ascending order are : ",min, mid, max)

#Volume of sphere
r=float(input("Enter the radius of sphere:"))
v=4*3.14*r*r*r/3
print("Volume of sphere is",v)

