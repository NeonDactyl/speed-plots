import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

times = []
speed_data = {'up': [], 'down': [], 'ping': []}

with open('../data/speed-log.csv') as input_file:
    csv_reader = csv.DictReader(input_file)

    for row in csv_reader:
        times.append(datetime.fromisoformat(row['Timestamp'][:-1]))
        speed_data['up'].append(float(row['Upload'])/1000000)
        speed_data['down'].append(float(row['Download'])/1000000)
        speed_data['ping'].append(float(row['Ping']))

plt.subplot(3, 1, 1)
plt.grid(which='major', axis='y')
plt.plot(times, speed_data['down'])
plt.title('Internet Speeds')
plt.ylabel('Download')

plt.subplot(3, 1, 2)
plt.grid(which='major', axis='y')
plt.plot(times, speed_data['up'], color='red', linewidth=1.0, linestyle='--')
plt.ylabel('Upload')

plt.subplot(3, 1, 3)
plt.grid(which='major', axis='y')
plt.plot(times, speed_data['ping'])
plt.ylabel('Ping')

plt.show()
