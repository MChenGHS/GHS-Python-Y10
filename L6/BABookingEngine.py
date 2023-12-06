def airport_in_list(airport):
    # Check if an airport is in any of the lists

    # Remove below when you start writing the function
    return True

def calculate_base_fare(departure, arrival):
    # Calculate the base fare per person
    # Domestic UK flights: £80
    # Between Europe & UK: £100
    # Between North America & UK: £400
    # Between East Asia & UK: £500
    # Between South Asia & UK: £450
    # If they make a flght between two non-UK airports, the fare is calculated as follows:
    # (depareture to UK fare + UK to arrival fare) * 0.75

    # Remove below when you start writing the function
    return 999

def calculate_return_fare(ticketType, inputFare):
    # Calculate the fare per person based on journey type
    # Singe fare is the same as input fare
    # Return fare is caculated as follows:
    # If input fare is below £450:
    #   1.7 * input fare + £50
    # Otherwise:
    #   1.5 * input fare

    # Remove below when you start writing the function
    return inputFare

def calculate_class_fare(ticketClass, inputFare):
    # Calculate the fare per person based on journey class
    # Economy fare is the same as input fare
    # Premium Economy is caculated as follows:
    # 1.6 * input fare
    # Business is caculated as follows:
    # 2.5 * input fare + £100
    # First is caculated as follows:
    # 3.4 * input fare + £200

    # Remove below when you start writing the function
    return inputFare

# No changes to the rest of the program necessary
import time

# A list of all available airports
allAirportsUK = ["LHR", "LGW", "MAN", "BHX", "EDI", "GLA"]
allAirportsEuro = ["CDG", "FRA", "AMS", "FCO"]
allAirportsNA = ["JFK", "LGA", "LAX", "YYZ"]
allAirportsEAsia = ["PVG", "HKG", "HND", "ICN"]
allAirportsSAsia = ["DEL", "MAA", "SIN", "KUL"]

print("Welcome to British Airways Booking Engine")
time.sleep(1) # Wait 1 second, pretending the computer is doing a serious search

# Get departure airport
depAirport = input("Where are you flying from?")
while airport_in_list(depAirport) == False:
    print("We currently don't operate flights from ", depAirport, ". Please try again.")
    depAirport = input("Where are you flying from?")

time.sleep(1) # Wait 1 second, pretending the computer is doing a serious search

# Get arrival airport
arrAirport = input("Where are you flying to?")
while airport_in_list(depAirport) == False:
    print("We currently don't operate flights to ", arrAirport, ". Please try again.")
    arrAirport = input("Where are you flying to?")

print("We are finding the best fare for you.")
time.sleep(2) # Wait 2 seconds, pretending the computer is doing a serious search

# Calculate the fare per person based on journey type
ticketType = input("Single or Return? ")
baseFare = calculate_base_fare(depAirport, arrAirport)
currentFare = baseFare
if ticketType.lower() == "return":
    currentFare = calculate_return_fare(ticketType, currentFare)

# Calculate the fare per person based on journey class
ticketClass= input("Which class? ")
currentFare = calculate_class_fare(ticketClass, currentFare)

# Calculate total price
numPersons = int(input("How many persons are flying? "))
finalFare = currentFare * numPersons

# Print itinerary
print("Please see your itinerary below:")
print("Departure from: ", depAirport)
print("Arriving at: ", arrAirport)
if numPersons == 1:
    print(ticketType, " journey for 1 person")
else:
    print(ticketType, " journey for ", numPersons, " persons")
print("Total cost: ", finalFare)