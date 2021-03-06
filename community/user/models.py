from django.db import models

# Create your models here.
class Fcuser(models.Model):
    username = models.CharField(
        max_length=32,
        verbose_name='사용자명',
    )
    useremail = models.EmailField(
        max_length=128,
        verbose_name='사용자이메일',
    )
    password = models.CharField(
        max_length=64,
        verbose_name='비밀번호',
    )
    registered_dttm = models.DateTimeField(
        # 현재 시간을 자동으로 등록한다
        auto_now_add=True,
        verbose_name='등록시간',
    )

    # Fcuser.__str__ 의 반환값으로 Fcuser.username 을 사용한다. -> /admin 에서 보여지는 값을 변경한다.
    def __str__(self):
        return self.username
    
    # Meta class 를 통해 Django 에 원하는 정보를 전달할 수 있다.
    class Meta:
        # Table 이름
        db_table = 'user'
        verbose_name = '사용자'
        # Django 는 기본적으로 verbose_name 을 복수형으로 보여준다. 
        verbose_name_plural = '사용자'