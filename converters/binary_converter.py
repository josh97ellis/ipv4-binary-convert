def binary_converter_int(x: int):
    """
    Converts an integer value to its binary equivalent
    """
    if type(x) is int:
        pass
    elif type(x) is float:
        x = int(x)
    else:
        raise TypeError(
            f"Input is of type {type(x)}, however input must be int or float")

    # Divide x by 2 and use the integer quotient obtained as
    # the dividend for the next step.
    # Repeat the process until the quotient becomes 0.
    binary_remainders = []
    while x > 0:
        dividend = x % 2
        x = x//2
        binary_remainders.append(str(dividend))

    # Reverse the remainder to obtain the binary equivalent
    binary_remainders.reverse()
    
    return ''.join(binary_remainders)


def main():
    value = int(input("Enter an Integer Value: "))
    print(binary_converter_int(value))


if __name__ == '__main__':
    main()
