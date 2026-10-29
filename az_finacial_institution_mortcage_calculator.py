#1. Minimum Down Payment Component




#2. Mortgage Default Insurance Component
mortgage_term = 0
while mortgage_term not in (1, 2, 3, 5, 10):
    mortgage_term = int(input('Enter mortgage term (1, 2, 3, 5, 10): '))

    if mortgage_term not in (1, 2, 3, 5, 10):
        print('Please enter a valid choice')

mortgage_amortization_period = 0
while mortgage_amortization_period not in (5, 10, 15, 20, 25):
    mortgage_amortization_period = int(input('Enter mortgage amortization period (5, 10, 15, 20, 25): '))

    if mortgage_amortization_period not in (5, 10, 15, 20, 25):
        print('Please enter a valid choice')

match mortgage_term:
    case 1:
        annual_mortgage_interest_rate = 5.9
    case 2:
        annual_mortgage_interest_rate = 5.8
    case 3:
        annual_mortgage_interest_rate = 5.5
    case 5:
        annual_mortgage_interest_rate = 5.3
    case 10:
        annual_mortgage_interest_rate = 6

print(f'Interest rate for the term will be {annual_mortgage_interest_rate:0.2f}%')

effective_monthly_rate = ((1 + (annual_mortgage_interest_rate / 100) / 2) ** 2) ** (1 / 12) - 1

number_of_monthly_payments = mortgage_amortization_period * 12

math_part_1 = principal_amount * (effective_monthly_rate * (1 + effective_monthly_rate) ** number_of_monthly_payments)
monthly_payment_amount = math_part_1 / ((1 + effective_monthly_rate) ** number_of_monthly_payments - 1)
print(f'Monthly payment amount is: ${monthly_payment_amount:0.2f}')
