from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from add_upd.utils.OTP import *
# from .OTP import *

def getCaptcha(request): 
    captcha_response_body = OTP.generate_captchar()
    return JsonResponse(captcha_response_body)
