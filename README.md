## treasury_operations
This Python script is designed to calculate and print a transfer schedule for invoices across multiple bank accounts, taking into account daily limits for each bank account. The script is structured into several functions, each with a specific role, and uses Python's datetime module to handle dates.

## Overview
   - Imports and Data Structures: The script starts by importing necessary modules and defining data structures for bank limits and invoices.
   - Total Amount Calculation: A function `total_amounts` is defined to calculate the total amount to be transferred based on the invoices.
   - Transfer Schedule Calculation: The core logic is encapsulated in the `calculate_transfer_schedule` function, For each day, it iterates through each banks, determining the appropriate bank account to transfer funds to based on the limits defined for each bank.
   - Printing the Schedule: The `print_schedule` function is used to print the calculated transfer schedule in a readable format.
   - Main Execution: The main function orchestrates the execution of the script, calling the necessary functions to calculate and print the transfer schedule.

## Detailed Explanation
### Data Structures
  - Bank Limits: A dictionary `master_banks_limits` is defined to store the daily limits for each bank account. Each bank can have different limits for weekdays, weekends, and instant transfers.
  - Invoices: A dictionary `invoices` is defined to store the invoice amounts for each subsidiary company.

### Total Amount Calculation
  - The `total_amounts` function iterates over the invoices dictionary and sums up all the invoice amounts to calculate the total amount to be transferred.

### Transfer Schedule Calculation
  - The `calculate_transfer_schedule` function is the heart of the script. It first calculates the total amount to be transferred using the `total_amounts` function.
  - It then initializes a list `amount_transfer_schedule` to store the transfer schedule.
  - The function sorts the bank limits based on the instant and weekend limits in descending order to prioritize banks with higher limits.
  - For each day, it iterates through the sorted bank limits, calculating the transfer amount based on the day type and the bank's limits.
  - It appends the transfer details (date, bank, transfer type, and amount) to the `amount_transfer_schedule` list.
  - The process continues until the total amount to be transferred is zero.

## Printing the Schedule
The `print_schedule` function iterates through the `amount_transfer_schedule` list and prints each transfer detail in a formatted manner.

## Design Rationale
The script is designed to efficiently distribute invoice payments across multiple bank accounts, ensuring that each bank's daily limits are respected. By sorting the banks based on their limits, the script prioritizes banks with higher limits, ensuring that the total amount is distributed as early as possible. This approach minimizes the risk of exceeding a bank's daily limit while also ensuring that the total amount is distributed across all banks.

## Execution Instructions
To execute this script, simply run `python treasury_operations.py`
