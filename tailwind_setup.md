<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Installation Guide</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background-color: #f9f9f9;
      color: #333;
    }
    h2 {
      font-size: 1.8em;
      color: #333;
      border-bottom: 2px solid #eee;
      padding-bottom: 0.3em;
      margin-bottom: 1em;
    }
    h3 {
      font-size: 1.5em;
      color: #555;
      margin-bottom: 0.5em;
    }
    ol {
      margin-left: 1.5em;
      margin-bottom: 2em;
    }
    li {
      margin-bottom: 1em;
    }
    pre, code {
      background-color: #f4f4f4;
      padding: 10px;
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.95em;
      border-radius: 3px;
      display: block;
      overflow-x: auto;
      margin: 10px 0;
    }
    code.inline-code {
      display: inline;
      padding: 2px 5px;
      border-radius: 3px;
    }
    blockquote {
      margin: 1.5em 0;
      padding: 0.5em 1em;
      background-color: #f9f9f9;
      border-left: 3px solid #ccc;
      font-style: italic;
      color: #555;
    }
    a {
      color: #008080;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <h2>Installation</h2>

  <h2>Step-by-step instructions</h2>

  <ol>
    <li>
      <strong>Install the django-tailwind package via pip:</strong>
      <pre><code>python -m pip install django-tailwind</code></pre>
      If you want to use automatic page reloads during development (see steps 10-12 below), use the <a href="https://nodejs.org/">reload</a> extras, which installs the <code class="inline-code">django-browser-reload</code> package in addition:
      <pre><code>python -m pip install 'django-tailwind[reload]'</code></pre>
      Alternatively, you can install the latest development version via:
      <pre><code>python -m pip install git+https://github.com/timonweb/django-tailwind.git</code></pre>
    </li>

    <li>
      <strong>Add 'tailwind' to INSTALLED_APPS in settings.py:</strong>
      <pre><code>INSTALLED_APPS = [

# other Django apps

'tailwind',
]</code></pre>
</li>

    <li>
      <strong>Create a Tailwind CSS compatible Django app (I like to call it <code class="inline-code">theme</code>):</strong>
      <pre><code>python manage.py tailwind init</code></pre>
    </li>

    <li>
      <strong>Add your newly created 'theme' app to <code class="inline-code">INSTALLED_APPS</code> in settings.py:</strong>
      <pre><code>INSTALLED_APPS = [

# other Django apps

'tailwind',
'theme'
]</code></pre>
</li>

    <li>
      <strong>Register the generated 'theme' app by adding the following line to settings.py file:</strong>
      <pre><code>TAILWIND_APP_NAME = 'theme'</code></pre>
    </li>

    <li>
      <strong>Make sure that the INTERNAL_IPS list is present in the settings.py file and contains the <code class="inline-code">127.0.0.1</code> IP address:</strong>
      <pre><code>INTERNAL_IPS = [

"127.0.0.1",
]</code></pre>
</li>

    <li>
      <strong>Install Tailwind CSS dependencies, by running the following command:</strong>
      <pre><code>python manage.py tailwind install</code></pre>
    </li>

    <li>
      The Django Tailwind comes with a simple <code class="inline-code">base.html</code> template located at <code class="inline-code">your_tailwind_app_name/templates/base.html</code>. You can always extend or delete it if you already have a layout.
    </li>

    <li>
      If you are not using the <code class="inline-code">base.html</code> template that comes with Django Tailwind, add <code class="inline-code">{% tailwind_css %}</code> to the <code class="inline-code">base.html</code> template:
      <pre><code>{% load static tailwind_tags %}

...

<head>
  ...
  {% tailwind_css %}
  ...
</head>
<!-- The {% tailwind_css %} tag includes Tailwind’s stylesheet. -->
</code></pre>
    </li>

    <li>
      <strong>Add and configure <code class="inline-code">django_browser_reload</code> for automatic page and CSS refreshes in development mode. Add it to <code class="inline-code">INSTALLED_APPS</code> in settings.py:</strong>
      <pre><code>INSTALLED_APPS = [

# other Django apps

'tailwind',
'theme',
'django_browser_reload'
]</code></pre>
</li>

    <li>
      <strong>In settings.py, add the middleware:</strong>
      <pre><code>MIDDLEWARE = [

# other middleware

"django_browser_reload.middleware.BrowserReloadMiddleware",

# ...

]</code></pre>
The middleware should be listed after any that encode the response, such as Django’s <code class="inline-code">GZipMiddleware</code>.
</li>

    <li>
      <strong>Include <code class="inline-code">django_browser_reload</code> URL in your root url.py:</strong>
      <pre><code>from django.urls import include, path

urlpatterns = [
...,
path("__reload__/", include("django_browser_reload.urls")),
]</code></pre>
</li>

    <li>
      <strong>Start the development server by running the following command in your terminal:</strong>
      <pre><code>python manage.py tailwind start</code></pre>
    </li>

  </ol>

</body>
</html>
