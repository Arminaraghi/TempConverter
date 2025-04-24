print('Welcome to Temp Convert 2..!')

from_unit = input('Enter the input unit (C/F/K): ')
to_unit = input('Enter the output unit (C/F/K): ')
temp = float(input('Enter the temperature: '))

def temp_convert(from_unit, to_unit, temp):
    if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
        return False

    if from_unit == 'C':
        if to_unit == 'F':
            temp = (temp * 1.8) + 32
        elif to_unit == 'K':
            temp = temp + 273.15

    elif from_unit == 'F':
        if to_unit == 'C':
            temp = (temp - 32) / 1.8
        elif to_unit == 'K':
            temp = (temp + 459.67) / 1.8

    elif from_unit == 'K':
        if to_unit == 'C':
            temp = temp - 273.15
        elif to_unit == 'F':
            temp = (temp * 1.8) - 459.67

    return temp, to_unit, from_unit

result = temp_convert(from_unit, to_unit, temp)

if result:
    temp, to_unit, from_unit = result
    print(f"Converted: {temp:.2f}°{to_unit} (from {from_unit})")
else:
    print("Invalid input units.")
