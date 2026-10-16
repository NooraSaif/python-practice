"""
challenge-1

Write a Python program that simulates a high-precision currency exchange system.

The program needs to:

Take three inputs from the user sequentially:

The first input represents an amount in USD (as a string that might contain extra whitespace or improper formatting).

The second input represents an exchange rate to EUR (a decimal number).

The third input represents a fixed transaction fee (a decimal number).

Clean and convert the USD amount and exchange rate into float types. If the user accidentally inputs a string with commas instead of periods for decimals (e.g., 1234,56), your program must handle or normalize it before conversion.

Calculate the converted amount in EUR (USD * exchange_rate).

Subtract the transaction fee from the converted total.

Print the final balance rounded precisely to 2 decimal places, prefixed with EUR:  (e.g., EUR: 452.10).

"""
amout_in_usd = float(input("Enter the amount in USD: ").replace(',', '.'))
exchange_rate_to_erd = float(input("Enter the exchange rate to EUR: ").replace(',', '.'))
transaction_fee = float(input("Enter the transaction fee: ").replace(',', '.'))

convert_to_eur = amout_in_usd * exchange_rate_to_erd
final_balance = convert_to_eur - transaction_fee

print(f"EUR: {final_balance:.2f}")


# Example Test Case
# Input 1:  1500,50  (with extra spaces and comma decimal)
# Input 2: 0.92
# Input 3: 5.50 
# Output: EUR: 1374.96