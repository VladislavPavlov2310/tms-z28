def inch_to_centimeter(inch):
    return inch * 2.54


def centimeter_to_inch(centimeter):
    return centimeter * 0.3937


def mile_to_kilometer(mile):
    return mile * 1.6093


def kilometer_to_mile(kilometer):
    return kilometer * 0.6213


def pound_to_kilogram(pound):
    return pound * 0.4535


def kilogram_to_pound(kilogram):
    return kilogram * 2.2046


def ounce_to_gram(ounce):
    return ounce * 28.3502


def gram_to_ounce(gram):
    return gram * 0.0352


def halon_to_liter(halon):
    return halon * 3.7854


def liter_to_halon(liter):
    return liter * 0.2641


def pint_to_liter(pint):
    return pint * 0.4731


def liter_to_pint(liter):
    return liter * 2.1133


while True:
    choice = input('1) Inch to centimeter\n'
                   '2) Centimeter to inch\n'
                   '3) Mile to kilometer\n'
                   '4) Kilometer to mile\n'
                   '5) Pound to kilogram\n'
                   '6) Kilogram to pound\n'
                   '7) Ounce to gram\n'
                   '8) Gram to ounce\n'
                   '9) Halon to liter\n'
                   '10) Liter to halon\n'
                   '11) Pint to liter\n'
                   '12) Liter to pint\n')
    if choice == '1':
        number = float(input('Write number to convert: '))
        print(inch_to_centimeter(number))
    elif choice == '2':
        number = float(input('Write number to convert: '))
        print(centimeter_to_inch(number))
    elif choice == '3':
        number = float(input('Write number to convert: '))
        print(mile_to_kilometer(number))
    elif choice == '4':
        number = float(input('Write number to convert: '))
        print(kilometer_to_mile(number))
    elif choice == '5':
        number = float(input('Write number to convert: '))
        print(pound_to_kilogram(number))
    elif choice == '6':
        number = float(input('Write number to convert: '))
        print(kilogram_to_pound(number))
    elif choice == '7':
        number = float(input('Write number to convert: '))
        print(ounce_to_gram(number))
    elif choice == '8':
        number = float(input('Write number to convert: '))
        print(gram_to_ounce(number))
    elif choice == '9':
        number = float(input('Write number to convert: '))
        print(halon_to_liter(number))
    elif choice == '10':
        number = float(input('Write number to convert: '))
        print(liter_to_halon(number))
    elif choice == '11':
        number = float(input('Write number to convert: '))
        print(pint_to_liter(number))
    elif choice == '12':
        number = float(input('Write number to convert: '))
        print(liter_to_pint(number))
    if input('Do you want to continue? (Y/N)') == 'N':
        break
