print("Bill Split Calculator")
bill_amount = float(input("Enter bill amount: ").replace(',', '.'))
tip_percentage = float(input("Enter tip percentage: ").replace(',', '.'))
num_of_people = int(input("Enter number of people: "))
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = tip_amount + bill_amount
print(total_amount)
amount_per_person = total_amount / num_of_people
print(amount_per_person)