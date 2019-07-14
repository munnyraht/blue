import requests
def get_bvn_details(bvn_number):
    api_url=api_url=f'https://api.ravepay.co/v2/kyc/bvn/{bvn_number}?seckey=FLWSECK-175a8247e8b19e7000616c504357e556-X'
    r = requests.get(api_url)
    return r.json()