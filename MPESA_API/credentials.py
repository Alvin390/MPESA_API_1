import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredential:
    consumer_key=""
    consumer_secret=""
    api_URL=""

class MpesaAccessToke:
    r= requests.get(MpesaC2bCredential.api_URL, auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key,
                                                                   MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']