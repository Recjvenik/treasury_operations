import datetime

# Define the invoice amounts for each company
invoices = {
    "Company 1": 214000,
    "Company 2": 372000,
    "Company 3": 112000,
    "Company 4": 72000,
    "Company 5": 198000,
    "Company 6": 97000
}

# Sort companies based on invoice amounts
sorted_companies = dict(sorted(invoices.items(), key=lambda x: x[1], reverse=True))
invoices_amount = list(sorted_companies.values())
invoices_companies = list(sorted_companies.keys())

# Define the daily limits for each bank account
bank_limits = {
    "Bank 1": {"weekday": 200000, "weekend": 100000},
    "Bank 2": {"weekday": 50000, "weekend": 50000, "instant": 20000},
    "Bank 3": {"weekday": 200000},
    "Bank 4": {"weekday": 100000, "weekend": 50000}
}

# Function to calculate the transfer schedule
def calculate_transfer_schedule():
    # Set the starting date for transfers
    current_date = datetime.date(2024, 1, 1)
    amount_transfer_schedule = []

    # total amount that need to be transfered
    total_amount = sum(invoices_amount)

    # Sort banks based on their weekday and weekend limits
    weekday_sorted_banks_limit = dict(sorted(bank_limits.items(), key=lambda item: item[1].get('weekday', 0), reverse=True))
    weekend_sorted_banks_limit = dict(sorted(bank_limits.items(), key=lambda item: item[1].get('weekend', 0), reverse=True))
    
    # get first invoice
    index = 0
    invoice_amount  = invoices_amount[index]

    # Loop until all invoices are paid
    while total_amount  > 0:
        # Choose banks based on the day of the week
        sorted_banks_limits = weekday_sorted_banks_limit if current_date.weekday() < 5 else weekend_sorted_banks_limit
        
        for bank, limits in sorted_banks_limits.items():    
            if total_amount == 0:
                break

            daily_limit = None
            # Determine the daily limit based on the day of the week and bank's limits
            if current_date.weekday() < 5:  # Weekday
                daily_limit = limits["weekday"]
                if limits.get("instant"):
                    daily_limit = daily_limit + limits["instant"]
            else: 
                if limits.get("weekend"):
                    daily_limit = limits["weekend"]

            if daily_limit:
                # If the invoice amount is within the daily limit, transfer the entire amount
                if invoice_amount <= daily_limit:
                    transfer_amount = invoice_amount
                    total_amount = total_amount - transfer_amount
                    amount_transfer_schedule.append((current_date, bank, transfer_amount, invoices_companies[index]))
                    left_limit = daily_limit - invoice_amount

                    # Transfer remaining amounts within the daily limit
                    while left_limit > 0 :
                        if index == len(invoices_amount) - 1:
                            break
                        index = index + 1 
                        invoice_amount = invoices_amount[index]
                        transfer_amount = min(invoice_amount, left_limit)
                        amount_transfer_schedule.append((current_date, bank, transfer_amount, invoices_companies[index]))
                        total_amount = total_amount - transfer_amount
                        invoice_amount -= transfer_amount
                        left_limit -= transfer_amount
                else:
                    # If the invoice amount exceeds the daily limit, transfer up to the limit
                    transfer_amount = daily_limit
                    amount_transfer_schedule.append((current_date, bank, transfer_amount, invoices_companies[index]))
                    total_amount = total_amount - transfer_amount
                    invoice_amount -= transfer_amount
            
            # If the current invoice amount is fully transferred, move to the next invoice
            if invoice_amount <= 0 and index < len(invoices_amount) - 1:
                index = index + 1
                invoice_amount = invoices_amount[index]

        # Move to the next day
        current_date += datetime.timedelta(days=1)
        
    return amount_transfer_schedule


def print_schedule(schedule):
    """
    Print the transfer schedule with details.
    
    Args:
    schedule (list): A list of tuples containing transfer information (date, bank, comapny, amount).
    """
    if schedule:
        print("Transfer Schedule:")
        for start_date, bank, amount, company_name in schedule:
            print(f"Date: {start_date.strftime('%Y-%m-%d')} | Bank: {bank}  | Amount: {amount}€ | {company_name}")
        print(f"Expected completion date for all transfers: {start_date.strftime('%Y-%m-%d')}")


# Calculate and print the transfer schedule
schedule = calculate_transfer_schedule()
print_schedule(schedule)
