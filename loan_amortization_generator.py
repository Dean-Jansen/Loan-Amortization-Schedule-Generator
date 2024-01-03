import pandas as pd

def generate_amortization_schedule(loan_amount, annual_interest_rate, loan_term_years, repayment_frequency):
    """
    Generate a loan amortization schedule.

    Parameters:
    - loan_amount (float): The initial loan amount.
    - annual_interest_rate (float): Annual interest rate as a percentage.
    - loan_term_years (int): The loan term in years.
    - repayment_frequency (str): Repayment frequency, e.g., 'monthly', 'quarterly'.

    Returns:
    - pd.DataFrame: Loan amortization schedule.
    """

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 100 / 12

    # Calculate total number of payments
    total_payments = loan_term_years * 12 if repayment_frequency == 'monthly' else loan_term_years * 4

    # Calculate monthly payment using the formula for an amortizing loan
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)

    # Initialize lists to store schedule details
    periods = list(range(1, total_payments + 1))
    interest_payments = []
    principal_payments = []
    remaining_balances = []

    # Calculate amortization schedule
    remaining_balance = loan_amount
    for period in periods:
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment

        remaining_balance -= principal_payment

        interest_payments.append(interest_payment)
        principal_payments.append(principal_payment)
        remaining_balances.append(remaining_balance)

    # Create a DataFrame for the schedule
    schedule_data = {
        'Period': periods,
        'Interest Payment': interest_payments,
        'Principal Payment': principal_payments,
        'Remaining Balance': remaining_balances
    }

    amortization_schedule = pd.DataFrame(schedule_data)

    return amortization_schedule

# Example usage:
loan_amount = 100000  # Example loan amount
annual_interest_rate = 5.0  # Example annual interest rate
loan_term_years = 30  # Example loan term in years
repayment_frequency = 'monthly'  # Example repayment frequency ('monthly' or 'quarterly')

schedule = generate_amortization_schedule(loan_amount, annual_interest_rate, loan_term_years, repayment_frequency)

# Display the loan amortization schedule
print(schedule)
