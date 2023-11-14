from database import collection, async_collection
from utils import is_data, is_phone, is_email


class Service:
    """
    The Service class serves as a wrapper for methods containing all the business logic
    for processing requests to application endpoints.
    """
    # @staticmethod
    # def get_form(data: dict[str, str]):
    #
    #     for key, value in data.items():
    #         if len(value) == 16 and value[0] == " ":
    #             data[key] = f'+{value[1:]}'
    #     print(type(data))
    #     print(data)
    #     search_dict: dict[str, str] = {}
    #     for key, value in data.items():
    #         if is_data(value):
    #             search_dict[key] = 'data'
    #         elif is_phone(value):
    #             search_dict[key] = 'phone'
    #         elif is_email(value):
    #             search_dict[key] = 'email'
    #         else:
    #             search_dict[key] = 'text'
    #
    #     list_form = [form for form in collection.find({}, {'_id': 0})]
    #     result = None
    #     for form in list_form:
    #         form_name = form.pop('name')
    #         for item in form.items():
    #             if item not in search_dict.items():
    #                 break
    #         else:
    #             result =form_name
    #
    #     if result is None:
    #         return search_dict
    #
    #     return {'form_name': result}


    @staticmethod
    async def get_form(data: dict[str, str]) -> dict[str, str]:
        """
        The asynchronous function get_form is a static method of the Service class.
        Takes as an argument all parameters received by the handler in the body of the request
        in the form of a dictionary. Implements the basic logic for processing received data
        and generating a response. Returns the response as JSON.
        """
        search_dict: dict[str, str] = {}
        for key, value in data.items():
            if await is_data(value):
                search_dict[key] = 'date'
            elif await is_phone(value):
                search_dict[key] = 'phone'
            elif await is_email(value):
                search_dict[key] = 'email'
            else:
                search_dict[key] = 'text'

        cursor = async_collection.find({}, {'_id': 0})
        list_form: list[dict[str, str]] = [form for form in await cursor.to_list(length=100)]

        for form in list_form:
            form_name = form.pop('name')
            for item in form.items():
                if item not in search_dict.items():
                    break
            else:
                return {'form_name': form_name}

        else:
            return search_dict


