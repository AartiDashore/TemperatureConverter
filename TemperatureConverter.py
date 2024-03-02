def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
        print("Temperature in Kelvin:", celsius_to_kelvin(celsius))
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
        print("Temperature in Kelvin:", fahrenheit_to_kelvin(fahrenheit))
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print("Temperature in Celsius:", kelvin_to_celsius(kelvin))
        print("Temperature in Fahrenheit:", kelvin_to_fahrenheit(kelvin))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
