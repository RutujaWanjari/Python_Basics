# A program demonstrating twilio package usage; which is calling, messaging, etc.

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC60bfc5a840d7c34da142bde1063b4d0c"
# Your Auth Token from twilio.com/console
auth_token = "/*Your Auth Token*/"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919561557812",
    from_="+18173811351",
    body="Hello User, this message is from Python!!")

print(message.sid)




