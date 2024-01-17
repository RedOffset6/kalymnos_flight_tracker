import pickle as pkl

#opens the file and reads in the pricing info
with open(f'data/prices.pkl', 'rb') as f:
    price_list = pkl.load(f)

print(price_list)