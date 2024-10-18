# hours_per_month = input("Enter your month hours  ")
# wage = input("Enter your wage(NIS)  ")
# salary = float(hours_per_month)*float(wage)
# print("Your salary is", salary, "NIS per month")
# print(f"salary (NIS) :{salary:.2f}")

amount = input("Enter sum of your money  ")
change_rate_dollars = input("Enter change $ rate ")
change_rate_euro = input("Enter change euro rate ")
dollars = float(amount)/float(change_rate_dollars)
euros = float(amount)/float(change_rate_euro)

# print(f"in dollars : {dollars:.2f}")
# print(f"in euros : {euro:.2f}")
print(dollars)
print(euros)

print(f"dollars: {dollars: .2f}")
print(f"euros: {euros: .2f}")



dollars_int = int(dollars // 1)
euros_int = int(euros // 1)

dollars_cents = int((dollars * 100) % 100)
euros_cents = int((euros * 100) % 100)

print(dollars_int, "$", dollars_cents, "cents")
print(euros_int, "euros", euros_cents, "cents")




