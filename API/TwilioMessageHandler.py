from django.conf import settings
from twilio.rest import Client


class TwilioMessageHandler:
    mobile=None
    otp=None
    def __init__(self,mobile,otp) -> None:
        self.mobile=mobile
        self.otp=otp
    def send_otp_via_message(self):     
        try:
            client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
            meassage = client.messages.create(
                body=f'your otp is:{self.otp}',
                from_=settings.TWILIO_PHONE_NUMBER,
                to=f'{settings.COUNTRY_CODE}{self.mobile}',
            )
            return meassage.sid
        except Exception as e :
            print(f"send_otp_via_message Error: {e}") 
        
    def send_otp_via_whatsapp(self):     
        try:
            client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
            meassage = client.messages.create(
                body=f'your otp is:{self.otp}',
                from_=f'{settings.TWILIO_WHATSAPP_NUMBER}',
                to=f'whatsapp:{settings.COUNTRY_CODE}{self.mobile}',
            )
            return meassage.sid
        except Exception as e:
            print(f"send_otp_via_whatsapp Error:{e}")


# #####
# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "ACab16021d54dc03acd45e5640f84aaf17"
# auth_token = "0ee3a5fbd375483bd57db53c4f867592"
# verify_sid = "VAce0a4d5c34cd760090d7a9f7bcb3b2cd"
# verified_number = "+201061656112"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)