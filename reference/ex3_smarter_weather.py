
# Remember, we get a string from raw_input, but we need an int to compare it
weather = int(raw_input("What temperature is it now? (as a number, please): "))

# if the weather is greater than or equal to 25 degrees
if weather >= 25:
    print("Go to the beach!")
# the weather is less than 25 degrees AND greater than 15 degrees
elif weather < 25 and weather > 15:
    # Still warm enough for ice cream!
    print("Still warm enough for ice cream!")
else:
    # Wear a sweater and dream of beaches.
    print("Wear a sweater and dream of beaches.")
