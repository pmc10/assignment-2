# Ask the user for the temperature in Fahrenheit
fahrenheit_input = input("Enter a temperature in Fahrenheit: ")

# Convert the text entered by the user to a decimal number
fahrenheit = float(fahrenheit_input)

# Apply the mathematical formula to convert to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the final result rounded to one decimal place using an f-string
print(f"{fahrenheit:.1f}°F is equal to {celsius:.1f}°C.")

