

## Installation

## Step-by-step instructions

1. ### **Install the django-tailwind package via pip:**

```python
python -m pip install django-tailwind
```

If you want to use automatic page reloads during development `(see steps 10-12 below)` use the [reload] extras, which installs the `django-browser-reload package` in addition:

```python
python -m pip install 'django-tailwind[reload]'
```

Alternatively, you can install the latest development version via:

```python
python -m pip install git+https://github.com/timonweb/django-tailwind.git
```

2. ### **Add 'tailwind' to INSTALLED_APPS in settings.py:**

```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
]
```

3. ### **Create a Tailwind CSS compatible Django app, I like to call it `theme`:**

```python
python manage.py tailwind init
```

4. ### **Add your newly created 'theme' app to `INSTALLED_APPS in settings.py`:**

```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme'
]
```

5. ### **Register the generated 'theme' app by adding the following line to settings.py file:**

```python
TAILWIND_APP_NAME = 'theme'
```

7. ### **Make sure that the INTERNAL_IPS list is present in the settings.py file and contains the `127.0.0.1` ip address:**

```python
INTERNAL_IPS = [
    "127.0.0.1",
]
```

8. ### **Install Tailwind CSS dependencies, by running the following command:**

```python
python manage.py tailwind install
```

9. ### The Django Tailwind comes with a simple base.html template located at `your_tailwind_app_name/templates/base.html`. You can always extend or delete it if you already have a layout.

10. ### If you are not using the base.html template that comes with Django Tailwind, add `{% tailwind_css %}` to the base.html template:

```html
{% load static tailwind_tags %} ...
<head>
  ... {% tailwind_css %} ...
</head>
The {% tailwind_css %} tag includes Tailwind’s stylesheet.
```

11. Let’s also add and configure `django_browser_reload`, which takes care of **automatic page and css refreshes in the development mode**. Add it to INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [

# other Django apps

'tailwind',
'theme',
'django_browser_reload'
]
```

12. ### **Staying in settings.py, add the middleware:**

```python
MIDDLEWARE = [

# ...

"django_browser_reload.middleware.BrowserReloadMiddleware",

# ...

]
```

- The middleware should be listed after any that encode the response, such as `Django’s GZipMiddleware`. The middleware automatically inserts the required script tag on HTML responses before </body> when DEBUG is True.

13. ### **Include django_browser_reload URL in your root url.py:**

```python
from django.urls import include, path
urlpatterns = [
...,
path("__reload__/", include("django_browser_reload.urls")),
]
```

Finally, you should be able to use Tailwind CSS classes in HTML.

14. ### **Start the development server by running the following command in your terminal:**

```python
python manage.py tailwind start
```
