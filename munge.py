# Place code below to do the munging part of this assignment.
def clean_and_convert_to_csv(input_filepath, output_filepath):
    def convert_to_fahrenheit(celsius):
        return celsius * 9.0 / 5.0

    with open(input_filepath, 'r') as file:
        lines = file.readlines()

    # Remove all lines with notes
    start_index = end_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith('Year'):
            start_index = i
            break
    for i, line in enumerate(reversed(lines)):
        if line.strip() and not line.strip().startswith('Year'):
            end_index = len(lines) - i
            break

    # Process only the relevant lines
    data_lines = lines[start_index:end_index]

    # Keep only the first column headings
    column_headings = data_lines[0].split()[:-1]  # Exclude the last 'yearly' column from the headings
    data_lines = [line for line in data_lines if line[0].isdigit()]

    # Clean and convert data
    cleaned_data = []
    for line in data_lines:
        parts = line.split()[:-1]  # Exclude the last 'year' column
        year = parts[0]
        temperatures = parts[1:]
        cleaned_temperatures = []
        for temp in temperatures:
            if temp == '':
                cleaned_temperatures.append('')
            else:
                try:
                    # Change the data 
                    celsius_value = float(temp) * 0.01  # Convert to degrees Celsius
                    temp_fahrenheit = convert_to_fahrenheit(celsius_value)
                    cleaned_temperatures.append(f'{temp_fahrenheit:.1f}')
                except ValueError:
                    # Handle other cases
                    cleaned_temperatures.append('')
        cleaned_data.append([year] + cleaned_temperatures)

    with open(output_filepath, 'w') as file:
        # Convert column headings to CSV format
        file.write(','.join(column_headings) + '\n')
        for row in cleaned_data:
            file.write(','.join(row) + '\n')


input_filepath = 'data/GLB.Ts+dSST.txt'
output_filepath = 'data/clean_data.csv'

clean_and_convert_to_csv(input_filepath, output_filepath)