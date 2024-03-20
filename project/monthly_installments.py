def calculate_amortization(principal, annual_interest_rate, years):
    """
    Calculates the monthly amortization payment for a loan.

    Args:
        principal (float): The principal amount of the loan.
        annual_interest_rate (float): The annual interest rate for the loan.
        years (int): The number of years for the loan.

    Returns:
        float: The monthly amortization payment.

    Raises:
        ValueError: If the principal, interest rate, or years are negative.
        ValueError: If the years is 0.

    """
    if principal < 0 or annual_interest_rate < 0 or years < 0:
        raise ValueError("Principal, interest rate, and years must all be non-negative.")
    if years == 0:
        raise ValueError("Years must be greater than 0.")
    if annual_interest_rate == 0:
        return round(principal / (years * 12), 2)
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    return round(monthly_payment, 2)