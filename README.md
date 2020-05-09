# Introduction

django-contactforms is a very simple application package. It's help you create your contact forms. Please refer to the tests to see how it's done.

## Prerequisites

- Django 3+
- Python 3+

## Installation

To install this just type:

```
pip install django-contactforms
```

After installation is complete:

1. add 'contactforms' to your INSTALLED_APPS directive and
2. Migrate ContactForms: `./manage.py migrate contactforms`
3. or if you don't: `./manage.py makemigrations contactforms`
4. And then migrate again: `./manage.py migrate contactforms`

## Usage

A basic usage of django-contactforms could be (example):

```django
# templates/contact/contact.html
 <div class="row">
  <form action="{% url 'contact' %}" method="post">
    <h3>Send a Message</h3>
    {% csrf_token %}
    <div class="form-group">
      {% if messages %}
        {% for message in messages %}
        <span{% if message.tags %} class="{{ message.tags }}"{% endif %} style="color: green">{{ message }}</span>
        {% endfor %}
      {% endif %}
    </div>
    <div class="form-group">
      {{ forms.name }}
    </div>
    <div class="form-group">
      {{ forms.email }}
    </div>
    <div class="form-group">
      {{ forms.subject }}
    </div>
    <div class="form-group">
      {{ forms.message }}
    </div>
    <button class="btn btn-primary" type="submit">Submit</button>
  </form>
</div>
```

Added this line in home file or where you using contact forms.
```
    {% include "contact/contact.html" %}
```
URL configuration
----------------------

The easiest way to set up the views in ``django-contactforms`` is to just use the provided ``URLconf``, found at ``contactforms.urls``.
You can include it wherever you like in your site's URL configuration; for example, to have it live at the URL ``/contact/``:

```
    from django.urls import path, include

    urlpatterns = [
        # ....
        path('contact/', include('contactforms.urls')),
    ]
```


## A note on the authors of this project

Hello, I am Sajib Hossain. I am the author of this project. If you face problem to install or setup this package please feel free to contact with me. I always try to help you. If you want to add someting in this package always welcome to pull request.

[Facebook](https://web.facebook.com/sajib1066 "Facebook")


