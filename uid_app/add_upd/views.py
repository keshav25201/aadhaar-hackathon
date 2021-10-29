import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from add_upd.utils import OTP
# from .OTP import *
def SignUp(request):
    
def getCaptcha(request): 
    if request.method == "POST":
        return HttpResponse(status = 401)
    captcha_response_body = OTP.generate_captchar()
    response = JsonResponse({
        "captchaBase64String" : captcha_response_body["captchaBase64String"],
    })
    response.set_cookie("captchaTxnId",captcha_response_body["captchaTxnId"])
    return response
def getOTP(request):
    captchaTxnId =  request.COOKIES["captchaTxnId"]
    captcha = json.loads(request.body)["captcha"]
    otp_response_body = OTP.gen_otp(captcha,captchaTxnId)
    response = HttpResponse()
    response.set_cookie('OTPtxnId',otp_response_body["txnId"])
    return response


     
