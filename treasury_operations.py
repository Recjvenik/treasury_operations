from datetime import datetime, timedelta

# Define the daily limits for each bank account
master_banks_limits = {
    'Bank 1': {'weekday_limit': 200000, 'weekend_limit': 100000},
    'Bank 2': {'weekday_limit': 50000, 'weekend_limit': 50000, 'instant_limit': 20000},
    'Bank 3': {'weekday_limit': 200000},
    'Bank 4': {'weekday_limit': 100000, 'weekend_limit': 50000}
}

# Define the invoices for each subsidiary company
invoices = {
    'Company 1': 2000000,
    'Company 2': 372000,
    'Company 3': 112000,
    'Company 4': 720000,
    'Company 5': 198000,
    'Company 6': 97000,
}


# Calculate total amount to be transferred
def total_amounts(invoices):
    """
    Calculate the total amount of invoices.
    
    Args:
    invoices (dict): A dictionary where keys are company names and values are invoice amounts.
    
    Returns:
    int: Total amount of all invoices.
    """
    return sum(invoices.values())

# Define the start date
start_date = datetime(2024, 1, 1)



# Function to calculate the transfer schedule
def calculate_transfer_schedule():
    """
    Calculate the transfer schedule for distributing funds to subsidiary companies.
    
    Returns:
    list: A list of tuples containing transfer information (date, bank, transfer type, amount).
    """

    total_amount = total_amounts(invoices)
    
    current_date = start_date
    amount_transfer_schedule = []

    # Sort banks based on their limits, prioritizing banks with higher limits
    weekday_sorted_banks_limit = dict(sorted(master_banks_limits.items(), key=lambda item: item[1].get('weekday_limit', 0), reverse=True))
    weekend_sorted_banks_limit = dict(sorted(master_banks_limits.items(), key=lambda item: item[1].get('weekend_limit', 0), reverse=True))
    
    while total_amount > 0:
        # Determine if it's a weekday or weekend
        is_weekday = True if current_date.weekday() < 5 else False
        banks_limits = weekday_sorted_banks_limit if is_weekday else weekend_sorted_banks_limit

        for bank, limits in banks_limits.items():

            transfer_amount = 0
            
            if is_weekday:
                # Check if the bank has instant transfer limit
                if limits.get('instant_limit'):
                    # Instant transfer amount
                    transfer_amount = min(total_amount, limits['instant_limit'])
                    if transfer_amount > 0:
                        # Append transfer details to the schedule for Instant transfer
                        amount_transfer_schedule.append((current_date, current_date, bank, "Instant", transfer_amount))
                        # Calculating remaining amount needs to be transfered
                        total_amount -= transfer_amount
                
                # Regular transfer amount
                transfer_amount =  min(total_amount, limits['weekday_limit']) 
            else:
                # Weekend transfer amount
                if limits.get('weekend_limit'):
                    transfer_amount = min(total_amount, limits['weekend_limit'])            

    
            if transfer_amount > 0:
                # Append transfer details to the schedule
                completion_date = current_date + timedelta(hours=24)
                amount_transfer_schedule.append((current_date, completion_date, bank, "Scheduled", transfer_amount))
                
                # Calculating remaining amount needs to be transfered
                total_amount -= transfer_amount

        current_date += timedelta(days=1)
    return amount_transfer_schedule


# Print the transfer schedule
def print_schedule(schedule):
    """
    Print the transfer schedule with details.
    
    Args:
    schedule (list): A list of tuples containing transfer information (date, bank, transfer type, amount).
    """
    if schedule:
        print("Transfer Schedule:")
        for start_date, completion_date, bank, transfer_type, amount in schedule:
            print(f"Date: {start_date.strftime('%Y-%m-%d')} | Completion Date: {completion_date.strftime('%Y-%m-%d')} | Bank: {bank} | Transfer Type: {transfer_type} | Amount: {amount}€")
        print(f"Expected completion date for all transfers: {completion_date.strftime('%Y-%m-%d')}")


# Main function
def main():
    """
    Main function to execute the transfer schedule calculation and printing.
    """
    schedule = calculate_transfer_schedule()
    print_schedule(schedule)

if __name__ == "__main__":
    main()



