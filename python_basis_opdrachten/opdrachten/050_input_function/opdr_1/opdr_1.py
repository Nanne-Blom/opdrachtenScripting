# Import math module voor sqrt functie
import math

# Vraag de gebruiker om de lengtes van de eerste twee zijden
a = float(input("Geef de lengte van de eerste zijde: "))
b = float(input("Geef de lengte van de tweede zijde: "))

# Bereken de lengte van de schuine zijde met de stelling van Pythagoras
c = math.sqrt(a**2 + b**2)

# Print de lengte van de schuine zijde
print("De lengte van de schuine zijde is:", c)
