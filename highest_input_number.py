#define function to compare
def compare(int1, int2, int3, int4, int5):
    if int1 >= int2:
        highest = int1
    else:
        highest = int2

    if int3 > highest:
        highest = int3

    if int4 > highest:
        highest = int4

    if int5 > highest:
        highest = int5
    return highest
#user input 5 numberds
int1 = int(input("Input your FIRST number: "))
int2 = int(input("Input your SECOND number: "))
int3 = int(input("Input your THIRD number: "))
int4 = int(input("Input your FOURTH number: "))
int5 = int(input("Input your FIFTH number: "))
#use define function
highest_number = compare (int1, int2, int3, int4, int5)
#output largest number
print(f"Your highest value input: {highest_number}")