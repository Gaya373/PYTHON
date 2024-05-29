# my_string=input("Enter the value :")
# total=0
# for i in my_string:
    # print(f"{i}:{ord(i)}")
    # total=total+ord(i)
#print(total)

def characters(my_string):
    total=0
    for i in my_string:
        print(f"{i}:{ord(i)}")
        total=total+ord(i)
    print(total)
characters(input("Enter the characters :"))
