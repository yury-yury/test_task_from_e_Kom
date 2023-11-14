from fastapi import APIRouter, Depends, Request, Body

from services import Service


router = APIRouter()


# @router.post('/get_form', )
# def get_form(data: Request, service: Service = Depends() ):
#     data_dict = dict(data.query_params)
#
#     return service.get_form(data_dict)


@router.post('/get_form', summary='Get the name of the form or a list of fields with data types.')
async def get_form(data: dict = Body(), service: Service = Depends()) -> dict[str, str]:
    """
    The asynchronous function get_form is a representation for processing requests using the
    POST method to the UPL address "/get_form". Accepts parameters - a data object containing
    all the data received from the request body in the form of a dictionary and an instance
    of the Service class in the form of a dependency. Returns the result of the Service class method as JSON.
    """
    return await service.get_form(data)