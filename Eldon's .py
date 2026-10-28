"""Monthly Mortgage Calculator
    AZ Financial Institution mothly mortgage calculator and schedule software containing...
Eldon Chin
2026.10.26
"""

"""PART 1 SECTION 1"""
client_name = input("Enter client name: ")
address = input("Enter address of property: ")
purchase_price = int(input("Enter purchase price: "))

"""Checks values for which minimum downpayment amount the client qualifies for"""
if purchase_price <= 400000:
    minimum_down_payment = 5

elif purchase_price <= 900000:
    minimum_down_payment_amount = (400000 * 0.05) + ((purchase_price - 400000) * 0.10)
    minimum_down_payment = (minimum_down_payment_amount / purchase_price) * 100

else:
    minimum_down_payment = 20

"""Checks if inputted downpayment amount is suffice"""
while True:
    input_down_payment_percent = float(
        input(f"Enter down payment percentage (minimum {minimum_down_payment:.3f}: ")
    )

    if (
        input_down_payment_percent < minimum_down_payment
        or input_down_payment_percent > 100
    ):
        print("Please enter a value between the minimum and 100")
    else:
        down_payment = float((input_down_payment_percent / 100) * purchase_price)
        print(f"Down payment amount is ${down_payment:.0f}")
        break


"""PART 1-SECTION 2"""
"Table for calculating which insurance bracket client falls into"
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


"""PART 1-SECTION 3"""
"mortgage term rate table"
mortgage_term_rate = {1: 0.059, 2: 0.058, 3: 0.055, 5: 0.053, 10: 0.06}
amortization_length = [5, 10, 15, 20, 25]

"nested loops for getting input values of mortgage length and amortization period"
while True:
    mortgage_term_length = int(input("Enter mortage term (1, 2, 3, 5, 10): "))
    if mortgage_term_length not in mortgage_term_rate:
        print("Please enter a valid choice")
        continue
    while True:
        amortization_period = int(
            input("Enter mortgage amortization period (5, 10, 15, 20, 25): ")
        )
        if amortization_period not in amortization_length:
            print("Please enter a valid choice")
            continue
        break
    break


"""Effective Monthly Rate(EMR) Calculator  AND Monthly Payment Calculator"""
annual_rate = float(mortgage_term_rate[mortgage_term_length])
# EMR=[((1+A/2)^2)^1/12]-1 where A=morgage_term_years value

EMR = ((1 + annual_rate / 2) ** 2) ** (1 / 12) - 1
monthly_payment = (
    principle_amount * (EMR * (1 + EMR) ** (amortization_period * 12))
) / (((1 + EMR) ** (amortization_period * 12)) - 1)


print(
    f"Interest rate for the term will be {mortgage_term_rate[mortgage_term_length]*100:.2f}%\n"
    f"Monthly payment amount is: ${monthly_payment:.2f}"
)

amortization_schedule = input(
    "Would you like to see the amortization schedule? (Y/N): "
).lower()
if amortization_schedule == "n":
    exit()


"""PART 2-SECTION 1"""
print(f"{'Monthly Amortization Schedule':^90}\n")
print(
    f"{'Month':<10}"
    f"{'Opening Bal':<20}"
    f"{'Payment':<15}"
    f"{'Principal':<15}"
    f"{'Interest':<15}"
    f"{'Closing Bal':<20}"
)
opening_balance = principle_amount

total_principal = 0
total_interest = 0

for month in range(1, amortization_period * 12 + 1):
    interest = opening_balance * EMR
    principal = monthly_payment - interest
    closing_balance = opening_balance - principal

    # Avoid tiny negative balance in final month
    if closing_balance < 0:
        principal += closing_balance
        closing_balance = 0

    print(
        f"{month:<10}"
        f"{opening_balance:<20.2f}"
        f"{monthly_payment:<15.2f}"
        f"{principal:<15.2f}"
        f"{interest:<15.2f}"
        f"{closing_balance:<20.2f}"
    )

    total_principal += principal
    total_interest += interest

    opening_balance = closing_balance

print("=" * 90)
print(f"{'Total':<45}" f"{total_principal:<15.2f}" f"{total_interest:<15.2f}")
