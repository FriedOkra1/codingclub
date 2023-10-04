print("How many stones?")
stones = float(input())
print("How many pounds?")
pounds = float(input())
total = 12.0*stones+pounds
kg = round(total/2.2, 2)
print("you are",kg,"kg")

if kg > 80:
  print("bit fat innit")
elif kg < 80:
  print("bit slim innit")
else:
  print("liar")
