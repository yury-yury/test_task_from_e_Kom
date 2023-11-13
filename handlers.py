import urllib
from urllib import request

from fastapi import APIRouter, Query, Depends, Request, Body

from services import Service

router = APIRouter()


# @router.post('/get_form', )
# def get_form(data: Request, service: Service = Depends() ):
#     data_dict = dict(data.query_params)
#
#     return service.get_form(data_dict)


@router.post('/get_form', )
def get_form(data: dict = Body(), service: Service = Depends() ):

    return service.get_form(data)