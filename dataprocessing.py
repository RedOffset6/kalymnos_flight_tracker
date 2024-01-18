import pickle as pkl
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np

#opens the file and reads in the pricing info
with open(f'data/prices.pkl', 'rb') as f:
    price_list = pkl.load(f)

dates = [entry['date_checked'] for entry in price_list]
outbound_prices = [entry['outbound_price'] for entry in price_list]
inbound_prices = [entry['inbound_price'] for entry in price_list]

# Define a function to format tick labels with £ sign
def pound_sign_formatter(x, _):
    return f'£{x:.2f}'

#adding the price I paid to the list 
dates.append(datetime(2024, 1, 11, 22, 00, 00))
outbound_prices.append(32.23)
inbound_prices.append(53.02)


# fig, ax = plt.subplots()

# ax.scatter(dates, outbound_prices)
# ax.scatter(dates, inbound_prices)

# Plotting
plt.figure(figsize=(10, 6))

total_price = np.array(outbound_prices) + np.array(inbound_prices)

plt.plot(dates, outbound_prices, label='Outbound Price', marker='o')
plt.plot(dates, inbound_prices, label='Inbound Price', marker='o')
plt.plot(dates, total_price, label='Total Price', marker='o')

# Formatting the x-axis to show dates elegantly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=10))

# Formatting y-axis to include £ sign
plt.gca().yaxis.set_major_formatter(FuncFormatter(pound_sign_formatter))

plt.xlabel('Date Checked')
plt.ylabel('Price')
plt.title('Flight Prices Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

#plt.show()

plt.savefig("plots/price_plot.png")

# print(price_list)

print(f"The ticket price has been recorded {len(price_list)} times")