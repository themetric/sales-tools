import sys
import urllib
import urllib2
from termcolor import colored

if len(sys.argv) < 2:
    sys.exit("Missing phone number! \n Usage: python phone.py PHONE_NUMBER")

params = {'number': sys.argv[1]}

url = "https://api.opencnam.com/v2/phone/" + params["number"]
print "Making request to " + url

try:
  req = urllib2.Request("https://api.opencnam.com/v2/phone/" + params["number"])
  resp = urllib2.urlopen(req)
  print colored(resp.read(), 'green')
except urllib2.HTTPError, e:
  codes = {
    404: ["Couldn't find that number", "red"],
    403: ["Throttle limit exceeded -- max is 10/hour", "yellow"],
    "default": ["Unknown HTTP error occurred", "red"]
  }
  if e.code in codes:
    message = codes[e.code]
  else:
    message = codes["default"]
  print colored(message[0], message[1])
except urllib2.URLError, e:
  print colored(e.args, 'red')