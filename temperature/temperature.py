from time import sleep

def temperatureConversion(fromUnit, toUnit, value):

    """temperatureConversion
    
    ### Parameters
    fromUnit (string): Unit to be converted from (c/f/k).
    toUnit (string): Unit to be converted to (c/f/k).
    value (int, float): Value to be converted.

    ### Returns
    int, float: Conversion result

    ### Example
    >temperatureConversion('c', 'f', 100)

    >212
    """

    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    
    if fromUnit == 'c':
        if toUnit == 'f':
            return value * 9 / 5 + 32
        elif toUnit == 'k':
            return value + 273.15
        else:
            return "Invalid"
    elif fromUnit == 'f':
        if toUnit == 'c':
            return (value - 32) * 5/9
        elif toUnit == 'k':
            return temperatureConversion('c', 'k', temperatureConversion('f', 'c', value))
        else:
            return "Invalid"
    elif fromUnit == 'k':
        if toUnit == 'c':
            return value - 273.15
        elif toUnit == 'f':
            return temperatureConversion('c', 'f', temperatureConversion('k', 'c', value))
        else:
            return "Invalid"
    else:
        return "Invalid"

# Uses example using loop
def start():
    while True:
        print("===Temperature Conversion===")
        print("(C)elsius")
        print("(F)ahrenheit")
        print("(K)elvin")
        print("Empty to quit")
        print()

        while True:
            fromUnit = input(("From: "))
            if fromUnit.lower() == 'c' or fromUnit.lower() == 'f' or fromUnit.lower() == 'k':
                break
            if fromUnit == '':
                return
            print("Enter a valid unit")

        while True:
            toUnit = input(("To: "))
            if toUnit.lower() == 'c' or toUnit.lower() == 'f' or toUnit.lower() == 'k':
                break;
            print("Enter a valid unit")

        while True:
            try:
                value = input("Value: ")
                value = int(value)
                break
            except ValueError:
                try:
                    value = float(value)
                    break
                except ValueError:
                    print("Please enter a valid number")
        result = temperatureConversion(fromUnit, toUnit, value)
        print("Result:", result)
        sleep(1)
        print()
        print()

if __name__ == '__main__':
    start()