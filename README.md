### git 설정
```
$ git init
$ git add README.md
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/bizzy91/Python.git
$ git push -u origin main
```

### 가상환경
가상환경을 위한 virtualenv 설치
```
$ python3 -m pip3 install --user -U virtualenv
```
현재 경로에서 가상환경을 위한 하위 경로 생성하기
```
$ virtualenv django_vnev
```
특정 버전을 지정하려면 아래 명령어를 추가한다.
```
$ virtualenv [경로 이름] --python=[python version]
(example)$ virtualenv django_venv --python=python3.8
(example)$ virtualenv django_venv --python=python3.9
```
가상 환경 활성화
```
$ source django_vnev/bin/activate
```
가상 환경 비활성화
```
$ deactivate
```
### Django
Django 설치하기
```
$ pip3 install django
```
프로젝트 시작하기
```
$ django-admin startproject [프로젝트 이름]
$ django-admin startproject community 
```
Django 실행하기
```
./community $ python3 manage.py runserver
```
앱 만들기
프로젝트 경로로 들어 간 뒤 아래 명령어 입력
```
$ cd community
$ django-admin startapp [앱 이름]
$ django-admin startapp board
$ django-admin startapp user
```
앱을 만든 후 ./community/setting.py 에 추가한다.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'user'
]
```
Model 생성/수정 후

생성/수정한 모델을 바탕으로 DB의 틀이 되는 class 를 생성/수정한다.
```
./community $ python3 manage.py makemigrations
```
INSTALLED_APPS 에 있는 앱들이 사용하는 테이블을 생성하여 준다.
```
./community $ python3 manage.py migrate
```
./community/settings.py 의 DATABASES 에서 어떤 DB 를 사용할 것인지 고를 수 있다. default 는 sqlite3

Super User 만들기
```
./community $ python3 manage.py createsuperuser
```

/admin 페이지에 나타나는 내용 관리하기 (./[앱 이름]/admin.py)
```
from django.contrib import admin
# models.py 에서 생성한 객체 가져온다.
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    # 표시할 형태 tuple 로 선언한다.
    list_display = ('username', 'password')

# /admin 페이지에 등록한다.
admin.site.register(Fcuser, FcuserAdmin)
```