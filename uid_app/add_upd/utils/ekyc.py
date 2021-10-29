import requests


def eKYC_api(otp, txnID):
    URL = "https://stage1.uidai.gov.in/onlineekyc/getEkyc/"
    json_data = {"uid": "999911588232", "txnId": txnID, "otp": str(otp)}
    response = requests.post(url=URL, json=json_data)
    print(response.text)
    return
