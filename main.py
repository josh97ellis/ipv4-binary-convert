from converters import binary_converter_int
import numpy as np

def main():
    ip_address = input("Enter IP Address: ")

    # Splits the ip address by '.' into a list and loops through it
    # converting and combining each element into binary
    binary_ip = []
    for i in ip_address.split('.'):
        binary_coding = binary_converter_int(int(i))
        if len(binary_coding) != 8:
            binary_coding = ''.join(list(map(str, list(map(int, np.zeros(8 - len(binary_coding))))))) + binary_coding
        else:
            pass
        
        binary_ip.append(binary_coding)

    print('.'.join(binary_ip))


if __name__ == '__main__':
    main()
