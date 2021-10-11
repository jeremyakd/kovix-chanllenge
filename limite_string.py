_string_input = input('Ingrese una cadena para formatear por favor.\n')
_limit_input = int(input('Ingrese límite por favor.'))


def clean_string(_string, _limit):

    if _limit == 0 or _string.replace(' ', '') == '' :
        print('Sin resultado.')
    else:
        order_char = ''
        actual_char = ''
        cant_chart = 0

        for s in _string:
            if actual_char != s and cant_chart <= _limit:
                actual_char = s
                order_char += actual_char
                cant_chart = 1
            elif cant_chart < _limit:
                order_char += s
                cant_chart += 1
        print('Cadena de texto ordenada. ', order_char)


clean_string(_string_input, _limit_input)
