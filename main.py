from pathlib import Path
from coh import coh_function
from overheads import overhead_function
from profit_loss import profitloss_function

# Set file paths to COH.csv, overheads.csv, and profit_loss.csv in the current working directory.
coh_file_path = Path.cwd()/"csv_reports"/"coh.csv"
overheads_file_path = Path.cwd()/"csv_reports"/"overheads.csv"
profitloss_file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"


def main():
    """
    -This function writes the computed amount from the overhead_function, coh_function, and profitloss_function to a text file and names it summary_report.txt.
    """
    # Open the summary_report.txt file for writing
    with open('summary_report.txt', 'w') as file:
        # File the overhead_function, coh_function, and profitloss_function results.
        file.write(overhead_function(overheads_file_path))
        file.write(coh_function(coh_file_path))
        file.write(profitloss_function(profitloss_file_path))
# Call the main function
main()
