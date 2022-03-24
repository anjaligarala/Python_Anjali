try:
    a = int(input())
    b = int(input())

    if b == 0:
        raise ArithmeticError(f"This is raise error")
    else:
        print("a/b", a / b)
        print("This is testing")

except Exception as xyz:
    print("value of b cant be 0" + str(xyz))
