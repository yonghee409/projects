from django.db import models

# 이하 테스트 코드

class ApiKeyset(models.Model):
    user        = models.ForeignKey('auth.User')
    alias       = models.CharField(max_length=20)
    apikey      = models.CharField(max_length=50)
    apisecret   = models.CharField(max_length=50)
