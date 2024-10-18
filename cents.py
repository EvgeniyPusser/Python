q = 1234.987654
q_int = int(q // 1)
q_cents = q*100
q_only_cents = q_cents % 100
print(int(q_only_cents//1))
print(q_int)
