from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"

def profitloss_function(file_path):
    """
    -The function calculates the net profit difference if the current day's net profit is lower than the previous day's. 
    If net profit always increases, the function will identify the day and amount of the highest increase.
    -There is only one required parameter, file_path, which provides the location of the CSV file containing the profit and loss data. 
    File_path should be a string or Path object indicating the system location of the CSV file.
    """
    # Read the contents of the CSV file.
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)[1:]  # Skip the header row
        # Set the variables to track previous profit, maximum difference, and day.
        prev_profit = 0
        max_diff = 0
        max_diff_day = 0
        result = ''
        # Iterate over the data, starting from the first row
        for row in data:
            # Unpack the day and profit from the row
            day = int(row[0])
            profit = int(row[4])
            
            diff = profit - prev_profit
            ## If the difference is negative (profit decreased), update the result string.
            if diff < 0:
                result += f'[PROFIT DEICIT] DAY: {day}, AMOUNT: USD{abs(diff)}\n'
                always_increasing = False
            #Update max_diff and max_day if the difference is positive (profit increased) and greater than the maximum difference.
            elif diff > max_diff:
                max_diff = diff
                max_diff_day = day
                
            prev_profit = profit
        ## If profit was always increasing, add a message to the result string indicating this, as well as a message indicating the day and amount of the highest increase.
        if always_increasing:
            result += '[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n'
            result += f'[HIGHEST NET PROFIT SURPLUS] DAY: {max_diff_day}, AMOUNT: USD{max_diff}\n'
        return result