def main():
    from contextlib import suppress
    from os import name, system

    def pres_check(prompt):
        a = ''
        while not a:
            with suppress(KeyboardInterrupt):
                a = input(prompt)
        a = a.replace(' ', '')
        return a

    def base_check(base):
        if base < 2 or base > 62:
            print('-----\nINVALID\nThis numeral base is not supported.\n-----')
            return False
        else:
            return True

    def base_note(base):
        # ₀₁₂₃₄₅₆₇₈₉
        note = ''
        for digit in str(base):
            match digit:
                case '0':
                    note += '₀'
                case '1':
                    note += '₁'
                case '2':
                    note += '₂'
                case '3':
                    note += '₃'
                case '4':
                    note += '₄'
                case '5':
                    note += '₅'
                case '6':
                    note += '₆'
                case '7':
                    note += '₇'
                case '8':
                    note += '₈'
                case '9':
                    note += '₉'
        return note

    def clear():
        system('cls' if name == 'nt' else 'clear')

    def base_name(base):
        # Tens
        if base >= 10:
            if base >= 20:
                if base >= 60:
                    name = 'SEXA'
                elif base >= 50:
                    name = 'QUINQUA'
                elif base >= 40:
                    name = 'QUADRA'
                elif base >= 30:
                    name = 'TRI'
                elif base >= 20:
                    name = 'VI'
                name += 'GES'
            else:
                name = 'DEC'
            name += 'IMAL'

            # Units
            unit = str(base)[1]
            if unit != '0':
                match unit:
                    case '1':
                        name = 'UN' + name
                    case '2':
                        name = 'DUO' + name
                    case '3':
                        name = 'TRI' + name
                    case '4':
                        name = 'TETRA' + name
                    case '5':
                        name = 'PENTA' + name
                    case '6':
                        name = 'HEXA' + name
                    case '7':
                        name = 'HEPTA' + name
                    case '8':
                        name = 'OCTO' + name
                    case '9':
                        name = 'ENNEA' + name

        # Singles
        else:
            match base:
                case 2:
                    name = 'BI'
                case 3:
                    name = 'TER'
                case 4:
                    name = 'QUATER'
                case 5:
                    name = 'QUI'
                case 6:
                    name = 'SE'
                case 7:
                    name = 'SEPTE'
                case 8:
                    name = 'OCTAL'
                case 9:
                    name = 'NO'

            if 2 <= base <= 7 or base == 9:
                name += 'NARY'

        return name

    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    print('''╔═════
║ NUMERAL BASE CONVERTER''')

    while True:

        # 1.1 Number to Convert
        print('═════')

        # Logic Validation
        while True:
            a = True
            # Character Validation
            while a:
                a = False
                # Number Validation
                while True:
                    num_input = pres_check('Number to convert: ')

                    # Decimal separator check
                    if num_input.count('.') > 1:
                        print('-----\nINVALID\nThis is an invalid number.\n-----')
                    else:
                        break

                # Minus
                if num_input[0] == '-':
                    minus = True
                    num_input = num_input[1:]
                else:
                    minus = False

                # Character check
                for char in num_input:
                    if char != '.' and char not in alphabet:
                        print(
                            '-----\nINVALID\nThis input contains invalid characters.\n-----'
                        )
                        a = True
                        break

            # Checking decimals
            dec_pres = '.' in num_input
            number = num_input.split('.')
            # and trailing zeros
            if dec_pres and number[1] == '0' * len(number[1]):
                number.pop(1)
                dec_pres = False

            # The numbers equal in every base
            if not dec_pres and (number[0] == '0' * len(number[0])
                                 or number[0] == '0' * (len(number[0]) - 1) + '1'):
                print(
                    '-----\nILLOGICAL\nThis number is the same in every base.\n-----'
                )
            else:
                break

        # 1.2 From Numeral Base
        print('\n═════')
        b = False
        # Logic Validation
        while not b:
            # Range Validation
            while True:
                # Presence & Type Validation
                while True:
                    from_base = pres_check('From base: ')
                    if not from_base.isnumeric():
                        print(
                            '-----\nINVALID\nPlease only enter numeric symbols.\n-----')
                    else:
                        break

                from_base = int(from_base)
                if base_check(from_base):
                    break

            # Base character set check
            if from_base != 62:
                for i, char in enumerate(num_input):
                    if char not in alphabet[:from_base] and char != '.':
                        print(
                            '-----\nINVALID\nThis number contains characters not of this base.\n-----'
                        )
                        break
                    elif i == len(num_input) - 1:
                        b = True
            else:
                b = True

        # 1.3 To Numeral Base
        to_bases = []
        print('\n═════')
        # Equality Validation
        c = True
        while c:
            # Range Validation
            while True:
                # Presence & Type Validation
                while True:
                    to_base = pres_check('To base (enter X to stop entering bases): ').upper()

                    if to_base == 'X':
                        if len(to_bases) == 0:
                            print('-----\nINVALID\nNo bases entered.\n-----')
                        else:
                            c = False
                            break

                    elif not to_base.isnumeric():
                        print(
                            '-----\nINVALID\nPlease only enter numeric symbols.\n-----')
                    else:
                        break

                if c:
                    to_base = int(to_base)
                    if base_check(to_base):
                        break
                else:
                    break

            if c:
                if to_base == from_base:
                    print(
                        '-----\nINVALID\nThis base is the same as the original base.\n-----'
                    )
                else:
                    to_bases.append(to_base)

        # 2 Conversion
        clear()

        # 2.1 Number to Denary
        if from_base != 10:
            total = 0
            number[0] = number[0][::-1]  # Reverses

            # Integers
            for i, char in enumerate(number[0]):
                total += from_base ** i * alphabet.index(char)
            # Decimals
            if dec_pres:
                for i, char in enumerate(number[1]):
                    total += from_base ** (-i - 1) * alphabet.index(char)

        else:
            total = float(num_input)

        # 2.2 Denary to Bases
        new_nums = []
        for to_base in to_bases:
            denary = total

            if to_base != 10:
                # 2.2.1 Getting number of places
                expo = 0

                if denary >= 1:
                    while not (denary >= to_base ** expo
                               and denary < to_base ** (expo + 1)):
                        expo += 1

                # 2.2.2 Composition
                new_num = ''

                # 2.2.2.1 Integers
                for e in range(expo, -1, -1):
                    power = to_base ** e
                    value = int(denary / power)
                    new_num += alphabet[value]
                    denary -= power * value

                # 2.2.2.2 Decimals
                if dec_pres:
                    new_num += '.'
                    expo_2 = 0

                    while denary > 0:
                        expo_2 -= 1
                        power = to_base ** expo_2
                        try:
                            value = int(denary / power)
                        except ZeroDivisionError:
                            break
                        new_num += alphabet[value]
                        denary -= power * value

                # 2.2.3 Binary Nibbles
                if to_base == 2:
                    num_list = new_num.split('.')

                    # 2.2.3.1 Padding
                    # 2.2.3.1.1 Integers
                    while len(num_list[0]) % 4:
                        num_list[0] = '0' + num_list[0]
                    # 2.2.3.1.2 Decimals
                    if dec_pres:
                        while len(num_list[1]) % 4:
                            num_list[1] += '0'

                    # 2.2.3.2 Spacing
                    ints = list(num_list[0])
                    for i in range(int(len(num_list[0]) / 4) - 1):
                        ints.insert((i + 1) * 5 - 1, ' ')

                    if dec_pres:
                        while len(num_list[1]) % 4:
                            num_list[1] += '0'

                        decs = list(num_list[1])
                        for i in range(int(len(num_list[1]) / 4) - 1):
                            decs.insert((i + 1) * 5 - 1, ' ')

                    new_num = ''.join(ints)
                    if dec_pres:
                        new_num += '.' + ''.join(decs)

                if minus:
                    new_num = '-' + new_num

            else:
                new_num = str(denary)
                if minus:
                    new_num = '-' + str(denary)

            # 2.2.4 The New Numbers
            new_nums.append(new_num)

        # 3 Display
        if minus:
            num_input = '-' + num_input
        print(
            f'═════\n{from_base}: {base_name(from_base)}\n-\n{num_input + base_note(from_base)}\n'
        )

        for i, base in enumerate(to_bases):
            print(
                f'═════\n{base}: {base_name(base)}\n-\n{new_nums[i] + base_note(base)}\n'
            )

        with suppress(KeyboardInterrupt):
            input('-----\nPress ENTER to continue')

        clear()

if __name__ == '__main__':
    main()