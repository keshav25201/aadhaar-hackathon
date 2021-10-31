const reloadBtn = document.getElementById('reloadBtn');
const OtpBtn = document.getElementById('OtpBtn');
const captcha_image = document.getElementById('captcha_image');
const registerBtn = document.getElementById('registerBtn');
const Captcha = document.getElementById('Captcha');
const mobile = document.getElementById('mobile');
const aadhaar = document.getElementById('aadhaar');
const password = document.getElementById('password');
const confirm_password = document.getElementById('confirm_password');
const otp = document.getElementById('otp')
const url = "http://127.0.0.1:8000/";

var captchaTxnId,OTPtxnId;
window.onload = () => {
    fetchCaptcha();
}

function fetchCaptcha()
{   
    fetch(url + 'captcha',{
        method : "GET"
    }).then(response => {
        if(!response.ok){
            throw new Error();
        }
        return response.json();
    })
    .then(data => {
        var captchaBase64String = data["captchaBase64String"];
        captchaTxnId = data["captchaTxnId"]
        captcha_image.src = 'data:image/jpeg;base64,' + captchaBase64String;
    })
    .catch(error => {
        console.log(error);
    })
}
function fetchOtp(){
    fetch(url + 'otp',{
        method : "POST",
        credentials: 'include',
        body : JSON.stringify({
            "captcha" : Captcha.value,
            "uid" : aadhaar.value,
            "captchaTxnId" : captchaTxnId
        }),
        headers : {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if(!response.ok){
            throw new Error();
        }
        return response.json();
    })
    .then(data => {
        OTPtxnId = data["OTPtxnId"]
    })
    .catch(error => {
        console.log(error)
    })
}
function Submit(event)
{
    if(password.innerText != confirm_password.innerText)return;
    fetch(url + 'signup',{
        method : "POST",
        headers : {
            'Content-Type': 'application/json',
        },
        body : JSON.stringify({
            "OTPtxnId" : OTPtxnId,
            "otp" : otp.innerText,
            "uid" : aadhaar.innerText,
            "mobile" : mobile.innerText,
            "password" : password.innerText,
        })
    }).then(response => {
        if(response.status == 200){
            window.location = url + 'home'
        }else{
            throw new Error("failed signup")
        }
    })
    .catch(error => {
        console.log(error)
    })

}
reloadBtn.addEventListener('click',fetchCaptcha);
OtpBtn.addEventListener('click',fetchOtp);
registerBtn.addEventListener('click',Submit);
