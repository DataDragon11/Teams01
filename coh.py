from pathlib import Path
import csv
# Path the coh.csv file to the current working directory.
file_path = Path.cwd()/"csv_reports"/"coh.csv"
def coh_function(file_path):
    """
    -The function determines the difference in cash on hand if it is lower than the previous day 
    and the highest increment day and quantity if it is always increasing.
    -One parameter is the file_path to the cash-on-hand CSV file. File path should be a 
    string or Path object representing the CSV file's system location.
    """
    # Read the contents of the CSV file.
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)[1:]  # Skip the header

     # Convert the data to a list of tuples, with dates as the first element and cash on hand (converted to float) as the second element.
    cash_on_hand = []
    for row in data:
        day = int(row[0])
        cash = float(row[1])
        cash_on_hand.append((day,cash))
    # Set the variables to track the maximum difference and day.
    max_diff = 0 
    max_day = 0 
    result = ''
    #Iterate over the cash on hand data from day two.
    for current in range(1,len(cash_on_hand)):
        diff = cash_on_hand[current][1] - cash_on_hand[current-1][1]
        # If the difference is negative (cash on hand decreased), update result string and set always_increasing to False.
        if diff < 0:
            result += f'[CASH DEFICIT] DAY: {cash_on_hand[current][0]}: {abs(diff)}\n'
            always_increasing = False
        ## Update max_diff and max_day if the difference is positive (cash on hand increased) and greater than the maximum difference.
        elif diff > max_diff:
            max_diff = diff 
            max_day = cash_on_hand[current][0]
    # # If cash on hand was always increasing, add a message to the result string indicating this, as well as a message indicating the day and amount of the highest increase.
    if always_increasing:
        result += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        result += f'[HIGHEST CASH SURPLUS]: Day {max_day}, AMOUNT: {max_diff}\n'
    return result
