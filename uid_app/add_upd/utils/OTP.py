import requests, uuid

# import base64


def generate_captchar():
    Url = "https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/get/captcha"
    dat = {"langCode": "en", "captchaLength": "3", "captchaType": "2"}
    response = requests.post(url=Url, json=dat)
    # print(response.text)
    return response.json()


def gen_otp(captcha, txnId):
    obj = uuid.uuid4()
    string = str(obj)
    headers = {
        "x-request-id": "a5747bf7-1dc0-4995-bb27-c5f3728baca7",
        "appid": "MYAADHAAR",
        "Accept-Language": "en_in",
        "Content-Type": "application/json",
    }
    json_data = {
        "uidNumber": "999911588232",
        "captchaTxnId": txnId,
        "captchaValue": captcha,
        "transactionId": "MYAADHAAR:86ddc9b5-36e4-47fa-a947-9ff55d931d6a",
    }
    URL = (
        "https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/generate/aadhaar/otp"
    )
    response = requests.post(url=URL, json=json_data)
    return response.json()
    


def auth_api(otp, txnID):
    URL = "https://stage1.uidai.gov.in/onlineekyc/getAuth/"
    json_data = {"uid": "999911588232", "txnId": txnID, "otp": str(otp)}
    response = requests.post(url=URL, json=json_data)
    return response.json()


# def read_image(response):
#     imgdata = base64.b64decode(response["captchaBase64String"])
#      print(imgdata)
#     filename = "some_image.jpg"  # I assume you have a way of picking unique filenames
#     with open(filename, "wb") as f:
#         f.write(imgdata)
#     return


captcha_response = generate_captchar()

if captcha_response["status"] == "Success" and captcha_response["statusCode"] == 200:

    captchaBase64String = captcha_response["captchaBase64String"]  # send to front end
    # recieve captcha string from front end
    # send captchaTxnId and captcha string to get_otp()
    captcha = "from front end"
    otp_response = gen_otp(captcha, captcha_response["captchaTxnId"])

    if otp_response["status"] == "Success":
        # send msg to front end otp_response[“message”]
        # fetch otp from front end
        # call auth ap to verify otp and proceed
        otp = 000000
        auth_response = auth_api(otp, otp_response["txnId"])
        if auth_response["status"] == "y":
            # send msg to front end that vefification succesful
            pass
        else:
            raise Exception("OTP entered is not correct")
    else:
        raise Exception("OTP could not be generated. Please try again.")
else:
    raise Exception(
        "status = ",
        captcha_response["status"],
        "status code = ",
        captcha_response["statusCode"],
    )

# # print(captchaBase64String)

# # read_image()
# # gen_otp()
# """1. run generate_captcha() function, replace the value of captchaTxnId and cpt (captchabase64) from the response recieved.
# 2. run read_image() function and manually read the captcha from the image
# 3. replace this captcha in captchaValue 
# 4. run gen_otp() function"""
