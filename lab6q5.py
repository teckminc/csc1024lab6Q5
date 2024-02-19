'''
Do not remove any text from these comments
5.	Redesign the Python program of Question 4 of LAB 4, Coding Exercise 4 
to use for-loop for all iterative processes, except the main loop that 
prompts the user to repeat the program can maintain using the while-loop.

Functions to use: print(), input(), int(),str.upper()
Operators: ==,<=, +, -, /, *, 
Structures: for, if-else, if – elif -else
'''
def main():

    play_gain = 'Y'
    while play_gain == 'Y':
        print("Temperature Conversion Programme.")
        print("[1] Convert Celsius to Fahreneit.")
        print("[2] Convert Fahrenheit to Celsius.")
        
        selection = int(input("Enter your selection, 1 or 2:"))
        if selection == 1:
            print("Celsius (c) to Fahrenheit (F) Conversion")
            print("Enter temperature in integer values only.")
            temp_min = int(input("Enter minimum temperature: "))
            temp_max = int(input("Enter maximum temperature: "))

            if temp_min <= temp_max:
                temp_c = temp_min
                while temp_c <= temp_max:
                    temp_f = (temp_c * 9 / 5) +32
                    print(f'{temp_c:>5.1f}C = {temp_f:>5.1f}F')
                    temp_c = temp_c + 1
                print("Conversion Done. ")
            else:
                print("Error: Invalid Input!")
        elif selection == 2:
            print("Fahrenheit (F) to Celsius (C) Conversion")
            print("Enter temperature in integer values only.")
            temp_min = int(input("Enter minimum temperture: "))
            temp_max = int(input("Enter maximum temperature: "))

            if temp_min <= temp_max:
                temp_f = temp_min
                while temp_f <= temp_max:
                    temp_c = (temp_f - 32) * 5/9
                    print(f'{temp_f:>5.1f}F = {temp_c:>5.1f}C')
                    temp_f = temp_f + 1
                print("Conversion Done.")
            else:
                print("Error: Invalid Input!")
        else: 
            print("Error: Invalid Selection!")
        play_gain = input("Do you want to run the program again? [Y/N]:").upper()
        print()

        while play_gain != 'N' and play_gain != "Y":
            play_gain = input("Do you want to run the program again? [Y/N]: ").upper()
    print("Program Terminated. ")
    return 0

