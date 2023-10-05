if __name__ == "__main__":

    print("Welcome to the bin to dec converter")
    binaryValue = input("Please enter a binary value: ")

    binaryLength = len(binaryValue)
    totalDecimal = 0

    for i in range(binaryLength):

        totalDecimal += (int(binaryValue[i]) * (2**(binaryLength - 1 - i)))

    print(f"{binaryValue} in Binary is equal to {totalDecimal} in Decimal")
