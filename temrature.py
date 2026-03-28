import os
import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


print("🌡️ Temperature Converter")

while True:
    print("\nChoose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if not choice.isdigit() or int(choice) not in range(1, 8):
        print("❌ Invalid choice! Please choose a number between 1 and 7.")
        continue  

    choice = int(choice)

    if choice == 7:
        print("✅ Exiting... Thank you for using Temperature Converter!")
        sys.exit()

    while True:
        try:
            temp = float(input("Enter temperature value: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

    if choice == 1:
        print(f"{temp} °C = {celsius_to_fahrenheit(temp):.2f} °F")
    elif choice == 2:
        print(f"{temp} °F = {fahrenheit_to_celsius(temp):.2f} °C")
    elif choice == 3:
        print(f"{temp} °C = {celsius_to_kelvin(temp):.2f} K")
    elif choice == 4:
        print(f"{temp} K = {kelvin_to_celsius(temp):.2f} °C")
    elif choice == 5:
        print(f"{temp} °F = {fahrenheit_to_kelvin(temp):.2f} K")
    elif choice == 6:
        print(f"{temp} K = {kelvin_to_fahrenheit(temp):.2f} °F")

    while True:
        again = input("\nDo you want to convert again? (y/n): ").lower()
        if again == 'y':
            clear_screen()
            break
        elif again == 'n':
            print("✅ Exiting... Thank you for using Temperature Converter!")
            sys.exit()
        else:
            print("❌ Invalid input! Please enter 'y' for yes or 'n' for no.")