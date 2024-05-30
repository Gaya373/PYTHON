# in-build function
my_string=input("Enter the string :")
print(my_string.lower())

# for loop
my_string=input("Enter the string :")
lower=''
for i in my_string:
    if 'A'<= i <='Z':
        lower=lower+chr(ord(i)+32)
    else:
        lower=lower+i
print(lower)


#using function

def lower_case(my_string):
    lower=''
    for i in my_string:
        if 'A'<= i <='Z':
            lower=lower+chr(ord(i)+32)
        else:
            lower=lower+i
    print(lower)
lower_case(input("Enter the string :"))

