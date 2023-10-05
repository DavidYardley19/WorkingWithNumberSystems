if __name__ == "__main__":

    print("Welcome to the Decimal to Binary conversion centre!")
    decimal_input = input("Please enter a decimal number: ")
    decimal_input_to_int = int(decimal_input)

    StopLoop = False
    newQuotient = decimal_input_to_int
    remainder = None
    binary_list = []

    while newQuotient != 0:
        remainder = newQuotient % 2
        newQuotient //= 2
        binary_list.insert(0, remainder)

    print(f"So {decimal_input} in Decimal is equal to the binary value: ", end="")
    for x in binary_list:
        print(x, end="")
