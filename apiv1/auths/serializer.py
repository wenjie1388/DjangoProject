from rest_framework import serializers

from apiv1.filter import AccountField,Captcha6Field

class CreateCaptchaSerializer(serializers.Serializer):
  account = AccountField()
  
    
class verifyCaptchaSerializer(serializers.Serializer):
  account = AccountField()
  captcha = serializers.CharField(
    max_length = 6,
    min_length = 6
  )
  
  
  