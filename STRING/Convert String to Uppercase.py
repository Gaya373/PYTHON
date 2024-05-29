#using inbuild function
my_string=input("Enter the string :")
print(my_string.upper())

#using for loop
my_string=input("Enter the string :")
upper=' '
for i in my_string:
    if 'a'<= i <='z':
        upper+=chr(ord(i)-32)
    else:
        upper=upper+i
print(upper)

#using function
def upper_case(my_string):
    upper=''
    for i in my_string:
        if 'a'<=i<='z':
            upper=upper+chr(ord(i)-32)
        else:
            upper=upper+i
    print(upper)
upper_case(my_string=input("Enter the string :"))
