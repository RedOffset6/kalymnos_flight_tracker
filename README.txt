This code records the price of the flights between stansted and kos airport on the 4th and 11th of April for the UBMC 2024 trip

Every time the flight_tracker.py script is executed it records the price of the flights in the price_list.pkl file in data

The flight tracker is executed hourly by the cron deamon (accessed by crontab -e) in the ubuntu linux partition of my pc

The crontab line is below:

0 * * * * /home/benmorgan/miniconda3/envs/ryanair_env/bin/python3 /mnt/c/Users/benlu/Documents/Bristol/forth_year/UBMC/ryanair_tracker/flight_tracker.py

this executes when minutes = zero for every hour of every day (shown by *)

The script then points to my python environment and the python file