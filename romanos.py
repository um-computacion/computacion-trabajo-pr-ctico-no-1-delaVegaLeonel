def roman_to_decimal(roman):
    if roman == 'I':
        return 1
    elif roman == 'II':
        return 2
    elif roman == 'III':
        return 3
    elif roman == 'IV':
        return 4
    elif roman == 'V':
        return 5
    elif roman == 'VI':
        return 6
    elif roman == 'VII':
        return 7
    elif roman == 'VIII':
        return 8
    elif roman == 'IX':
        return 9
    else:
        raise ValueError('Número romano no soportado')
