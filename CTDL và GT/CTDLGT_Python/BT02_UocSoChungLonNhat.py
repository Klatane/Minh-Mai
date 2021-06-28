def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

a = int(input("Số dương thứ nhất: "))
b = int(input("Số dương thứ hai: "))

print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))


