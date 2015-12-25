import re
from twilio.rest import TwilioRestClient

### first we read the patterns.txt file to know last failures###

fileobj = open("/home/raina/patterns.txt",'r')
filedata = fileobj.read() ###read whole file in string###

len1 = len(filedata) ###previous number of failures###
print len1
fileobj.close()

### Now person attempts authorization,so more failures get logged in auth.log###
###Read the failures again###

fobj = open("/var/log/auth.log",'r')
strdata = fobj.read()
fobj.close()

matches = re.findall("authentication failure",strdata)
###Use regex to find all failure patterns
### Findall returns a list

fileobj = open("/home/raina/patterns.txt",'w+')

for i in range(0,len(matches)):
    fileobj.write(matches[i] + "\n")
fileobj.close()

fileobj = open("patterns.txt",'r')
strdata = fileobj.read()
len2 = len(strdata)
print len2
fileobj.close()

if len2 > len1:


# To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXX"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
    body="Someone just attempted a failed authentication on your laptop",  # Message body, if any
    to="YOUR PH.NO",
    from_="YOUR TWILIO PH.NO",
    )
