import requests
# from urllib.request import urlopen, Request
# import urllib.error
# import json

# # api_url=f'https://api.ravepay.co/v2/kyc/bvn/{bvn_number}?seckey=FLWSECK-175a8247e8b19e7000616c504357e556-X'
# def get_bvn_details(bvn_number):
#     api_url=f'https://api.ravepay.co/v2/kyc/bvn/{bvn_number}?seckey=FLWSECK-175a8247e8b19e7000616c504357e556-X'
#     data = json.dumps({'number': bvn_number})
#     byteData = bytes(data, encoding="utf8")
#     req = Request(api_url,data=byteData, method="POST")
#     req.add_header("Content-Type", "application/json")
#     resp = urlopen(req)
#     response= resp.read()
#     bvndata = json.loads(response)
#     return bvndata


def get_bvn_details(bvn_number):
    api_url=api_url=f'https://api.ravepay.co/v2/kyc/bvn/{bvn_number}?seckey=FLWSECK-175a8247e8b19e7000616c504357e556-X'
    r = requests.get(api_url)
    return r.json()