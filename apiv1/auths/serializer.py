from rest_framework.serializers import Serializer,ModelSerializer

from apiv1.filter import AccountField,Captcha6Field

class CreateCaptchaSerializer(Serializer):
  account = AccountField
  
    
class verifyCaptchaSerializer(Serializer):
  account = AccountField
  captcha = Captcha6Field
  
  
  