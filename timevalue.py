"""
    Collection of functions to calculate time value of money
"""

def calc_present_val(periods, rate, future_val):
    """
        Given number of periods, interest rate and the future value,
        return the present value.
    """
    return future_val / ((1 + rate) ** periods)

def calc_future_val(periods, rate, present_val):
    """
        Given number of periods, interest rate and the present value,
        return the future value.
    """
    return present_val * ((1 + rate) ** periods)

def NPV(rate, cashflows):
    """
        Given an interest rate and a list of cashflow, calculate the net present value.
    """
    if type(cashflows) is not list:
        raise ValueError(list)
    result = 0
    for period, cashflow in enumerate(cashflows):
        result += calc_present_val(period, rate, cashflow)
    return result
