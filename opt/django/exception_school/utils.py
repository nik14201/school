from rest_framework.views import exception_handler
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import set_rollback

def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        name="Error"
        errors=[]
        if isinstance(exc.detail, (list, dict)):
            for mes in exc.detail:
                if mes in exc.detail:
                    detail = exc.detail[mes][0] if exc.detail[mes] else "Неизвестная ошибка"
                    name = mes
                    errors.append({
                        "name": name,
                        "message": detail,
                    })
                else:
                    detail = exc.detail
                    errors.append({
                        "name": "Error",
                        "message": detail,
                    })
            # if 'new_password2' in  exc.detail:
            #     detail = exc.detail['new_password2'][0] if exc.detail['new_password2'] else "Ошибка ввода пароля"
            # elif 'email' in  exc.detail:
            #     detail = exc.detail['email'][0] if exc.detail['email'] else "Ошибка ввода пароля"
            # else:
            #     detail = exc.detail
        else:
            detail = exc.detail
        data={
            "type": "Error",
            "message": detail,
            "errors": errors,
        }
        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)
    return None

