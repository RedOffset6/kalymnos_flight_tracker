import pickle as pkl

#opens the file and reads in the pricing info
with open(f'data/cron_test.pkl', 'rb') as f:
    crontest = pkl.load(f)



print(crontest)