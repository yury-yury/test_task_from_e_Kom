from database import collection
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
    def get_form(data: dict[str, str]):
        search_dict: dict[str, str] = {}
        for key, value in data.items():
            if is_data(value):
                search_dict[key] = 'date'
            elif is_phone(value):
                search_dict[key] = 'phone'
            elif is_email(value):
                search_dict[key] = 'email'
            else:
                search_dict[key] = 'text'

        list_form = [form for form in collection.find({}, {'_id': 0})]

        result = None
        for form in list_form:
            form_name = form.pop('name')
            for item in form.items():
                if item not in search_dict.items():
                    break
            else:
                result =form_name

        if result is None:
            return search_dict

        return {'form_name': result}
