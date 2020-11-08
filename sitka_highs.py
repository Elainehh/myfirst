import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
   
    for index, column_header in enumerate(header_row):
        print(index,column_header)

    dates, highs = [], []
    for row in reader:
        high = int(row[8])
        current_date = datetime.strptime(row[2],"%m/%d/%Y") 
        dates.append(current_date)
        highs.append(high)
    print(highs)
    plt.style.use('seaborn')
    fig,ax = plt.subplots()
    ax.plot(dates,highs,c='red')
    plt.title("Daily high temperatures-2018, fontsize =24")
    plt.xlabel('', fontsize =16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)",fontsize=16)
    plt.tick_params(axis ='both',which ='major',labelsize =16)
    plt.show()
    
    

    