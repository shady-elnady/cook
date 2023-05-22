from django.conf import settings
from twilio.rest import Client


class TwilioMessageHandler:
    mobile=None
    otp=None
    def __init__(self,mobile,otp) -> None:
        self.mobile=mobile
        self.otp=otp
    def send_otp_via_message(self):     
        client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(
            body=f'your otp is:{self.otp}',
            from_=settings.TWILIO_mobile,
            to=f'{settings.COUNTRY_CODE}{self.mobile}',
        )
    def send_otp_via_whatsapp(self):     
        client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(
            body=f'your otp is:{self.otp}',
            from_=f'{settings.TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{settings.COUNTRY_CODE}{self.mobile}',
        )
