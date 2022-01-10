import re
import datetime

regex_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regex_phone = '^[0-9]{9}$'

class Validations:

    def __init__(self):
        pass

    def validateName(self, name):

        if len(name) < 3 or len(name) > 50:
            raise ValueError(f'The name must have a minimum of 3 characters and a maximum of 50 characters, current size: {len(name)}')
        return True

    def validateSurname(self, surname):

        if len(surname) < 5 or len(surname) > 100:
            raise ValueError(f'The surnames must have a minimum of 5 characters and a maximum of 100 characters, current size: {len(surname)}')
        return True


    def validateEmail(self, email):
        if not re.search(regex_email, email):
            raise ValueError('El formato del email no es válido')
        return True

    def validatePhone(self, phone):
        if not re.search(regex_phone, phone):
            raise ValueError('El formato del teléfono no es válido, debe ser un número de 9 cifras sin guiones ni puntos')
        return True


    def validateBirthday(self, birthday):
        try:
            datetime.datetime.strptime(birthday, '%Y-%m-%d')
        except ValueError:
            raise ValueError('El formato de la fecha es incorrecta, debe ser YYYY-MM-DD')
        return True