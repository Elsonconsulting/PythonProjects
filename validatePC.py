# postcode api youtube vid https://www.youtube.com/watch?v=9iTBvjEnIg4
# uses Postcodes.io
# Does not work now but have a look and figure out!


import urllib.request as req
import json

def loadJsonResponse(url):
    return json.loads(req.urlopen(url).read())

def validatePostcode(postcode):
    url = 'https://api.postcodes.io/postcodes/{}/validate.format(postcode)'

print(validatePostcode('NG71PS'))