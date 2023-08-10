from pathlib import Path
import csv
# Path the overhead.csv file to the current working directory.
file_path = Path.cwd()/"overheads.csv"
def overhead_function(file_path):
    """
    -This function finds the highest overhead category.
    -One required parameter is file_path, which shows where the overheads CSV file is. 
    File_path should be a string or Path object indicating the system location of the CSV file.
    """
    # Read the contents of the CSV file.
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)[1:]  # Skip the header

    # Set the variables to track maximum overhead and category.
    max_overhead = 0
    max_category = ''
    # Iterate over the data, starting from the second row
    for row in data[1:]:
        # Unpack row category and value.
        category, value = row
        # Convert value to float
        value = float(value)
        #Update max_overhead and max_category if the value is greater than maximum overhead.
        if value > max_overhead:
            max_overhead = value
            max_category = category
    # Return the result
    return f'[HIGHEST OVERHEAD] {max_category.upper()}: {max_overhead}%\n'