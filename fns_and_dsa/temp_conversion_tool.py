FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit-32)
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius) + 32
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
        "Is this temprature in celsius or fahrenhiet? (C/F): ").strip().upper()
    if choose not in ("C", "F"):
        print("Invalid Unit ")
        continue
    else:
        break
if choose == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif choose == "F":
    print(f"{temperature:.1f}°F is {convert_to_celsius(temperature)}°C")
