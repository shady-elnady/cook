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
