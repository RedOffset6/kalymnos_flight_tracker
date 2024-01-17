import pickle as pkl

with open(f'data/cron_test.pkl', 'wb') as f:
   pkl.dump("THE cron script was succesfully activated", f)


