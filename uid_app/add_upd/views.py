import json
from django.contrib.auth.models import User
from django import http
from add_upd.models import Request
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from add_upd.utils import apis
# from .apis import *


def getCaptcha(request): 
    if request.method == "POST":
        return HttpResponse(status = 401)
    captcha_response_body = apis.generate_captchar()
    response = JsonResponse({
        "captchaBase64String" : captcha_response_body["captchaBase64String"],
    })
    response.set_cookie("captchaTxnId",captcha_response_body["captchaTxnId"])
    return response


def getOTP(request):
    captchaTxnId = request.COOKIES["captchaTxnId"]
    captcha = json.loads(request.body)["captcha"]
    uid = json.loads(request.body)["uid"]
    otp_response_body = apis.gen_otp(captcha,captchaTxnId,uid)
    response = HttpResponse()
    response.set_cookie("OTPtxnId", otp_response_body["txnId"])
    return response

def SignUp(request):
    OTPtxnId = request.COOKIES['OTPtxnId']
    request_body = json.loads(request.body)
    otp = request_body["otp"]
    uid = request_body["uid"]
    mobile = request_body["mobile"]
    ekyc_response_body = apis.eKYC_api(otp,OTPtxnId,uid)
    if ekyc_response_body["mobile"] == mobile:
        user = User.objects.create_user()
        return HttpResponse(status = 200)
    else:
        return HttpResponse(status = 400)

def Login(request):
    request_body = json.loads(request.body)
    mobile = 
    mo
    return HttpResponse()
def requestForSharingAddress(request):

    return HttpResponse()

def ResponseToRequestForAddress():
    return HttpResponse()
     
