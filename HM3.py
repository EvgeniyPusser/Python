# # input("сумму всех покупок в магазине", "сколько даешь денег", "даем сдачу")
# # input -> enter total amount
# # input -> enter cash money(NIS)
# # output Your change(NIS)
# #your change (NIS)
#
# # input first number
# # input second number
# # calculate division first to second
# #
# #
# # input "enter hours worked"
# # input "wage(NIS)"
# # input "enter bonus in percent"
# # input "tax in per cent"
#
# #Первое задание
#
# total_amount = input("Enter prices for all you've bought(NIS)")
# cash_money= input("Enter money you give(NIS)")
# change = int(cash_money)-int(total_amount)
# print("Your change is ",change, "NIS")
#
# #Второе задание
#
# first_num = input("Enter the first number")
# second_num = input("Enter the second number")
# quotient = (float(first_num) / float(second_num))
# print(quotient)
#
# #Третье задание

hours = input("Enter all hours you worked ")
wage = input("Enter your wage(NIS) ")
bonus = input("Enter your bonus in percent ")
tax = input("Enter your tax in percent ")

dollar_rate = float(input("Enter the rate of US dollar "))
euro_rate = float(input("Enter the rate of euro "))

salary_gross = float(hours) * float(wage)
print(f"Your salary without bonus before-tax is {salary_gross:.2f} (NIS)")
income = salary_gross + salary_gross * int(bonus) / 100
print(f"Your salary with bonus is {income:.2f} (NIS)")
salary_after_tax = income - income * int(tax) / 100
salary_after_tax_in_dollars = salary_after_tax / dollar_rate
salary_after_tax_in_euro = salary_after_tax / euro_rate

print(f"Your take-home pay is {salary_after_tax_in_dollars:.2f} ($)")
print(f"Your take-home pay is {salary_after_tax_in_euro:.2f} (euro)")
print(f"Your take-home pay is {salary_after_tax:.2f} (NIS)")







# Изюм

salary_gross_shekel = salary_gross // 1
salary_gross_agorot = (salary_gross * 100) % 100
print(f"\nYour gross salary is {salary_gross_shekel:.0f} (NIS) and {salary_gross_agorot:.01f} agorot")

income_shekel = (salary_gross + salary_gross * int(bonus) / 100) // 1
income_agorot = ((salary_gross + salary_gross * int(bonus) / 100) * 100) % 100
print(f"Your salary with bonus is {income_shekel:.0f} (NIS) and {income_agorot:.0f} agorot")

salary_after_tax_shekel = (salary_after_tax) // 1
salary_after_tax_agorot = ((salary_after_tax / 100) * 100) % 100
print(f"Your take-home pay is {salary_after_tax_shekel:.0f} (NIS) and {salary_after_tax_agorot:.0f} agorot")

# print("number equals", round(8.889090909, 3), sep="_    _")
