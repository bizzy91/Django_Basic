from django.contrib import admin
# models.py 에서 생성한 객체 가져온다.
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    # 표시할 형태 tuple 로 선언한다.
    list_display = ('username', 'password')

# /admin 페이지에 등록한다.
admin.site.register(Fcuser, FcuserAdmin)