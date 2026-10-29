def SI(p, t, r):
    return (p * t * r) / 100

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
s = input("Senior citizen? (yes/no): ")

if s == "yes":
    r = 12
else:
    r = 10

print("Simple Interest =", SI(p, t, r))

