import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredential:
    consumer_key=""
    consumer_secret=""
    api_URL=""

class MpesaAccessToken:
    r= requests.get(MpesaC2bCredential.api_URL, auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key,
                                                                   MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

class LipanaMpessaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = ""
    OffSetValue = ""
    passkey = ""
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
    print(decode_password)