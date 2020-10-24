# Pragati Dode
# find armstron numbers between 10 and user enterd number.
# added condition to check if entered number is valid interger or not
# this program take o(n) time, for loop will run for n times, all other statement would be constants

def get_user_input():
    return input("Please enter an integer from 10 through 1000000000:- ")

def calculate_armstrong_number(uppernumber):
    lower = 10
    total_armstrong = 0
    for num in range(lower, uppernumber + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            print(num)
            total_armstrong += 1
    print("\nThe total number of Armstrong numbers found was ", total_armstrong)

print("Welcome to the Armstrong number calculator.")
while True:
    try:
        upper=int(get_user_input()) # Lthis will fail if input entered is not number
        if upper < 10 or upper > 1000000000: #check for condition for range
            print("Enter a 10 for correct input")
        else:
            break
    except ValueError:
        print("Enter a valid integer type number")

print("The Armstrong numbers from 10 through ", upper ,"are:\n")
calculate_armstrong_number(upper)



