# A ryanair flight tracker for teh UBMC Kalymnos trip 

#run crontab -e to open the crontab

from datetime import datetime, timedelta, date
from ryanair import Ryanair
from ryanair.types import Flight
import pickle as pkl
import os

#This line creates a blank price list

# price_list = []
# with open(f'data/prices.pkl', 'wb') as f:
#    pkl.dump(price_list, f)



# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))



#opens the file and reads in the pricing info
with open(os.path.join(script_dir, 'data/prices.pkl'), 'rb') as f:
    price_list = pkl.load(f)



api = Ryanair(currency="GBP")  # Euro currency, so could also be GBP etc. also

# flights = api.get_cheapest_flights("DUB", tomorrow, tomorrow + timedelta(days=1))

#input the outbound date [yyyy, mm, dd, hh, mm, ss]
outbound_date = datetime(2024, 4, 4, 00, 00, 00)
return_date = datetime(2024, 4, 11, 00, 00, 00)

outbound_flights = api.get_cheapest_flights("STN", outbound_date, outbound_date + timedelta(days=1), destination_airport = "KGS")
inbound_flights = api.get_cheapest_flights("KGS", return_date, return_date + timedelta(days=1), destination_airport = "STN")

print(outbound_date)

#Gets the cheapest outbound flight
flight: Flight = outbound_flights[0]
print(flight)  # Flight(departureTime=datetime.datetime(2023, 3, 12, 17, 0), flightNumber='FR9717', price=31.99, currency='EUR' origin='DUB', originFull='Dublin, Ireland', destination='GOA', destinationFull='Genoa, Italy')
outbound_price = flight.price

# Gets the cheapest inbound flight
flight: Flight = inbound_flights[0]
print(flight)  # Flight(departureTime=datetime.datetime(2023, 3, 12, 17, 0), flightNumber='FR9717', price=31.99, currency='EUR' origin='DUB', originFull='Dublin, Ireland', destination='GOA', destinationFull='Genoa, Italy')

inbound_price = flight.price

# print(f"the return flight costs {flight.price}")

# print(f"Total price = {outbound_price+inbound_price}")

#Creates a dictionary entry 
price_dict = {}

#creating a dictionary to append to the price list
price_dict["date_checked"]  = datetime.today()
price_dict["outbound_price"] = outbound_price
price_dict["inbound_price"] = inbound_price

#appends this to the price list
price_list.append(price_dict)

#saves the updated price list
with open(os.path.join(script_dir, 'data/prices.pkl'), 'wb') as f:
    pkl.dump(price_list, f)
