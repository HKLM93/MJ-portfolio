# ๐210917_PJT ๊ดํตํ๋ก์ ํธ 6

## ๐์ฌ์ฉ์ ์ธ์ฆ๊ธฐ๋ฐ ์น ์๋น์ค ๊ตฌํ

### ๐งญ๋ชฉํ

-  ๋ฐ์ดํฐ๋ฅผ ์์ฑ, ์กฐํ, ์์ , ์ญ์ ํ  ์ ์๋ Web application ์ ์
-  Django web framework๋ฅผ ํตํ ๋ฐ์ดํฐ ์กฐ์
- Authentication(์ฌ์ฉ์ ์ธ์ฆ)์ ๋ํ ์ดํด



## ๐๋ฌธ์ ํ์ด

### A. ํ๋ก์ ํธ ๊ตฌ์กฐ(๊ธฐ๋ณธ ์ค์ )

1. ๊ฐ์ํ๊ฒฝ ์ค์น

```
$ python -m venv venv
```



2. pip ์ค์น 

- ์ฅ๊ณ ๋ ๊ธฐ๋ณธ์ ์ผ๋ก ์ค์นํด์ผ ํ๊ณ  ํน์ ๋ชฐ๋ผ์ extensions๋ ์ค์นํ๋ค. 
- requirements ํ์ผ์ ๋ค์ด๋ฐ์ pip๋ฅผ ์๋ ฅํด์ฃผ์๋ค.

```
$ pip install django django-extensions
$ pip freeze > requirements.txt
```



3. ํ๋ก์ ํธ ๋ฐ ์ ํ๋ฆฌ์ผ์ด์ ๋ง๋ค๊ธฐ

- ํ๋ก์ ํธ ์ด๋ฆ์ pjt06์ด๊ณ  ์ ํ๋ฆฌ์ผ์ด์์ ์ด๋ฆ์ community, accounts์ด๋ค. 

```
$ django-admin startproject pjt06
$ python manage.py startapp community
$ python manage.py startapp accounts
```



4. settings.py์ ์ค์ 

- ์ ํ๋ฆฌ์ผ์ด์๊ณผ ์ฅ๊ณ  ์ต์คํ์์ INSTALLED_APPS์ ๋ฑ๋กํด์ฃผ์๋ค
- TEMPLATES ์์ base.html์ ์ฝ์ ์ ์๋๋ก BASE_DIR์ ๋ฑ๋กํด์ฃผ์๋ค.
- ์ธ์ด์ ์๊ฐ์ ํ๊ตญ์ด, ํ๊ตญ์๊ฐ์ผ๋ก ๋ง์ถ์๋ค. 

```
# pjt06/settings.py

...
INSTALLED_APPS = [
    # local
    'community',
    'accounts',

    # third-party
    'django_extensions',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

...
```



5. base.html ๋ง๋ค๊ธฐ

- ๋ชจ๋  ํ์ผ์ base.html์ ํ์ฅํ์ฌ ์ฌ์ฉํ๊ธฐ ์ํด ๋ค๋น๊ฒ์ด์ ๋ฐ์ ๊ฐ์ด ๋ง๋ค์ด์ค๋ค. 
- ์ฌ์ฉ์๊ฐ ์ธ์ฆ๋์ด ์์ผ๋ฉด **๋ฆฌ๋ทฐ ์์ฑํ์ด์ง์ ๋ก๊ทธ์์** ์ธ์ฆ๋์ด ์์ง ์์ผ๋ฉด **๋ก๊ทธ์ธ ํ์ด์ง์ ํ์๊ฐ์** ๋งํฌ๋ฅผ ํ์ํ๋ค.

![11111](README.assets/11111.png)

```
# templates/base.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        ReviewPage
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'community:index' %}">Home</a>
          </li>
          {% if request.user.is_authenticated %}
            <li>
              <a class="nav-link active" href="{% url 'community:create' %}">Create</a>
            </li>
            <li class="nav-item">
              <form action="{% url 'accounts:logout' %}" method="POST">
                {% csrf_token %}
                <input class="text-dark bg-light" type="submit" value="Logout">
              </form>
            </li>
          {% else %}
            <li>
              <a class="nav-link active" href="{% url 'accounts:signup' %}">Signup</a>
            </li>
            <li>
              <a class="nav-link active" href="{% url 'accounts:login' %}">Login</a>
            </li>
          {% endif %}
        </ul>
      </div>
    </div>
  </nav>
  <div class="container">
    <h3>Hello, {{ request.user }}</h3>
    <br>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
</body>
</html>
```



6. urls.py ์ค์ 

- ํ๋ก์ ํธ url์ด ์ ํ๋ฆฌ์ผ์ด์ ๊ฐ๊ฐ์ url๋ก ๊ฐ ์ ์๋๋ก include๋ฅผ ํตํด ๊ฒฝ๋ก๋ฅผ ๋ง๋ค์๋ค.

```
# pjt06/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
]
```



### B. Model ์ค์ 

- ๋ฌธ์ ์์ ํ๋๋ช์ movie_title, title, content, rank๋ก ์ค์ ํ๋ผ๊ณ  ํด์ ์ด๋ฅผ ๊ฐ๊ฐ ์ค์ ํด์ฃผ์๋ค.
- rank๋ ๋ฌด์ ํ์ผ๋ก ์ค์ ํ  ์ ์๊ฒ ๋ณ์ ์ฒ๋ผ 1-5๊น์ง๋ง ํ  ์ ์๋๋ก ์ ํ์ ๋์๋ค.
- admin ํ์ด์ง์์ ์ํ์ ๋ชฉ๊ณผ ๋ฆฌ๋ทฐ์ ๋ชฉ์ด ๋์์ ๋์ค๋๋ก fstring์ ์ฃผ์๋ค.
- ๋ชจ๋ธ์ ์ค์ ํ ํ์ migrate๋ฅผ ํด์ฃผ์๋ค.

```
# community/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.movie_title}: {self.title}'
```

```
$ python manage.py makemigrations
$ python manage.py migrate
```



### C. Form ์ค์ 

- ๋ฌธ์ ์ ์๊ตฌ๋๋ก forms.py๋ฅผ ๋ง๋ค์ด ์ฅ๊ณ ์ ModelForm์ ์ฌ์ฉํ๋ค.
- ์ถ๊ฐ ์ค์ ์ ํตํด ํผ์ ๋ํ๋๋ movie_title, title, content, rank์ ๋ํ ์ค์ ์ ํด์ฃผ์๋ค.  

```
# community/forms.py

from django import forms
from django.forms.widgets import TextInput
from .models import Review
 
class ReviewForm(forms.ModelForm):
    movie_title = forms.CharField(
        label = '์ํ ์ ๋ชฉ',
        widget = forms.TextInput(
            attrs = {
                'class': 'my-moive_title',
                'placeholder': 'Enter the movie_title',
                'maxlength': '100',

            }   
        ),
    )

    title = forms.CharField(
        label = '๋ฆฌ๋ทฐ ์ ๋ชฉ',
        widget = forms.TextInput(
            attrs = {
                'class': 'my-title',
                'placeholder': 'Enter the review title',
                'maxlength': '100',

            }   
        ),
    )

    content = forms.CharField(
        label = '๋ฆฌ๋ทฐ ๋ด์ฉ',
        widget = forms.Textarea(
            attrs = {
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 150,
            }
        ),
        error_messages={
            'required': '๋ด์ฉ์ด ํ์ํฉ๋๋ค'
        },
    )

    rank = forms.IntegerField(
        label = '์ ์',
        widget = forms.NumberInput(
            attrs = {
                'max_value': '5',
                'min_value': '1',
            } 
        ),
    )

    class Meta:
        model = Review
        fields = '__all__'
        
```



### D. Admin ์ค์ 

- ๊ด๋ฆฌ์ ํ์ด์ง๋ฅผ ๋ง๋ค๊ธฐ ์ํด admin.py์ ๋ฑ๋กํด์ค๋ค.
- ๋ฑ๋ก๋ ๊ธ์ด Review๋ชจ๋ธ์ด ๋ค์ด๊ฐ๋๋ก ํด์ค๋ค.
- ๊ด๋ฆฌ์ ์์ด๋๋ admin์ผ๋ก ๋ฑ๋กํด์ค๋ค.

```
# community/admin.py

from django.contrib import admin
from .models import Review

# Register your models here.
admin.site.register(Review)
```

```
# ํฐ๋ฏธ๋ ์ฐฝ

$ python manage.py createsuperuser
```



### E. URL ์ค์ 

1. community url ์ค์ 

- ํ๋ก์ ํธ์ urls.py๋ฅผ ๋ฐ๊ณ  view๋ก ๋๊ฒจ์ฃผ๋๋ก from๊ณผ import๋ฅผ ์๋์ ๊ฐ์ด ์ค์ 
- app์ด๋ฆ์ commuinty๋ก ํ๊ณ  urlpatterns๋ ๋ฆฌ๋ทฐ๊ธ ๋ง๋ค๊ธฐ, ๋ฆฌ๋ทฐ ์์ธ ๋ด์ฉ, ๋ฆฌ๋ทฐ๊ธ ์์ , ๋ฆฌ๋ทฐ๊ธ ์ญ์ , index๋ฅผ ์ค์ 

```
# community/urls.py

from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:review_pk>/', views.detail, name = 'detail'),
    path('<int:review_pk>/update/', views.update, name = 'update'),
    path('<int:review_pk>/delete/', views.delete, name = 'delete'),
]
```



2. account url์ค์ 

- ํ์๊ฐ์๊ณผ ๋ก๊ทธ์ธ ๋ก๊ทธ์์์ ๋ง๋ ๋ค.

```
app_name='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```



### F. View & Template ์ค์ 

1.  community์ฑ์ view

- ์ฅ๊ณ  ๋ด์ ์ฌ๋ฌ ๋ชจ๋ธ๋ค์ ๋ถ๋ฌ์์ ์ด๋ฅผ ์ ์ฉ์์ผฐ๋ค. 
- ๋ฆฌ๋ทฐ๊ธ์ ์์ฑ, ์์ , ์ญ์ ๋ ๋ก๊ทธ์ธํ ์ ์ ๋ค๋ง ์ฌ์ฉํ  ์ ์๋๋ก require_safe๋ฅผ ์ค์ ํ๋ค.
- ์์  ํ์ด์ง์ ์ญ์ ๋ฒํผ์ ๋๋ฅด๋ฉด ๊ธ์ด ์ญ์  ๋๋ค.

![image-20210917190231116](README.assets/image-20210917190231116.png)

```
# community/view.py

from django import forms
from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)

    
@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk =review_pk)
    context = {
        'review': review,
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review.pk) 
    else:
        form = ReviewForm(instance = review)
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'community/update.html', context)

@login_required
@require_POST
def delete(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    if request.method == 'POST':
        review.delete()
        return redirect('community:index')
    else:
        return redirect('community:detail', review.pk)
```



2. community์ html 

- create.html์ formํ์์ ๋ฐ์์ ์ถ๋ ฅ๋๋๋ก ํ๋ค.
- detail.html์ ๋ฆฌ๋ทฐ์ ์์ธ ๋ด์ฉ์ด ๋์ค๋๋ก ์ถ๋ ฅํ๋ค.
- index.html์ ๋ฑ๋ก๋ review๋ค์ด ์ฐจ๋ก๋๋ก ๋์ค๋๋ก for๋ฌธ์ ์ฌ์ฉํ๋ค.
- update.html ํด๋น ๋ฆฌ๋ทฐ์ ๋ํด์ form์ ๋ฐ์ ์์ฑํ  ์ ์๋๋ก ํ๋ค.

![image-20210917185823370](README.assets/image-20210917185823370.png)

```
# community/templates/community/create.html

{% extends 'base.html' %}

{% block content %}
  <h1>์ํ ๋ฆฌ๋ทฐ ์ฐ๊ธฐ</h1>
  <form action="{% url 'community:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'community:index' %}">[back]</a>
{% endblock content %}
```

![image-20210917190024633](README.assets/image-20210917190024633.png)

```
# community/templates/community/detail.html

{% extends 'base.html' %}

{% block content %}
  <h1>๋ฆฌ๋ทฐ ์์ธ ๋ด์ฉ</h1>
  <hr>
  <p> ์ํ ์ ๋ชฉ: {{ review.movie_title }}</p>
  <p> ๋ฆฌ๋ทฐ ์ ๋ชฉ: {{ review.title }}</p>
  <p> ๋ฆฌ๋ทฐ ๋ด์ฉ: {{ review.content }}</p>
  <p> ์ ์: {{ review.rank }}</p>
  <hr>
  <a href="{% url 'community:update' review.pk %}" class="btn btn-primary">[UPDATE]</a>
  <form action="{% url 'community:delete' review.pk %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-danger">DELETE</button>
  </form>
  <a href="{% url 'community:index' %}" class="btn btn-primary">[back]</a>
{% endblock content %}
```

![image-20210917190044904](README.assets/image-20210917190044904.png)

```
# community/templates/community/index.html

{% extends 'base.html' %}

{% block content %}
  <h1>๋ฆฌ๋ทฐ ๋ชฉ๋ก</h1>
  <hr>
  {% for review in reviews %} 
    <a href="{% url 'community:detail' review.pk %}">
    ์ํ: {{ review.movie_title }} / {{ review.title }}
    </a>
    <hr>
  {% endfor %}
{% endblock content %}
```

![image-20210917190101137](README.assets/image-20210917190101137.png)

```
# community/templates/community/update.html

{% extends 'base.html' %}

{% block content %}
  <h1>๋ฆฌ๋ทฐ ์์ </h1>
  <form action="{% url 'community:update' review.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'community:index' %}">[back]</a> 
{% endblock content %}
```



3. accounts์ view

- Signup์ ์ธ์ฆ๋ ์ฌ์ฉ์๊ฐ ์ ๊ทผํ  ๊ฒฝ์ฐ community ํ์ด์ง๋ก ๋๊ฒจ์ค๋ค.
- auth_login์ ํตํด ํ์๊ฐ์ ํ์ community ํ์ด์ง๋ก ๋๊ฒจ์ค๋ค.
- Login์ ์ธ์ฆ๋ ์ฌ์ฉ์์ธ ๊ฒฝ์ฐ Community๋ก ๋์๊ฐ๊ณ  ์๋๊ฒฝ์ฐ index๋ก ๋๋์๊ฐ๊ฑฐ๋ ๋ก๊ทธ์ธ์ ์งํํ๋ค.
- ๋ก๊ทธ์ธ์ ํ๋ฉด nav์ฐฝ์ ๋ก๊ทธ์์์ด ๋ํ๋๋ค. 

![44444](README.assets/44444.png)

```
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
    

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')
```



4. accounts์ htmlํ์ผ

- ๋ก๊ทธ์ธ๊ณผ ๊ฐ์๋ง ํผํ์์ ๋ฐ์์ ์์ฑํ๋๋ก ํ๋ค.

![33333](README.assets/33333.png)



```
# accounts/templates/accounts/login.html

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Login</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Login" class="btn btn-primary">
  </form>
  <a href="{% url 'community:index' %}" class="btn btn-danger">Back</a>

{% endblock content %}
```

![image-20210917173309496](README.assets/image-20210917173309496.png)

```
# accounts/templates/accounts/signup.html

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">ํ์ ๊ฐ์</h1>
  <hr>
  <form action=" {% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'community:index' %}" class="btn btn-danger">Back</a>
{% endblock content %} 
```



## ๐๋ฐฐ์ด์  ๋ฐ ๋๋์ 

1. ๊น๋ํ

- ๋ฐฐ์ด์  : 2๊ฐ์ง์ App์ ๊ฐ์ ๋๋ ์ ์์ฑ์ ํ ํ์ branch๋ฅผ ์ฌ์ฉํ์ฌ ์ถฉ๋๋ ๋ฐ์ํด๋ณด๊ณ  ๋ค์ local๋ก ํ์ผ์ ํฉ์น๋ฉด์ git์ ๋ํด์ ์กฐ๊ธ์ฉ ๋ฐฐ์๋๊ฐ๋ ๊ฒ ๊ฐ์ต๋๋ค.

  ์ฝ๋์์ฑ ์ค๊ฐ์ ์คํ ๋ฐ ๋น ์ง๋ถ๋ถ์ด ์์ด์ ์ค๋ฅ๊ฐ ๋ง์ด ๋ฐ์ํ์์ต๋๋ค. ๐ฅถ

  ๋ช์ฌ๋์ด ํ๋ฆฐ ๋ถ๋ถ์ ๋ง์ด ์ฐพ์์ฃผ์์ ๊ผผ๊ผผํ๊ฒ ํ๋ ๋ฐฉ๋ฒ์ ๋ง์ด ๋ฐฐ์ด ๊ฒ ๊ฐ์ต๋๋ค. 



- ๋๋์  : ์ง๋์ฃผ์ ๋ค๋ฅด๊ฒ 3๋ช์์ 2๋ช์ผ๋ก ์ค์๊ธฐ ๋๋ฌธ์ ๊ฐ์ธ์ ์ผ๋ก ํด์ผํ๋ ๋ถ๋ถ์ด ๋ง์ด ๋์๋ค. ์ง๋์ฃผ๋ณด๋ค ๋น ๋ฅด๊ฒ ํ์ง๋ ๋ชปํ์ง๋ง ๋ฐฐ์๊ฐ๋ ๋ถ๋ถ์ ๋ ๋ง๋ค๊ณ  ์๊ฐํฉ๋๋ค. ์ค๊ฐ์ ์คํ๋ ์กฐ๊ธ ์์ด์ ์ฃ์กํ ๋ถ๋ถ๋ ์์๊ณ  ๋ง์ด ์ฐพ์์ฃผ์์ ํ๋ฒ ๋ ์ ๊ฒํ๊ณ  ๋ฐฐ์ธ ์ ์๋ ๊ธฐํ๊ฐ ๋ ๊ฒ ๊ฐ์ต๋๋ค. ์๊ฐ์์ ์์ฑ์ ํ์์ง๋ง ๊พธ๋ฏธ์ง๋ ๋ชปํ์ฌ์ ๋ง์ด ์์ฝ๊ณ  ์ฅ๊ณ ๋ฅผ ์กฐ๊ธ ๋ ์ด์ฌํ ์ฐ์ตํด์ ๋น ๋ฅด๊ฒ ํด๊ฒฐํ  ์ ์๋๋ก ๋ธ๋ ฅํ๊ฒ ์ต๋๋ค.



2. ์ต๋ช์ฌ

- ๋ฐฐ์ด์ : git branch์ ๋ํด์ ๋ฐฐ์ฐ๊ณ  ์ด๋ฅผ ์คํํ๋ฉด์ ๊ฐ๋ฐ์๋ค์ด ์ผํ๋ ๋ฐฉ์์ ๋ํด์ ์กฐ๊ธ ๋ ๋ฐฐ์ฐ๊ฒ ๋ ๊ฒ ๊ฐ์ต๋๋ค. ํ์ง๋ง ์ ๊ฐ ์ค์๋ก master์ push๋ฅผ ํ๋ ๋ฐ๋์ ๊น ์ถฉ๋์ด ๋ฐ์ํด ๋ฐฐ์ด ๊ฒ์ ์ ๋๋ก ํ์ฉํ์ง ๋ชปํด ์์ฌ์ ์ต๋๋ค.  



- ๋๋์ : ์ด๋ฒ์ฃผ๋ git branch๋ฅผ ๋ฐฐ์ฐ๊ณ  ํ์ฉํด์ผ ํด์ ์ง๋์ฃผ์ฒ๋ผ ํ๋ฉด๊ณต์ ๋ฅผ ํตํด ๊ฐ์ด ์ผํ๋ ๊ฒ์ด ์๋๋ผ ์๋ฌด๋ฅผ ๋๋ ์ ์์์ ํ์ต๋๋ค. ํ์ง๋ง ์ง๋์ฃผ๋ณด๋ค ํด์ผํ  ์ผ์ด ๋ง์์ ์ฝ์ง๋ ์์๋ ๊ฒ ๊ฐ์ต๋๋ค. ์๊ฐ์ด ์ข๋ง ๋ ์์์ผ๋ฉด ๊พธ๋ฏธ๊ธฐ๋ ํ์ํ๋ฐ ํ๋ก์ ํธ๋ฅผ ๋๋ด๊ณ  ๋๋ ์๊ฐ์ด ์ผ๋ง ๋จ์ง ์์์ ์์ฌ์ ์ต๋๋ค. ๊ทธ๋๋ ์ฑ๊ณต์ ์ผ๋ก ํ๋ก์ ํธ๋ฅผ ๋ง์น  ์ ์์ด์ ๋ฟ๋ฏํ์ต๋๋ค.
