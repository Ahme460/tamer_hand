import requests
import hmac
import hashlib
import time
import json

def hmac_sha256(secret_key, data):
    hmac_digest = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).digest()
    return hmac_digest

APIKey = '0S8T25YWNJWUN6CD27QH2190kfLtXwhpbnGFdkGuHK7mmX-ms'
sharedSecret = 'zTOhPP4N+u$$2Wtoazv2d-p$cO}Od0@MyDF1{E7F'
URI = 'settlementv1/latest'
QS = 'apikey=' + APIKey
timeStampUTC = str(int(time.time()))
payload = ''
message = timeStampUTC + URI + QS + payload

HMACDigest = hmac_sha256(sharedSecret, message)
encodedDigest = HMACDigest.hex()
XPayToken = 'xv2:' + timeStampUTC + ':' + encodedDigest
print(XPayToken)
headers = {
    'x-pay-token': XPayToken
}
payload = {
                "msgIdentfctn": {
                    "clientId": "1VISAGCT000001",
                    "correlatnId": "12bc567d90f23e56a8f012",
                    "origId": "123451234567890"
                },
                "Body": {
                    "Envt": {
                        "Accptr": {
                            "AddtlData": {
                                "Tp": "ISOid",
                                "Val": "42999952606"
                            },
                            "AddtlId": "52014057",
                            "AddtlIds": {
                                "Tp": "GtyMrchntData",
                                "Val": "V070990024552"
                            },
                            "Adr": {
                                "Ctry": "US",
                                "CtrySubDvsnMjr": "48",
                                "CtrySubDvsnMnr": "002",
                                "PstlCd": "78641"
                            },
                            "CstmrSvc": "14155552235",
                            "FrgnRtlrInd": False,
                            "Id": "GCTstore",
                            "PaymentFacltId": "52014057",
                            "ShrtNm": "ABC Supplies",
                            "SpnsrdMrchnt": {
                                "Id": {
                                    "Id": "520140578465770"
                                }
                            },
                            "Card": {
                                "CardSeqNb": "0200",
                                "Trck1": "B4000222357994675^CHARLES                   ^230420100558222222",
                                "Trck2": {
                                    "HexBinryVal": "04000220130005421D230620100222222222"
                                }
                            },
                            "Termnl": {
                                "Cpblties": {
                                    "CardRdngCpblty": "MGST",
                                    "CrdhldrVrfctnCpblty": {
                                        "Cpblty": "NOOP"
                                    },
                                    "PINLngthCpblties": "05"
                                },
                                "TermnlId": {
                                    "Id": "VGCTapi1"
                                }
                            }
                        }
                    }
                }
            }

url = "https://sandbox.api.visa.com/acs/v3/payments/authorizations"

response = requests.post(
    url=url,
    headers=headers,
    json=payload
)





print(response.json())