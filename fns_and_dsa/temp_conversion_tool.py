FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


while True:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        break  # valid input, exit loop
    except ValueError:
        print("Invalid Temperature. Please enter a numeric value.")
        continue

while True:
    choose = input(
        "Is this temprature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if choose not in ("C", "F"):
        print("Invalid Unit ")
        continue
    else:
        break
if choose == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif choose == "F":
    print(f"{temperature:.1f}°F is {convert_to_celsius(temperature)}°C")
