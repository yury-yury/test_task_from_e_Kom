import re
from datetime import datetime
from typing import Optional


async def is_data(value: str) -> bool:
    """
    Asynchronous function is_data checks the value received as an argument in the form of a string.
    If the received value matches the date format, return True otherwise False.
    """
    if value.count('.') == 2:
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except Exception:
            return False
        else:
            return True
    elif value.count('-') == 2:
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except Exception:
            return False
        else:
            return True
    return False


async def is_phone(value: str) -> bool:
    """
    Asynchronous function is_phone checks the value received as an argument in the form of a string.
    If the received value matches the phone number format, return True otherwise False.
    """
    result: Optional[str] = re.search('^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', value)
    if result is None:
        return False
    return True


async def is_email(value: str) -> bool:
    """
    Asynchronous function is_email Checks the value received as an argument in the form of a string.
    If the received value matches the email format, return True otherwise False.
    """
    result: Optional[str] = re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', value)
    if result is None:
        return False
    return True
