def gram_to_kilogram(grams):
    kilograms = grams / 1000
    return kilograms

def kilogram_to_gram(kilograms):
    grams = kilograms * 1000
    return grams

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

# Example usage
grams = 1500
kilograms = gram_to_kilogram(grams)
print(f"{grams} grams is equal to {kilograms} kilograms.")

kilograms = 2.5
grams = kilogram_to_gram(kilograms)
print(f"{kilograms} kilograms is equal to {grams} grams.")

fahrenheit = 75
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

hours = 2
seconds = hours_to_seconds(hours)
print(f"{hours} hours is equal to {seconds} seconds.")

seconds = 7200
hours = seconds_to_hours(seconds)
print(f"{seconds} seconds is equal to {hours} hours.")
