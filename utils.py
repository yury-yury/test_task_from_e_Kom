import re
from datetime import datetime


def is_data(value: str) -> bool:
    if len(value) == 10:
        if value.count('.') == 2:
            try:
                dt = datetime.strptime(value, "%d.%m.%Y")
            except Exception:
                return False
            else:
                return True
        elif value.count('-') == 2:
            try:
                dt = datetime.strptime(value, "%Y-%m-%d")
            except Exception:
                return False
            else:
                return True
    return False


def is_phone(value: str) -> bool:
    # +7 xxx xxx xx xx
    if len(value) == 16:
        result = re.search('^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', value)
        if result is None:
            return False
        return True
    return False


def is_email(value: str) -> bool:
    result = re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', value)
    if result is None:
        return False
    return True


if __name__ == '__main__':
    # print(is_data('13.11.2023'))
    # print(is_phone('+7 962 446 76 71'))
    print(is_email('yuryyury@mail.ru'))
