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
            print(meassage.sid)
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
            print(meassage.sid)
            return meassage.sid
        except Exception as e:
            print(f"send_otp_via_whatsapp Error:{e}")

# account_sid = 'AC581b79873a392165b31f7429d2fcfcfb'
# auth_token = 'd5c961c16b402d455d56e0930cfe6bfa'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Your appointment is coming up on July 21 at 3PM',
#   to='whatsapp:+201060611123'
# )

# print(message.sid)

