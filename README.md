# Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

# Tutorial

- Following the simple Polls application from the [documentation tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)

# Installation

- Create a new virtual environment and run

```
pip install Django
```

# Create a new project & application

- To set up a new project

```
django-admin startproject [project_name] [local_directory_path]
```

- To add a new application

```
python manage.py startapp [application_name]
```

## Projects vs. apps

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

## Philosophy of apps

Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.

# Running dev server

```
python manage.py runserver

```

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.
