# Converteer Celsius naar Fahrenheit
def celsius_naar_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Converteer Fahrenheit naar Celsius
def fahrenheit_naar_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# Celsius
c = -12

# Fahrenheit
f = 102

# Converteer en print Celsius naar Fahrenheit
print(f"{c} graden Celsius is gelijk aan {celsius_naar_fahrenheit(c)} graden Fahrenheit")

# Converteer en print Fahrenheit naar Celsius
print(f"{f} graden Fahrenheit is gelijk aan {fahrenheit_naar_celsius(f)} graden Celsius")

# Extra testgevallen
c = 62.2
f = 96

print(f"{c} graden Celsius is gelijk aan {celsius_naar_fahrenheit(c)} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {fahrenheit_naar_celsius(f)} graden Celsius")
