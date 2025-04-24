Temp_unit = input('enter the Temp unit')
a = int(input('enter the Temperature'))
B = input('Converted to')
if Temp_unit == 'C' or 'c':
    if B == 'F' or 'f':
        Temp = (a*1.8) + 32
    elif B == 'K' or 'k':
        Temp = a + 273.15
    else:
        print('undefined..!')
if Temp_unit == 'F' or 'f':
    if B == 'C' or 'c':
        Temp = (a-32) / 1.8
    elif B == 'K' or 'k':
        Temp = (a + 459.67) / 1.8
    else:
        print('undefined..!')
if Temp_unit == 'K' or 'k':
    if B == 'F' or 'f':
        Temp = (a*1.8) - 459.67
    elif B == 'C' or 'c':
        Temp = a - 273.15
    else:
        print('undefined..!')
print(Temp,B)
