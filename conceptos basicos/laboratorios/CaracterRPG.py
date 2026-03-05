full_dot = '●'
empty_dot = '○'

def validate_name(name):
    if not isinstance(name, str):
        return 'El caracter deberia se un string'
    if not name:
        return "El caracter deberia tenner un nombre"
        

    if len(name) > 10:
        return 'El nombre del caracter es muy largo'
    if " " in name:
        return 'El nombre del caracter no debe contener espacios'


def validate_stats(strength, intelligence, charisma): #defino la funcion validate_stats con los parametros strength, intelligence y charisma
    for stat in (strength, intelligence, charisma): #recorro cada estadistica en la tupla (strength, intelligence, charisma)
        if not isinstance(stat, int):
            return 'Todas las estadisticas deberian ser enteros'

    for stat in (strength, intelligence, charisma):
        if stat < 1:
            return 'Todas las estadisticas deberian ser no menores que 1'

    for stat in ( strength, intelligence, charisma):
        if stat > 4:
            return 'Todas las estadisticas deberian ser no mas de 4'
    
    if strength + intelligence + charisma != 7:
        return 'El caracter deberia comenzar con 7 puntos'

def create_dots(stat):
    return stat * full_dot + empty_dot * (10 - stat)


def create_character(name, strength, intelligence, charisma):
    name_error = validate_name(name)
    if name_error:
        return name_error

    stats_error = validate_stats(strength, intelligence, charisma)
    if stats_error:
        return stats_error

    return (
        f'{name}\n'
        f'STR {create_dots(strength)}\n'
        f'INT {create_dots(intelligence)}\n'
        f'CHA {create_dots(charisma)}'
    )
result = create_character('ren', 4, 2, 1)
print(result)