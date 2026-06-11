deposited_sum = float(input())
maturity_in_months = int(input())
annual_interest_rate = float(input())

credited_sum = deposited_sum + maturity_in_months * ((deposited_sum * annual_interest_rate / 100) / 12)
print(credited_sum)
