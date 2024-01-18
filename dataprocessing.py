import pickle as pkl

#opens the file and reads in the pricing info
with open(f'data/prices.pkl', 'rb') as f:
    price_list = pkl.load(f)

dates = [entry['date_checked'] for entry in price_list]
outbound_prices = [entry['outbound_price'] for entry in price_list]
inbound_prices = [entry['inbound_price'] for entry in price_list]

print(price_list)

print(f"The ticket price has been recorded {len(price_list)} times")