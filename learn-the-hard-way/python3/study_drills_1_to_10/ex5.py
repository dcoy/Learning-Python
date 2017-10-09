name = 'David Coy'
age = 30
height = 72 # inches
weight = 260 #lbs
eyes = 'grey'
teeth = 'White'
hair = 'Brown'

cent = 2.54
kg = 0.453592

print("Let's talk about {0}.".format(name))
print("He's {0} inches tall.".format(height))
print("He's {0} centimeters tall.".format(height * cent))
print("He's {0} pounds heavy.".format(weight))
print("He's {0} kg heavy.".format(kg * weight))
print("Actually, that's not too heavy.")
print("He's got {0} eyes and {1} hair.".format(eyes, hair))
print("His teeth are usually {0} depending on the coffee.".format(teeth))

total = age + height + weight
print("If I add {0}, {1}, and {2}, I get {3}.".format(
                                               age,
                                               height,
                                               weight,
                                               total))