import csv
import os

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

# variables = financial data
total_months = 0
net_total = 0
net_change_list = []
previous_net = 0

# variables = greatest increase/decrease in profits
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
 
# open and read csv
try:
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)
        header = next(reader)

        # get first row
        first_row = next(reader)
        total_months += 1
        net_total += int(first_row[1])
        previous_net = int(first_row[1])

        # loop through all rows
        for row in reader:
            total_months += 1
            net_total += int(row[1])

            # net change calculation
            net_change = int(row[1]) - previous_net
            previous_net = int(row[1])
            net_change_list.append(net_change)

            # greatest increase calculation
            if net_change > greatest_increase[1]:
                greatest_increase = [row[0], net_change]

            # greatest decrease calculation
            if net_change < greatest_decrease[1]:
                greatest_decrease = [row[0], net_change]

    # average change calculation
    average_change = sum(net_change_list) / len(net_change_list)

    # summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    print(output)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

except FileNotFoundError as e:
    print(f"Error: {e}. Please check the file path and try again.")