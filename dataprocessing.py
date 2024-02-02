import pickle as pkl
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns

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

# Create a DataFrame for Seaborn
import pandas as pd
df = pd.DataFrame({'Date': dates, 'outbound_price': outbound_prices, 'inbound_price': inbound_prices})
df["total_price"] = df["outbound_price"] + df["inbound_price"]

# Set the seaborn style
sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})

# Plotting with Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='outbound_price', data=df, label='Outbound Price', marker='o')
sns.lineplot(x='Date', y='inbound_price', data=df, label='Inbound Price', marker='o')
sns.lineplot(x='Date', y='total_price', data=df, label='Total Price', marker='o')

# Formatting the x-axis to show dates elegantly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=10))

# Formatting y-axis to include £ sign
plt.gca().yaxis.set_major_formatter(FuncFormatter(pound_sign_formatter))

plt.xlabel('Date Checked',  fontsize=18)
plt.ylabel('Price (£)',  fontsize=18)
plt.title('Flight Prices Over Time',  fontsize=26)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Beautify the legend
plt.legend(frameon=False)

# Optionally, add shaded region for weekends
for i in range(len(dates) - 1):
    if dates[i].weekday() == 4:  # Friday
        plt.axvspan(dates[i], dates[i + 1], facecolor='lightgray', alpha=0.2)

plt.tight_layout()


plt.savefig("plots/price_plot.png")

# print(price_list)

print(f"The ticket price has been recorded {len(price_list)} times")

daily_change = (df["total_price"].max() - df["total_price"].min()) / (19-12)

print(f"The average daily price increase was £{daily_change}")

