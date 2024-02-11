# Place code below to do the analysis part of the assignment.
import csv

def calculate_decade_averages(input_filepath):
    # Initialize a dictionary
    decade_data = {}

    with open(input_filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip headline

        for row in reader:
            year = int(row[0])
            decade = (year // 10) * 10 
            anomalies = [float(val) for val in row[1:] if val]

            if anomalies:
                if decade not in decade_data:
                    decade_data[decade] = {'sum': 0, 'count': 0}
                decade_data[decade]['sum'] += sum(anomalies)
                decade_data[decade]['count'] += len(anomalies)

    for decade, values in sorted(decade_data.items()):
        average_anomaly = values['sum'] / values['count']
        print(f"{decade}s: {average_anomaly:.2f}°F")

input_filepath = 'data/clean_data.csv'

calculate_decade_averages(input_filepath)