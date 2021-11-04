import json
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import http
from add_upd import models
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from add_upd.utils import apis

# from .apis import *


def getCaptcha(request):
    if request.method == "POST":
        return HttpResponse(status=405)
    captcha_response_body = apis.generate_captchar()
    response = JsonResponse(
        {
            "captchaBase64String": captcha_response_body["captchaBase64String"],
        }
    )
    response.set_cookie("captchaTxnId", captcha_response_body["captchaTxnId"])
    return response


def getOTP(request):
    try:
        captchaTxnId = request.COOKIES["captchaTxnId"]
        captcha = json.loads(request.body)["captcha"]
        uid = json.loads(request.body)["uid"]
        otp_response_body = apis.gen_otp(captcha, captchaTxnId, uid)
        response = HttpResponse()
        response.set_cookie("OTPtxnId", otp_response_body["txnId"])
        return response
    except KeyError:
        return HttpResponse(401)


def SignUp(request):
    OTPtxnId = request.COOKIES["OTPtxnId"]
    request_body = json.loads(request.body)
    otp = request_body["otp"]
    uid = request_body["uid"]
    mobile = request_body["mobile"]
    password = request_body["password"]
    ekyc_response_body = json.loads(apis.eKYC_api(otp, OTPtxnId, uid))
    uidData = ekyc_response_body["eKycString"]["KycRes"]["UidData"]
    ekyc_mobile = uidData["Poi"]["@phone"]
    ekyc_name = uidData["Poi"]["@name"]
    if ekyc_mobile == mobile:
        user = User.objects.create_user(username=mobile, password=password)
        user.first_name = ekyc_name
        # add name
        user.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def Login(request):
    login_data_body = json.loads(request.body)
    mobile = login_data_body["mobile"]
    password = login_data_body["password"]
    user = authenticate(username=mobile, password=password)
    if user is not None:
        login(request, user)
        # get the records to display after login
        sent_requests = models.req_address.objects.get(From=user)
        recieved_requests = models.req_address.objects.get(To=user)
        return JsonResponse({"sent": sent_requests, "recieved": recieved_requests})
    else:
        return HttpResponse(status=400)


def requestForSharingAddress(request):
    request_body = json.loads(request.body)
    user = request.user
    Transaction = models.req_address(From=user, To=request_body["mobile"])
    Transaction.save()
    return HttpResponse(status=200)


def requestForMoreInfo(request):
    request_body = json.loads(request.body)
    user = request.user
    Transaction = models.req_info(From=user, To=request_body["mobile"])
    Transaction.save()
    return HttpResponse(status=200)


def shareInfo(request):
    OTPtxnId = request.COOKIES["OTPtxnId"]
    request_body = json.loads(request.body)
    if request_body["permission"] == "accepted":
        otp = request_body["otp"]
        uid = request_body["uid"]
        ekyc_response_body = json.loads(apis.eKYC_api(otp, OTPtxnId, uid))
        uidData = ekyc_response_body["eKycString"]["KycRes"]["UidData"]
        ekyc_name = uidData["Poi"]["@name"]
        ekyc_mobile = uidData["Poi"]["@phone"]
        ekyc_photo_byte64_string = uidData["Pht"]
        response = JsonResponse(
            {
                "info": {
                    "name": ekyc_name,
                    "mobile": ekyc_mobile,
                    "photo": ekyc_photo_byte64_string,
                },
                "status": "y",
            }
        )
    else:
        response = JsonResponse(
            {
                "info": {
                    "name": None,
                    "mobile": None,
                    "photo": None,
                },
                "status": "n",
            }
        )

    return response


def sendAddressToUser(request):
    request_body = json.loads(request.body)
