#1. Minimum Down Payment Component




#2. Mortgage Default Insurance Component
if input_down_payment_percent < 10:
    insurance_premium = 5
elif input_down_payment_percent < 15:
    insurance_premium = 4
elif input_down_payment_percent < 20:
    insurance_premium = 3
else:
    insurance_premium = 0

"Calculates insurance cost and the end cost(principle amount;total mortgage)"
insurance_cost = (purchase_price - down_payment) * (insurance_premium / 100)
principle_amount = (purchase_price - down_payment) + insurance_cost
print(
    f"Mortgage insurance price is {insurance_cost}\n"
    f"Total mortgage amount is {principle_amount}"
)



#3. Mortgage Payment Component
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
